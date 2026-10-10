// Albaruthenica - Main Application Logic

let map;
let markerCluster;
let allPlaces = [];
let allPersons = [];
let markersMap = new Map();
let currentLang = localStorage.getItem('albaruthenica_lang') || 'by';
let activeCategory = 'all';
let searchQuery = '';
let personsSearchQuery = '';
let selectedPlaceId = null;
let selectedPersonId = null;
let pickCoordsMode = false;
let tempPickMarker = null;
let pendingPickedCoords = null;
let targetPlaceForCoordsCorrection = null;

// Admin moderation state
let isAdminMode = localStorage.getItem('albaruthenica_admin_mode') === 'true';
let filterOnlyUnverified = false;
let adminPickMode = false;
let activeDraggableMarker = null;

// Category config with distinct colors and crisp SVG glyph icons
const CATEGORY_CONFIG = {
  mustSee: {
    color: '#d97706',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>`
  },
  city: {
    color: '#8b5cf6',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M15 11V5l-3-3-3 3v2H3v14h18V11h-6zm-8 7H5v-2h2v2zm0-4H5v-2h2v2zm0-4H5V8h2v2zm6 8h-2v-2h2v2zm0-4h-2v-2h2v2zm0-4h-2V8h2v2zm0-4h-2V4.5l1-1 1 1V6zm6 12h-2v-2h2v2zm0-4h-2v-2h2v2z"/></svg>`
  },
  monument: {
    color: '#d97706',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm-3 8a3 3 0 0 0-3 3v2h12v-2a3 3 0 0 0-3-3H9zm-5 7h16v2H4v-2zm-2 3h20v2H2v-2z"/></svg>`
  },
  historical: {
    color: '#dc2626',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M18 20V8.5l-2-1.5V4h-2v3h-1V4h-2v3h-1V4H8v3l-2 1.5V20H2v2h20v-2h-4zM9 19H7v-8h2v8zm4 0h-2v-4a1 1 0 0 1 2 0v4zm4 0h-2v-8h2v8z"/></svg>`
  },
  culture: {
    color: '#2563eb',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2L2 7v2h20V7L12 2zM4 11v7h3v-7H4zm6 0v7h4v-7h-4zm7 0v7h3v-7h-3zM2 20v2h20v-2H2z"/></svg>`
  },
  church: {
    color: '#7c3aed',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M11 1.5h2v2.5h2.5v2H13v3l6 4v9h-6v-5a1 1 0 0 0-2 0v5H5v-9l6-4V6H8.5V4H11V1.5z"/></svg>`
  },

  plaque: {
    color: '#059669',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M4 3h16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm2 4v2h12V7H6zm0 4v2h12v-2H6zm0 4v2h8v-2H6z"/></svg>`
  },
  grave: {
    color: '#475569',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2C8.69 2 6 4.69 6 8v12h12V8c0-3.31-2.69-6-6-6zm0 4c.55 0 1 .45 1 1v1h1c.55 0 1 .45 1 1s-.45 1-1 1h-1v4c0 .55-.45 1-1 1s-1-.45-1-1v-4H9c-.55 0-1-.45-1-1s.45-1 1-1h1V7c0-.55.45-1 1-1zm-8 16h16v2H4v-2z"/></svg>`
  },
  prison: {
    color: '#475569',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M2 3h20v2H2V3zm0 16h20v2H2v-2zM5 5h2v14H5V5zm4 0h2v14H9V5zm4 0h2v14h-2V5zm4 0h2v14h-2V5z"/></svg>`
  },
  embassy: {
    color: '#0284c7',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2l4 2.5-4 2.5V2zm-9 6h18v2H3V8zm2 3h2v7H5v-7zm5 0h2v7h-2v-7zm5 0h2v7h-2v-7zm5 0h2v7h-2v-7zM2 19h20v3H2v-3z"/></svg>`
  }
};
const CATEGORY_ICONS = CATEGORY_CONFIG;

// Ensure any image loaded dynamically or statically sends no-referrer to avoid 403 on Wikimedia
const imgReferrerObserver = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    mutation.addedNodes.forEach((node) => {
      if (node.nodeType === 1) {
        if (node.tagName === 'IMG' && !node.hasAttribute('referrerpolicy')) {
          node.setAttribute('referrerpolicy', 'no-referrer');
        }
        node.querySelectorAll?.('img:not([referrerpolicy])').forEach(img => {
          img.setAttribute('referrerpolicy', 'no-referrer');
        });
      }
    });
  });
});
imgReferrerObserver.observe(document.documentElement, { childList: true, subtree: true });

// Universal Wikimedia thumbnail resolution helper
// Valid thumbnail buckets allowed by Wikimedia Commons: 120, 250, 330, 500, 960, 1280
function getWikimediaThumb(url, width = 250) {
  if (!url || typeof url !== 'string') return url;
  if (!url.includes('wikimedia.org')) return url;
  // ONLY rewrite commons.wikimedia.org URLs! Local language wikipedias (like be.wikipedia.org) do not support thumb endpoints in this manner
  if (!url.includes('/wikipedia/commons/')) {
    return url;
  }

  // Snap requested width to closest valid Wikimedia thumbnail bucket
  const allowed = [120, 250, 330, 500, 960, 1280];
  let targetWidth = 250;
  if (allowed.includes(width)) {
    targetWidth = width;
  } else {
    targetWidth = allowed.reduce((prev, curr) => Math.abs(curr - width) < Math.abs(prev - width) ? curr : prev);
  }

  // Strip query parameters
  const cleanUrl = url.split('?')[0];

  // Match /thumb/ path: .../wikipedia/commons/thumb/a/ab/Filename.ext/([0-9]+px-Filename.ext)
  const thumbMatch = cleanUrl.match(/^(https?:\/\/(?:upload|thumb)\.wikimedia\.org\/wikipedia\/(?:commons|[a-z]+)\/thumb\/([^\/]+\/[^\/]+\/[^\/]+))\/(?:lossy-page\d+-)?(?:page\d+-)?\d+px-[^\/]+$/);
  if (thumbMatch) {
    const base = thumbMatch[1];
    const rel = thumbMatch[2];
    const filename = rel.split('/').pop();
    if (filename.toLowerCase().endsWith('.svg')) {
      return `${base}/${targetWidth}px-${filename}.png`;
    }
    return `${base}/${targetWidth}px-${filename}`;
  }

  // Match raw unscaled Commons path: .../wikipedia/commons/a/ab/Filename.ext
  const rawMatch = cleanUrl.match(/^(https?:\/\/(?:upload|thumb)\.wikimedia\.org\/wikipedia\/(?:commons|[a-z]+))\/([^\/]+\/[^\/]+\/[^\/]+)$/);
  if (rawMatch) {
    const hostPrefix = rawMatch[1];
    const rel = rawMatch[2];
    const filename = rel.split('/').pop();
    if (filename.toLowerCase().endsWith('.svg')) {
      return `${hostPrefix}/thumb/${rel}/${targetWidth}px-${filename}.png`;
    }
    return `${hostPrefix}/thumb/${rel}/${targetWidth}px-${filename}`;
  }

  return cleanUrl;
}
window.getWikimediaThumb = getWikimediaThumb;


document.addEventListener('DOMContentLoaded', () => {
  // Check admin parameter in URL query or hash: ?admin or #admin
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('admin') || window.location.hash === '#admin') {
    isAdminMode = true;
    localStorage.setItem('albaruthenica_admin_mode', 'true');
  }

  initI18n();
  initAuth();
  initMap();
  loadPlaces();
  setupEventListeners();
  updateAdminUI();
  checkUrlHash();
});

// Initialize i18n texts
function initI18n() {
  const dict = window.i18n[currentLang] || window.i18n.by;

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.textContent = dict[key];
    }
  });

  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.getAttribute('data-i18n-placeholder');
    if (dict[key]) {
      el.placeholder = dict[key];
    }
  });

  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-lang') === currentLang);
  });

  renderCategoryPills();
  updateStats();
}

let baseLayers = {};
let layerControl = null;
let activeBaseLayerKey = 'osm';

function setLanguage(lang) {
  if (['by', 'ru', 'en'].includes(lang)) {
    currentLang = lang;
    localStorage.setItem('albaruthenica_lang', lang);
    initI18n();
    updateAuthUI();
    updateLayerControl();
    updateAdminUI();
    renderSidebarList();
    if (selectedPlaceId) {
      showPlaceDetail(selectedPlaceId, false);
    }
    updateAllMarkersTooltips();
    if (document.getElementById('allPersonsModal')?.classList.contains('open')) {
      renderPersonsGrid();
    }
    if (selectedPersonId && document.getElementById('personModal')?.classList.contains('open')) {
      openPersonDetail(selectedPersonId, false);
    }
  }
}

// Initialize Leaflet Map
function initMap() {
  // Center on Europe initially
  map = L.map('map', {
    center: [52.5, 20.0],
    zoom: 5,
    minZoom: 2,
    zoomControl: true
  });

  setupBaseLayers();

  markerCluster = L.markerClusterGroup({
    showCoverageOnHover: false,
    maxClusterRadius: 45,
    spiderfyOnMaxZoom: true
  });

  map.addLayer(markerCluster);

  // Handle adaptive popup image orientation dynamically
  map.on('popupopen', (e) => {
    const popupEl = e.popup?.getElement();
    if (!popupEl) return;
    const img = popupEl.querySelector('.popup-img');
    if (img) {
      if (img.complete && img.naturalWidth) {
        handlePopupImageOrientation(img);
      } else {
        img.addEventListener('load', () => handlePopupImageOrientation(img), { once: true });
      }
    }
  });

  // Map click for coordinate picker (Add Place modal, Admin moderation, or Place coordinate correction)
  map.on('click', (e) => {
    if (adminPickMode && selectedPlaceId) {
      handleAdminMapClick(e.latlng);
      return;
    }

    if (targetPlaceForCoordsCorrection || pickCoordsMode) {
      handleMapPickClick(e.latlng);
      return;
    }
  });
}

// Setup base layers (Esri Street, OpenStreetMap, HOT, Topo, Satellite)
function setupBaseLayers() {
  const esriStreetLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, METI, TomTom',
    maxZoom: 19
  });

  const osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19,
    referrerPolicy: 'strict-origin-when-cross-origin'
  });

  const osmHotLayer = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles courtesy of Humanitarian OpenStreetMap Team',
    maxZoom: 19
  });

  const esriTopoLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; USGS, Intermap, TomTom, FAO, NPS, NRCAN',
    maxZoom: 19
  });

  const satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP',
    maxZoom: 19
  });

  baseLayers = {
    esriStreet: esriStreetLayer,
    osm: osmLayer,
    osmHot: osmHotLayer,
    esriTopo: esriTopoLayer,
    satellite: satelliteLayer
  };

  if (!baseLayers[activeBaseLayerKey]) {
    activeBaseLayerKey = 'osm';
  }

  // Add default layer (OpenStreetMap)
  baseLayers[activeBaseLayerKey].addTo(map);

  map.on('baselayerchange', (e) => {
    for (const [key, layer] of Object.entries(baseLayers)) {
      if (e.layer === layer) {
        activeBaseLayerKey = key;
        break;
      }
    }
  });

  updateLayerControl();
}

// Update layer control with current language labels
function updateLayerControl() {
  if (layerControl) {
    map.removeControl(layerControl);
  }

  const dict = window.i18n[currentLang] || window.i18n.by;
  const layerLabels = {
    [dict.layerOSM || 'OpenStreetMap']: baseLayers.osm,
    [dict.layerOSMHot || 'OpenStreetMap (HOT)']: baseLayers.osmHot,
    [dict.layerStreet || 'Карта вуліц (Esri)']: baseLayers.esriStreet,
    [dict.layerTopo || 'Тапаграфічная (Esri)']: baseLayers.esriTopo,
    [dict.layerSatellite || 'Спадарожнік (Esri)']: baseLayers.satellite
  };

  layerControl = L.control.layers(layerLabels, null, {
    position: 'topright',
    collapsed: true
  }).addTo(map);
}

// Client-side overrides for coordinates & verification status (moderation)
function getPlaceOverrides() {
  try {
    const o1 = JSON.parse(localStorage.getItem('albaruthenica_place_overrides') || '{}');
    const o2 = JSON.parse(localStorage.getItem('albaruthenica_overrides') || '{}');
    return { ...o2, ...o1 };
  } catch (e) {
    return {};
  }
}

function savePlaceOverride(placeId, data) {
  const overrides = getPlaceOverrides();
  overrides[placeId] = {
    ...(overrides[placeId] || {}),
    ...data
  };
  try {
    localStorage.setItem('albaruthenica_place_overrides', JSON.stringify(overrides));
    localStorage.setItem('albaruthenica_overrides', JSON.stringify(overrides));
  } catch (e) {
    console.warn('Failed to save override to localStorage:', e);
  }
  updateAdminUI();
}

// Fetch places & persons data
async function loadPlaces() {
  try {
    const response = await fetch('data/places.json?v=' + Date.now());
    if (!response.ok) throw new Error('Failed to load places.json');
    allPlaces = await response.json();
  } catch (error) {
    console.warn('Fetch places.json failed, falling back to window.INITIAL_PLACES:', error);
    if (window.INITIAL_PLACES && Array.isArray(window.INITIAL_PLACES)) {
      allPlaces = window.INITIAL_PLACES;
    }
  }

  // Merge user custom places from localStorage
  try {
    const userPlaces = JSON.parse(localStorage.getItem('albaruthenica_user_places') || '[]');
    if (Array.isArray(userPlaces) && userPlaces.length > 0) {
      userPlaces.forEach(up => {
        if (!allPlaces.some(p => p.id === up.id)) {
          allPlaces.unshift(up);
        }
      });
    }
  } catch (err) {
    console.warn('Error reading albaruthenica_user_places:', err);
  }

  // Apply localStorage overrides (from user moderation)
  const overrides = getPlaceOverrides();
  allPlaces.forEach(p => {
    if (overrides[p.id]) {
      if (Array.isArray(overrides[p.id].coordinates)) {
        p.coordinates = overrides[p.id].coordinates;
      }
      if (typeof overrides[p.id].unverifiedCoordinates !== 'undefined') {
        p.unverifiedCoordinates = overrides[p.id].unverifiedCoordinates;
        p.isUnverifiedCoordinates = overrides[p.id].unverifiedCoordinates;
      }
      if (overrides[p.id].image) {
        p.image = overrides[p.id].image;
      }
    }
  });

  try {
    const responsePersons = await fetch('data/persons.json?v=' + Date.now());
    if (!responsePersons.ok) throw new Error('Failed to load persons.json');
    allPersons = await responsePersons.json();
  } catch (error) {
    console.warn('Fetch persons.json failed, falling back to window.INITIAL_PERSONS:', error);
    if (window.INITIAL_PERSONS && Array.isArray(window.INITIAL_PERSONS)) {
      allPersons = window.INITIAL_PERSONS;
    }
  }

  renderMarkers();
  renderSidebarList();
  updateStats();
  updateAdminUI();

  // Check if initial hash matches a place or person
  checkUrlHash();
}

// Get all persons connected to a place
function getPersonsForPlace(place) {
  if (!place) return [];
  const personIds = new Set();
  if (place.personId) personIds.add(place.personId);
  if (Array.isArray(place.personIds)) {
    place.personIds.forEach(id => personIds.add(id));
  }
  if (Array.isArray(place.items)) {
    place.items.forEach(it => {
      if (it.personId) personIds.add(it.personId);
    });
  }

  // Also check persons whose placeIds include this place id
  allPersons.forEach(p => {
    if (Array.isArray(p.placeIds) && p.placeIds.includes(place.id)) {
      personIds.add(p.id);
    }
  });

  return Array.from(personIds)
    .map(id => allPersons.find(p => p.id === id))
    .filter(Boolean);
}

// Get all places connected to a person
function getPlacesForPerson(person) {
  if (!person) return [];
  const placeIds = new Set(person.placeIds || []);

  allPlaces.forEach(pl => {
    if (pl.personId === person.id) placeIds.add(pl.id);
    if (Array.isArray(pl.personIds) && pl.personIds.includes(person.id)) placeIds.add(pl.id);
    if (Array.isArray(pl.items) && pl.items.some(it => it.personId === person.id)) {
      placeIds.add(pl.id);
    }
  });

  return Array.from(placeIds)
    .map(id => allPlaces.find(pl => pl.id === id))
    .filter(Boolean);
}

// Render category filter pills
function renderCategoryPills() {
  const container = document.getElementById('categoryFilters');
  if (!container) return;

  const dict = window.i18n[currentLang];
  const categories = [
    { id: 'all', label: dict.allCategories },
    { id: 'mustSee', label: dict.filterMustSee || 'Must-see' },
    { id: 'city', label: dict.categories.city || 'Гарады' },
    { id: 'monument', label: dict.categories.monument },
    { id: 'grave', label: dict.categories.grave },
    { id: 'prison', label: dict.categories.prison || 'Месцы зняволення' },
    { id: 'church', label: dict.categories.church },
    { id: 'culture', label: dict.categories.culture },
    { id: 'historical', label: dict.categories.historical },
    { id: 'plaque', label: dict.categories.plaque },
    { id: 'embassy', label: dict.categories.embassy || 'Дыпламатычныя місіі' }
  ];

  container.innerHTML = categories.map(cat => {
    const isAct = activeCategory === cat.id;
    const conf = CATEGORY_CONFIG[cat.id];
    const iconHtml = conf ? `<span class="category-pill-icon" style="background-color: ${conf.color}">${conf.icon}</span>` : '';
    return `
      <button class="category-pill ${isAct ? 'active' : ''} category-${cat.id}" data-cat="${cat.id}">
        ${iconHtml}
        <span>${cat.label}</span>
      </button>
    `;
  }).join('');

  container.querySelectorAll('.category-pill').forEach(btn => {
    btn.addEventListener('click', () => {
      activeCategory = btn.getAttribute('data-cat');
      renderCategoryPills();
      filterAndRender();
    });
  });
}

// Helper to get localized value
function getLocalized(obj) {
  if (!obj) return '';
  if (typeof obj === 'string') return obj;
  return obj[currentLang] || obj.by || obj.ru || obj.en || '';
}

// Helper to escape HTML safely
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Format title with subtitles in gray bold (падзагаловак)
function formatPlaceTitle(title, city = '') {
  if (!title) return '';
  let str = String(title).trim();

  // 1. Strip redundant bracketed marker like "(комплексны аб’ект)" or "(комплексны аб'ект)"
  str = str.replace(/\s*\((?:комплексны аб[’']ект|комплексный объект|complex object|city hub)\)\s*/gi, '').trim();

  const cityStr = typeof city === 'string' ? city.trim().toLowerCase() : '';

  // 2. Trailing parentheses: e.g. "Title (Subtitle)"
  const trailingMatch = str.match(/^(.*?)\s*\(([^()]+)\)\s*$/);
  if (trailingMatch && trailingMatch[1].trim()) {
    const mainText = trailingMatch[1].trim();
    const subText = trailingMatch[2].trim();
    const subLower = subText.toLowerCase();

    // If subtitle equals or contains city, or is a common city name in parentheses, do NOT duplicate it!
    if (cityStr && (subLower === cityStr || subLower.includes(cityStr) || cityStr.includes(subLower))) {
      return `<span class="title-main">${escapeHtml(mainText)}</span>`;
    }
    if (['варшава', 'warsaw', 'варшаве', 'парыж', 'paris', 'париж', 'вільня', 'vilnius', 'вильнюс', 'кракаў', 'krakow', 'краков', 'мінск', 'minsk', 'мінску', 'лондан', 'london', 'рым', 'rome', 'рыме', 'берлін', 'berlin', 'вест-пойнт', 'даўгаўпілс', 'дзвінск', 'лентварыс', 'кенгір', 'іерусалім', 'ерусалім'].includes(subLower)) {
      return `<span class="title-main">${escapeHtml(mainText)}</span>`;
    }

    return `<span class="title-main">${escapeHtml(mainText)}</span><span class="title-sub">${escapeHtml(subText)}</span>`;
  }

  // 3. Dash separator: "Main Title — Subtitle" or "Main Title – Subtitle"
  const dashMatch = str.match(/^(.*?)\s+[—–]\s+(.+)$/);
  if (dashMatch && dashMatch[1].trim() && dashMatch[2].trim()) {
    const mainText = dashMatch[1].trim();
    let subText = dashMatch[2].trim();
    subText = subText.replace(/^\((.+)\)$/, '$1');
    const subLower = subText.toLowerCase();
    if (cityStr && (subLower === cityStr || subLower.includes(cityStr) || cityStr.includes(subLower))) {
      return `<span class="title-main">${escapeHtml(mainText)}</span>`;
    }
    return `<span class="title-main">${escapeHtml(mainText)}</span><span class="title-sub">${escapeHtml(subText)}</span>`;
  }

  // 4. Mid-string parentheses: e.g. "Месца абвяшчэння ССРБ (БССР) у Смаленску"
  if (str.includes('(') && str.includes(')')) {
    const formatted = escapeHtml(str).replace(/\(([^()]+)\)/g, '<span class="title-sub-inline">($1)</span>');
    return `<span class="title-main">${formatted}</span>`;
  }

  return `<span class="title-main">${escapeHtml(str)}</span>`;
}

// Create custom pin HTML icon (round colored pin with centered white SVG icon)
function createCustomMarkerIcon(category, isUnverified = false) {
  const conf = CATEGORY_CONFIG[category] || CATEGORY_CONFIG.historical;
  const unverifiedClass = isUnverified ? ' unverified-pin' : '';
  return L.divIcon({
    className: 'custom-pin-wrapper',
    html: `<div class="custom-pin category-${category}${unverifiedClass}" style="--pin-color: ${conf.color};" title="${category}">${conf.icon}</div>`,
    iconSize: [28, 28],
    iconAnchor: [14, 14],
    popupAnchor: [0, -16]
  });
}

// Dynamic Image Orientation Handlers (portrait vs landscape)
function handlePopupImageOrientation(img) {
  if (!img) return;
  const nw = img.naturalWidth;
  const nh = img.naturalHeight;
  if (!nw || !nh) return;

  const wrap = img.closest('.popup-img-wrap');
  const card = img.closest('.popup-card');
  if (!wrap) return;

  const ratio = nh / nw;

  if (ratio > 1.12) {
    // Strongly vertical/portrait (e.g. portraits, monuments, tall stelae)
    wrap.classList.add('is-portrait');
    wrap.classList.remove('is-landscape', 'is-square');
    if (card) card.classList.add('has-portrait');
  } else if (ratio < 0.88) {
    // Landscape / panoramic
    wrap.classList.add('is-landscape');
    wrap.classList.remove('is-portrait', 'is-square');
    if (card) card.classList.remove('has-portrait');
  } else {
    // Roughly square
    wrap.classList.add('is-square');
    wrap.classList.remove('is-portrait', 'is-landscape');
    if (card) card.classList.remove('has-portrait');
  }
}

function handleHeroImageOrientation(img) {
  if (!img) return;
  const nw = img.naturalWidth;
  const nh = img.naturalHeight;
  if (!nw || !nh) return;

  if (nh / nw > 1.12) {
    img.classList.add('is-portrait');
    img.classList.remove('is-wide');
  } else if (nw / nh > 1.9) {
    img.classList.add('is-wide');
    img.classList.remove('is-portrait');
  } else {
    img.classList.remove('is-portrait', 'is-wide');
  }
}

// Render markers on map
function renderMarkers() {
  markerCluster.clearLayers();
  markersMap.clear();

  const filtered = getFilteredPlaces();

  filtered.forEach(place => {
    const [lat, lng] = place.coordinates;
    const title = getLocalized(place.title);
    const city = getLocalized(place.city);
    const country = getLocalized(place.country);
    const categoryName = window.i18n[currentLang].categories[place.category] || place.category;

    const marker = L.marker([lat, lng], {
      icon: createCustomMarkerIcon(place.category, place.unverifiedCoordinates)
    });

    // Custom popup
    const unverifiedPopupNotice = place.unverifiedCoordinates ? `
      <div class="unverified-coords-badge" style="margin-bottom: 5px;">
        ${window.i18n[currentLang]?.unverifiedCoordsBadge || 'Неправераныя каардынаты'}
      </div>
    ` : '';

    const nestedPopupNotice = (place.items && place.items.length > 0) ? `
      <div class="place-card-nested-badge" style="display: inline-block; margin-bottom: 5px; font-size: 0.72rem;">
        ${place.items.length} ${place.category === 'city' ? (window.i18n[currentLang]?.nestedCityObjectsBadge || 'пад’аб’ектаў') : (window.i18n[currentLang]?.nestedObjectsBadge || 'аб’ектаў')}
      </div>
    ` : '';

    const popupHtml = `
      <div class="popup-card">
        ${place.image ? `
          <div class="popup-img-wrap">
            <img src="${getWikimediaThumb(place.image, 500)}" alt="${title}" class="popup-img" loading="lazy" referrerpolicy="no-referrer" onload="handlePopupImageOrientation(this)" onerror="this.closest('.popup-img-wrap')?.remove()">
          </div>` : ''}
        <div class="popup-body">
          <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 4px; align-items: center;">
            <span class="place-card-category cat-${place.category}">${categoryName}</span>
            ${nestedPopupNotice}
          </div>
          ${unverifiedPopupNotice}
          <div class="popup-title">${formatPlaceTitle(title, city)}</div>
          <div class="popup-loc">${city}, ${country}</div>
          <button class="btn btn-primary btn-sm" style="width: 100%" onclick="selectPlace('${place.id}')">
            ${window.i18n[currentLang].detailsHeading}
          </button>
        </div>
      </div>
    `;

    marker.bindPopup(popupHtml, { maxWidth: 290, minWidth: 230 });
    marker.on('click', () => {
      highlightSidebarCard(place.id);
    });

    markerCluster.addLayer(marker);
    markersMap.set(place.id, marker);
  });

  map.addLayer(markerCluster);
}

function updateAllMarkersTooltips() {
  renderMarkers();
}

// Filter logic
function getFilteredPlaces() {
  return allPlaces.filter(place => {
    // Admin filter for unverified coordinates only
    if (filterOnlyUnverified && place.unverifiedCoordinates !== true) {
      return false;
    }

    // Category check
    if (activeCategory === 'mustSee') {
      if (place.mustSee !== true) return false;
    } else if (activeCategory !== 'all' && place.category !== activeCategory) {
      return false;
    }

    // Search query check
    if (searchQuery.trim() !== '') {
      let q = searchQuery.toLowerCase().trim();
      if (q.startsWith('#')) q = q.slice(1).trim();
      if (!q) return true;

      const titleBy = (place.title?.by || '').toLowerCase();
      const titleRu = (place.title?.ru || '').toLowerCase();
      const titleEn = (place.title?.en || '').toLowerCase();
      const city = getLocalized(place.city).toLowerCase();
      const country = getLocalized(place.country).toLowerCase();
      const tags = (place.tags || []).join(' ').toLowerCase();
      const desc = getLocalized(place.description).toLowerCase();

      let matches = titleBy.includes(q) || titleRu.includes(q) || titleEn.includes(q) ||
                    city.includes(q) || country.includes(q) || tags.includes(q) || desc.includes(q);

      // Deep search within nested items (artists, paintings, graves)
      if (!matches && place.items && Array.isArray(place.items)) {
        matches = place.items.some(it => {
          const itTitle = (it.title || '').toLowerCase();
          const itAuthor = (it.author || it.person || '').toLowerCase();
          const itDesc = (it.description || '').toLowerCase();
          return itTitle.includes(q) || itAuthor.includes(q) || itDesc.includes(q);
        });
      }

      // Deep search matching associated persons
      if (!matches) {
        const connectedPersons = getPersonsForPlace(place);
        matches = connectedPersons.some(ap => {
          const nameBy = (ap.name?.by || '').toLowerCase();
          const nameRu = (ap.name?.ru || '').toLowerCase();
          const nameEn = (ap.name?.en || '').toLowerCase();
          const role = getLocalized(ap.role).toLowerCase();
          const bio = getLocalized(ap.bio).toLowerCase();
          return nameBy.includes(q) || nameRu.includes(q) || nameEn.includes(q) || role.includes(q) || bio.includes(q);
        });
      }

      if (!matches) return false;
    }

    return true;
  });
}

function filterAndRender() {
  renderMarkers();
  renderSidebarList();
  updateStats();
}

// Render places list in sidebar
function renderSidebarList() {
  const container = document.getElementById('placesList');
  if (!container) return;

  const filtered = getFilteredPlaces();
  const dict = window.i18n[currentLang] || window.i18n.by;

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="padding: 2rem 1rem; text-align: center; color: var(--text-muted); font-size: 0.9rem;">
        ${dict.noResults}
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(place => {
    const title = getLocalized(place.title);
    const city = getLocalized(place.city);
    const country = getLocalized(place.country);
    const categoryName = dict.categories[place.category] || place.category;
    const thumb = getWikimediaThumb(place.image, 250) || 'https://images.unsplash.com/photo-1517824806704-9040b037703b?auto=format&fit=crop&w=200&q=80';

    const unverifiedBadge = place.unverifiedCoordinates ? `
      <span class="unverified-coords-badge" title="${dict.unverifiedCoordsNotice || ''}">
        ${dict.unverifiedCoordsBadge || 'Неправерана'}
      </span>
    ` : '';

    const nestedBadge = (place.items && place.items.length > 0) ? `
      <span class="place-card-nested-badge">
        ${place.items.length} ${place.category === 'city' ? (dict.nestedCityObjectsBadge || 'пад’аб’ектаў') : (dict.nestedObjectsBadge || 'аб’ектаў')}
      </span>
    ` : '';

    const mustSeeBadge = place.mustSee ? `
      <span class="place-card-must-see-badge" title="${dict.mustSeeBadge || 'Пабачыць абавязкова'}">
        ⭐ Must-see
      </span>
    ` : '';

    const thumbImgHtml = place.image ? `
      <img src="${getWikimediaThumb(place.image, 250)}" alt="${title}" class="place-card-thumb" loading="lazy" referrerpolicy="no-referrer" onerror="this.style.display='none'; if(this.nextElementSibling) this.nextElementSibling.style.display='flex';">
      <div class="place-card-thumb-placeholder" style="display:none;" title="${categoryName}">
        ${(CATEGORY_CONFIG[place.category] || CATEGORY_CONFIG.historical).icon}
      </div>
    ` : `
      <div class="place-card-thumb-placeholder" title="${categoryName}">
        ${(CATEGORY_CONFIG[place.category] || CATEGORY_CONFIG.historical).icon}
      </div>
    `;

    return `
      <div class="place-card ${selectedPlaceId === place.id ? 'active' : ''}" 
           id="card-${place.id}"
           onclick="selectPlace('${place.id}')">
        ${thumbImgHtml}
        <div class="place-card-content">
          <div>
            <div class="place-card-title">${formatPlaceTitle(title, city)}</div>
            <div class="place-card-meta">${city}, ${country}</div>
          </div>
          <div class="place-card-badges">
            <span class="place-card-category cat-${place.category}">
              ${categoryName}
            </span>
            ${mustSeeBadge}
            ${unverifiedBadge}
            ${nestedBadge}
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Update stats counter
function updateStats() {
  const counterEl = document.getElementById('statsCounter');
  if (!counterEl) return;

  const filtered = getFilteredPlaces();
  const countries = new Set(filtered.map(p => getLocalized(p.country)));
  const dict = window.i18n[currentLang];

  counterEl.innerHTML = `<span>${dict.statsFound} <strong>${filtered.length}</strong> ${dict.statsPlaces} (<strong>${countries.size}</strong> ${dict.statsCountries})</span>`;
}

// Select a place (click from card or map)
function selectPlace(placeId, updateHash = true) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  selectedPlaceId = placeId;
  highlightSidebarCard(placeId);

  // Pan map smoothly to place without zooming out if already close
  const [lat, lng] = place.coordinates;
  const currentZoom = (map && typeof map.getZoom === 'function') ? map.getZoom() : 13;
  const targetZoom = Math.max(currentZoom, 14);
  map.flyTo([lat, lng], targetZoom, { duration: 0.8 });

  // Open marker popup if available
  const marker = markersMap.get(placeId);
  if (marker) {
    markerCluster.zoomToShowLayer(marker, () => {
      marker.openPopup();
    });
  }

  // Show detailed drawer
  showPlaceDetail(placeId);

  if (updateHash) {
    window.location.hash = `place=${placeId}`;
  }
}

// Highlight card in sidebar
function highlightSidebarCard(placeId) {
  document.querySelectorAll('.place-card').forEach(c => c.classList.remove('active'));
  const card = document.getElementById(`card-${placeId}`);
  if (card) {
    card.classList.add('active');
    card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }
}

// Show Place Detail Drawer
function showPlaceDetail(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  const drawer = document.getElementById('placeDetailDrawer');
  if (!drawer) return;
  drawer.scrollTop = 0;

  const title = getLocalized(place.title);
  const city = getLocalized(place.city);
  const country = getLocalized(place.country);
  const desc = getLocalized(place.description);
  const categoryName = window.i18n[currentLang].categories[place.category] || place.category;
  const [lat, lng] = place.coordinates;
  const dict = window.i18n[currentLang];

  const heroThumb = place.image ? getWikimediaThumb(place.image, 960) : '';
  const heroImg = place.image ? `
    <div class="detail-hero-wrap" id="detailHeroWrap">
      <div class="detail-hero-bg" style="background-image: url('${heroThumb}')"></div>
      <img src="${heroThumb}" alt="${title}" class="detail-hero-img" loading="lazy" referrerpolicy="no-referrer" 
           onerror="handleHeroImageError('${place.id}')"
           onclick="openImageLightbox('${place.image}', '${title.replace(/'/g, "\\'")}')"
           title="Клікніце для прагляду на ўвесь экран">
      <button type="button" class="detail-hero-edit-badge" onclick="openAddImageModal('${place.id}')" title="${dict.btnChangeImage || 'Прапанаваць іншую выяву'}">
        📷 ${dict.btnChangeImage || 'Змяніць'}
      </button>
    </div>` : `
    <div class="detail-no-image-wrap" id="detailHeroWrap">
      <div class="detail-no-image-content">
        <div class="detail-no-image-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
            <circle cx="8.5" cy="8.5" r="1.5"/>
            <polyline points="21 15 16 10 5 21"/>
          </svg>
        </div>
        <div class="detail-no-image-text">
          <span class="detail-no-image-title">${dict.noImageTitle || 'Выява пакуль адсутнічае'}</span>
          <span class="detail-no-image-sub">${dict.noImagePrompt || 'Маеце фатаграфію ці выяву гэтага месца? Дапамажыце праекту!'}</span>
        </div>
        <button type="button" class="btn btn-primary btn-sm detail-add-photo-btn" onclick="openAddImageModal('${place.id}')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px; vertical-align:-1px;">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          ${dict.btnAddImage || 'Дадаць выяву'}
        </button>
      </div>
    </div>
  `;

  const tagsHtml = (place.tags || []).map(t => {
    const safeTag = escapeHtml(t).replace(/'/g, "\\'");
    return `<button type="button" class="detail-tag" onclick="filterByTag('${safeTag}')" title="Фільтраваць па тэгу #${escapeHtml(t)}">#${escapeHtml(t)}</button>`;
  }).join('');


  // Connected persons for this place
  const connectedPersons = getPersonsForPlace(place);
  let associatedPersonsHtml = '';
  if (connectedPersons.length > 0) {
    associatedPersonsHtml = `
      <div class="associated-persons-section">
        <strong style="font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--text-main);">${dict.associatedPersons || 'Звязаныя дзеячы і асобы:'}</strong>
        <div class="associated-persons-list">
          ${connectedPersons.map(p => `
            <div class="associated-person-chip" onclick="openPersonDetail('${p.id}')" title="${getLocalized(p.role)}">
              <img src="${getWikimediaThumb(p.image, 250) || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'}" 
                   alt="${getLocalized(p.name)}" class="associated-person-avatar" loading="lazy" referrerpolicy="no-referrer"
                   onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'">
              <span>${getLocalized(p.name)}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Nested sub-items (artworks, graves, exhibits, city historical spots)
  let nestedItemsHtml = '';
  if (place.items && Array.isArray(place.items) && place.items.length > 0) {
    const isCity = place.category === 'city' || place.isCityHub;
    const itemsHeaderTitle = isCity
      ? (dict.nestedCityObjectsTitle || 'Гістарычныя мясціны, падзеі і сляды ў гэтым горадзе / паселішчы:')
      : (dict.nestedObjectsTitle || 'Укладзеныя аб’екты, творы і пахаванні:');

    nestedItemsHtml = `
      <div class="nested-items-section">
        <div class="nested-items-header">
          <strong>${itemsHeaderTitle}</strong>
          <span class="nested-items-count">${place.items.length}</span>
        </div>
        <div class="nested-items-grid">
        ${place.items.map((it, idx) => {
          const itPerson = resolvePersonForSubItem(it);
          const personName = it.person || it.author || (itPerson ? getLocalized(itPerson.name) : '');
          const personBadge = personName ? `
            <button type="button" class="nested-item-person-btn" onclick="event.stopPropagation(); handlePersonClickFromItem('${itPerson ? itPerson.id : ''}', '${encodeURIComponent(personName)}')" title="${dict.aboutPerson || 'Пра асобу'}">
              <span class="person-icon-dot"></span>
              <span>${personName}</span>
              <span class="person-btn-arrow">&rarr;</span>
            </button>
          ` : '';

          const coordsBadge = (it.needsCoords || it.coordsRequest) ? `
            <span class="coords-request-badge" title="${dict.coordsRequestPrompt || ''}">
              🔍 ${dict.coordsRequestBadge || 'Запыт каардынат'}
            </span>
          ` : '';

          return `
          <div class="nested-item-card ${(it.needsCoords || it.coordsRequest) ? 'has-coords-request' : ''}" onclick="openNestedItemModal('${place.id}', ${idx})" title="${dict.clickToViewDetails || 'Націсніце для прагляду дэталяў'}">
            <div class="nested-item-card-header">
              <div class="nested-item-title">${it.title}</div>
              ${coordsBadge}
              ${it.year ? `<span class="nested-item-year">${it.year}</span>` : ''}
            </div>
            ${personBadge ? `<div class="nested-item-meta">${personBadge}</div>` : ''}
            ${it.description ? `<div class="nested-item-desc">${it.description}</div>` : ''}
            ${it.image ? `<div class="nested-item-image-wrapper"><img src="${getWikimediaThumb(it.image, 330)}" alt="${it.title}" class="nested-item-thumb" loading="lazy" referrerpolicy="no-referrer" onerror="this.closest('.nested-item-image-wrapper')?.remove()"></div>` : ''}
            <div class="nested-item-card-footer">
              <span class="nested-item-view-btn">${dict.viewDetails || 'Падрабязней'} &rarr;</span>
            </div>
          </div>
        `}).join('')}
        </div>
      </div>
    `;
  }

  // Categorized links (Wikipedia, background articles, catalog, sources)
  const combinedLinks = [];
  const seenUrls = new Set();

  if (Array.isArray(place.links)) {
    for (const l of place.links) {
      if (l && l.url && !seenUrls.has(l.url)) {
        seenUrls.add(l.url);
        combinedLinks.push({ title: l.title || l.url, url: l.url });
      }
    }
  }

  if (place.source && typeof place.source === 'string' && !seenUrls.has(place.source)) {
    seenUrls.add(place.source);
    let srcTitle = dict.formSourceUrl || 'Першакрыніца';
    if (place.source.includes('nashaniva.com')) {
      srcTitle = 'Наша Ніва: Чытаць матэрыял';
    } else if (place.source.includes('chagall.com')) {
      srcTitle = 'Marc Chagall: Афіцыйны каталог';
    } else if (place.source.includes('charter97.org')) {
      srcTitle = 'Хартыя\'97: Чытаць матэрыял';
    } else if (place.source.includes('racyja.com')) {
      srcTitle = 'Радыё Рацыя: Чытаць матэрыял';
    } else {
      try {
        const u = new URL(place.source);
        srcTitle = `Першакрыніца (${u.hostname.replace(/^www\./, '')})`;
      } catch (e) {
        srcTitle = 'Першакрыніца';
      }
    }
    combinedLinks.push({ title: srcTitle, url: place.source });
  }

  if (place.wiki && typeof place.wiki === 'string' && !seenUrls.has(place.wiki)) {
    seenUrls.add(place.wiki);
    combinedLinks.push({ title: 'Вікіпедыя: Артыкул', url: place.wiki });
  }

  const linksHtml = combinedLinks.map(l => {
    return `
      <a href="${l.url}" target="_blank" rel="noopener noreferrer" class="detail-link-item">
        <span class="link-text">${l.title}</span>
        <span class="link-arrow">&rarr;</span>
      </a>
    `;
  }).join('');

  // Draggable marker in admin mode
  if (isAdminMode) {
    const marker = markersMap.get(placeId);
    if (marker && marker.dragging) {
      if (activeDraggableMarker && activeDraggableMarker !== marker) {
        activeDraggableMarker.dragging.disable();
        const prevPin = activeDraggableMarker.getElement()?.querySelector('.custom-pin');
        if (prevPin) prevPin.classList.remove('is-draggable');
      }
      marker.dragging.enable();
      activeDraggableMarker = marker;
      const pinEl = marker.getElement()?.querySelector('.custom-pin');
      if (pinEl) pinEl.classList.add('is-draggable');

      marker.off('dragend');
      marker.on('dragend', (ev) => {
        const newPos = ev.target.getLatLng();
        const newLat = parseFloat(newPos.lat.toFixed(5));
        const newLng = parseFloat(newPos.lng.toFixed(5));
        place.coordinates = [newLat, newLng];
        savePlaceOverride(place.id, { coordinates: place.coordinates });

        const latInp = document.getElementById('adminInputLat');
        const lngInp = document.getElementById('adminInputLng');
        if (latInp) latInp.value = newLat;
        if (lngInp) lngInp.value = newLng;

        const locCoordEl = document.getElementById('detailCoordsCode');
        if (locCoordEl) locCoordEl.textContent = `${newLat.toFixed(4)}, ${newLng.toFixed(4)}`;

        const d = window.i18n[currentLang] || window.i18n.by;
        showToast(`${d.coordsSelected || 'Каардынаты:'} ${newLat}, ${newLng}`);
      });
    }
  }

  // Unverified banner
  const unverifiedBannerHtml = place.unverifiedCoordinates ? `
    <div class="unverified-coords-banner">
      <div style="display: flex; align-items: flex-start; justify-content: space-between; gap: 0.75rem;">
        <div>
          <div style="font-weight: 700; color: var(--text-main); margin-bottom: 2px; text-transform: uppercase; font-size: 0.72rem; letter-spacing: 0.04em; display: flex; align-items: center; gap: 4px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            ${dict.unverifiedCoordsBadge || 'Неправераныя каардынаты'}
          </div>
          <div style="font-size: 0.78rem; color: #52525b; line-height: 1.4;">
            ${dict.unverifiedCoordsNotice || 'Каардынаты гэтага пункта дададзены аўтаматычна з гістарычных крыніц і патрабуюць верыфікацыі.'}
          </div>
        </div>
        <button type="button" class="btn btn-primary btn-sm" onclick="startPlaceCoordinateCorrection('${place.id}')" style="white-space: nowrap; align-self: center; font-size: 0.75rem; padding: 0.35rem 0.65rem; display: inline-flex; align-items: center; gap: 0.3rem;">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
          <span>${dict.btnPickOnMap || 'Указаць на карце'}</span>
        </button>
      </div>
    </div>
  ` : '';

  // Admin moderation panel
  let adminPanelHtml = '';
  if (isAdminMode) {
    adminPanelHtml = `
      <div class="admin-detail-panel">
        <div class="admin-detail-panel-title">
          <span>${dict.adminPanelTitle || 'Мадэрацыя каардынат'}</span>
          ${place.unverifiedCoordinates ? `<span class="unverified-coords-badge">Патрабуе праверкі</span>` : `<span style="font-size:0.7rem; color:#16a34a; font-weight:700; text-transform:uppercase;">Верыфікавана</span>`}
        </div>
        <div class="admin-coords-grid">
          <div class="admin-coords-input-group">
            <label>Шырата (Lat):</label>
            <input type="number" step="0.00001" id="adminInputLat" class="admin-coords-input" value="${lat.toFixed(5)}" onchange="onAdminCoordInputChange('${place.id}')">
          </div>
          <div class="admin-coords-input-group">
            <label>Даўгата (Lng):</label>
            <input type="number" step="0.00001" id="adminInputLng" class="admin-coords-input" value="${lng.toFixed(5)}" onchange="onAdminCoordInputChange('${place.id}')">
          </div>
        </div>
        <div class="admin-detail-panel-hint">
          ${dict.adminDragMarkerHint || 'У рэжыме адміна можна перацягваць маркер на карце мышкай альбо выставіць кропку клікам.'}
        </div>
        <div class="admin-detail-actions">
          <button type="button" class="btn btn-secondary btn-sm" onclick="startAdminPickMode('${place.id}')">
            ${dict.adminPickOnMapBtn || 'Клікам на карце'}
          </button>
          ${place.unverifiedCoordinates ? `
            <button type="button" class="btn btn-primary btn-sm" onclick="confirmPlaceCoordinates('${place.id}')">
              ${dict.adminConfirmCoordsBtn || 'Пацвердзіць каардынаты'}
            </button>
          ` : `
            <button type="button" class="btn btn-secondary btn-sm" onclick="savePlaceCoordinates('${place.id}')">
              ${dict.adminSaveCoordsBtn || 'Захаваць каардынаты'}
            </button>
          `}
        </div>
      </div>
    `;
  }

  drawer.innerHTML = `
    <div class="detail-header-actions">
      <button class="btn btn-secondary btn-sm" onclick="closePlaceDetail()">
        &larr; ${dict.sidebarTitle}
      </button>
      <button class="btn btn-secondary btn-sm" onclick="copyCurrentShareLink()">
        ${dict.btnCopyLink}
      </button>
    </div>
    ${unverifiedBannerHtml}
    ${adminPanelHtml}
    ${heroImg}
    <div class="detail-body">
      <span class="place-card-category">
        ${categoryName}
      </span>
      ${place.isUserCreated ? '<span class="badge-user-created" style="display:inline-block; font-size:0.7rem; font-weight:700; background:#ecfdf5; color:#059669; border:1px solid #a7f3d0; padding:2px 8px; border-radius:4px; margin-left:6px;">👤 Створана вамі</span>' : ''}
      <h2 class="detail-title">${formatPlaceTitle(title, city)}</h2>
      <div class="detail-location">
        <strong>${city}, ${country}</strong> &bull; <code id="detailCoordsCode">${lat.toFixed(4)}, ${lng.toFixed(4)}</code>
        ${!place.unverifiedCoordinates ? `
        <button type="button" class="btn-text-action" onclick="startPlaceCoordinateCorrection('${place.id}')" title="${dict.btnRefineCoords || 'Удакладніць'}" style="background:none; border:1px solid var(--border-color); border-radius:4px; padding:2px 6px; font-size:0.72rem; cursor:pointer; color:var(--text-muted); margin-left:6px; display:inline-flex; align-items:center; gap:3px;">
          📍 ${dict.btnRefineCoords || 'Удакладніць'}
        </button>
        ` : ''}
      </div>
      <div class="detail-description">
        ${desc}
      </div>

      ${associatedPersonsHtml}

      ${nestedItemsHtml}

      ${tagsHtml ? `<div><strong style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.04em;">${dict.tagsHeading}:</strong><div class="detail-tags" style="margin-top:0.35rem">${tagsHtml}</div></div>` : ''}
      
      <div class="detail-actions-row">
        <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lng}" 
           target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
          ${dict.btnOpenGoogleMaps}
        </a>
        <a href="https://www.openstreetmap.org/?mlat=${lat}&mlon=${lng}#map=16/${lat}/${lng}" 
           target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
          ${dict.btnOpenOSM}
        </a>
        ${place.isUserCreated ? `
        <button type="button" class="btn btn-secondary btn-sm" onclick="window.deleteUserPlace('${place.id}')" style="color:#dc2626; border-color:#fca5a5;" title="Выдаліць з лакальнай карты">
          🗑️ Выдаліць
        </button>
        ` : ''}
      </div>

      ${linksHtml ? `
        <div style="margin-top: 0.5rem;">
          <strong style="font-size: 0.75rem; text-transform: uppercase; letter-spacing:0.04em; color: var(--text-muted);">${dict.sourcesHeading}:</strong>
          <div class="detail-links-list">
            ${linksHtml}
          </div>
        </div>
      ` : ''}
    </div>
  `;

  drawer.classList.add('open');
  drawer.scrollTop = 0;
}

function closePlaceDetail() {
  if (activeDraggableMarker) {
    activeDraggableMarker.dragging?.disable();
    const pinEl = activeDraggableMarker.getElement()?.querySelector('.custom-pin');
    if (pinEl) pinEl.classList.remove('is-draggable');
    activeDraggableMarker = null;
  }

  const drawer = document.getElementById('placeDetailDrawer');
  if (drawer) {
    drawer.classList.remove('open');
  }
  selectedPlaceId = null;
  history.replaceState(null, '', window.location.pathname);
}

// Copy share link
function copyCurrentShareLink() {
  const url = window.location.href;
  navigator.clipboard.writeText(url).then(() => {
    showToast(window.i18n[currentLang].linkCopied);
  });
}

// Resolve associated person from nested item metadata
function resolvePersonForSubItem(it) {
  if (!it) return null;
  if (it.personId) {
    const p = allPersons.find(p => p.id === it.personId);
    if (p) return p;
  }
  const rawStr = (it.person || it.author || '').toLowerCase();
  if (!rawStr) return null;
  const cleanStr = rawStr.replace(/\(.*?\)/g, '').trim();
  if (!cleanStr) return null;
  return allPersons.find(p => {
    const pBy = (p.name?.by || '').toLowerCase();
    const pRu = (p.name?.ru || '').toLowerCase();
    const pEn = (p.name?.en || '').toLowerCase();
    return cleanStr.includes(pBy) || pBy.includes(cleanStr) ||
           cleanStr.includes(pRu) || pRu.includes(cleanStr) ||
           cleanStr.includes(pEn) || pEn.includes(cleanStr);
  });
}

// Handle clicking person button from within a sub-item card
function handlePersonClickFromItem(personId, rawEncodedName) {
  if (personId && allPersons.some(p => p.id === personId)) {
    closeModal('nestedItemModal');
    openPersonDetail(personId);
    return;
  }
  const rawName = decodeURIComponent(rawEncodedName || '');
  const p = resolvePersonForSubItem({ author: rawName, person: rawName });
  if (p) {
    closeModal('nestedItemModal');
    openPersonDetail(p.id);
    return;
  }
  closeModal('nestedItemModal');
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    const cleanName = rawName.replace(/\(.*?\)/g, '').trim();
    searchInput.value = cleanName;
    searchInput.dispatchEvent(new Event('input'));
  }
}

// Open modal showing comprehensive details of a nested item
function openNestedItemModal(placeId, itemIdx) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place || !place.items || !place.items[itemIdx]) return;
  const it = place.items[itemIdx];
  const dict = window.i18n[currentLang] || window.i18n.by;
  const itPerson = resolvePersonForSubItem(it);
  const personDisplayName = it.person || it.author || (itPerson ? getLocalized(itPerson.name) : '');

  const titleEl = document.getElementById('nestedItemModalTitle');
  if (titleEl) titleEl.textContent = it.title;

  const subEl = document.getElementById('nestedItemModalSubtitle');
  if (subEl) subEl.textContent = `${getLocalized(place.title)} (${getLocalized(place.city)}, ${getLocalized(place.country)})`;

  const bodyEl = document.getElementById('nestedItemModalBody');
  if (bodyEl) {
    bodyEl.innerHTML = `
      <div class="nested-detail-container">
        ${it.image ? `
          <div class="nested-detail-image-box">
            <img src="${getWikimediaThumb(it.image, 960)}" alt="${it.title}" class="nested-detail-image" loading="lazy" referrerpolicy="no-referrer">
          </div>
        ` : ''}
        <div class="nested-detail-content">
          <h3 class="nested-detail-item-title">${it.title}</h3>
          <div class="nested-detail-meta-row">
            ${personDisplayName ? `
              <button type="button" class="nested-item-person-btn-lg" onclick="handlePersonClickFromItem('${itPerson ? itPerson.id : ''}', '${encodeURIComponent(personDisplayName)}')">
                <span class="person-icon-dot" style="width:8px;height:8px;border-radius:50%;background:#2563eb;display:inline-block;"></span>
                <span>${personDisplayName}</span> &rarr;
              </button>
            ` : ''}
            ${it.year ? `<span class="nested-detail-year-badge">${it.year}</span>` : ''}
          </div>
          ${it.description ? `
            <div class="nested-detail-description">
              ${it.description}
            </div>
          ` : ''}
          ${(it.needsCoords || it.coordsRequest) ? `
            <div class="coords-request-callout">
              <div style="font-weight:700; color:#c2410c; display:flex; align-items:center; gap:0.4rem; font-size:0.85rem;">
                <span>🔍</span>
                <span>${dict.coordsRequestBadge || 'Запыт каардынат ад супольнасці'}</span>
              </div>
              <p>${dict.coordsRequestPrompt || 'Дакладны адрас або каардынаты гэтага аб’екта пакуль не лакалізаваны на карце. Калі вы маеце архіўныя звесткі — паведаміце нам!'}</p>
              <button type="button" class="btn btn-primary btn-sm" onclick="suggestCoordsForSubItem('${place.id}', ${itemIdx})">
                ${dict.suggestCoordsBtn || 'Паведаміць адрас / каардынаты'} &rarr;
              </button>
            </div>
          ` : ''}
          <div class="nested-detail-parent-place">
            <div class="nested-parent-label">${dict.locatedInPlace || 'Знаходзіцца ў комплексе / аб’екце:'}</div>
            <div class="nested-parent-name" onclick="closeModal('nestedItemModal'); selectPlace('${place.id}')">
              <strong>${getLocalized(place.title)}</strong> &bull; ${getLocalized(place.city)}, ${getLocalized(place.country)} &rarr;
            </div>
          </div>
        </div>
      </div>
    `;
  }
  openModal('nestedItemModal');
}

// Prefill addPlaceModal for sub-item community coords submission
function suggestCoordsForSubItem(placeId, itemIdx) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place || !place.items || !place.items[itemIdx]) return;
  const it = place.items[itemIdx];
  closeModal('nestedItemModal');
  openAddPlaceModal();
  setTimeout(() => {
    const titleInp = document.getElementById('addTitle');
    const cityInp = document.getElementById('addCity');
    const countryInp = document.getElementById('addCountry');
    const descInp = document.getElementById('addDescription');
    if (titleInp) titleInp.value = it.title || '';
    if (cityInp) cityInp.value = getLocalized(place.city) || '';
    if (countryInp) countryInp.value = getLocalized(place.country) || '';
    if (descInp) descInp.value = `[Удакладненне каардынат для: ${getLocalized(place.title)}] ${it.description || ''}`;
  }, 100);
}
window.suggestCoordsForSubItem = suggestCoordsForSubItem;

// Check url hash on load
function checkUrlHash() {
  const hash = window.location.hash;
  if (hash.startsWith('#place=')) {
    const id = hash.replace('#place=', '');
    if (allPlaces.some(p => p.id === id)) {
      setTimeout(() => selectPlace(id, false), 300);
    }
  } else if (hash.startsWith('#person=')) {
    const id = hash.replace('#person=', '');
    if (allPersons.some(p => p.id === id)) {
      setTimeout(() => openPersonDetail(id, false), 300);
    }
  }
}

// Toast notification helper
function showToast(msg) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.style.display = 'block';
  setTimeout(() => {
    toast.style.display = 'none';
  }, 3000);
}

// Setup Event Listeners
function setupEventListeners() {
  // Search input
  const searchInput = document.getElementById('searchInput');
  const searchClear = document.getElementById('searchClear');

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const raw = e.target.value;
      if (raw.startsWith('#')) {
        searchQuery = raw.slice(1).trim();
      } else {
        searchQuery = raw.trim();
      }
      if (searchClear) {
        searchClear.style.display = raw ? 'block' : 'none';
      }
      filterAndRender();
    });
  }

    if (searchClear) {
      searchClear.addEventListener('click', () => {
        if (searchInput) {
          searchInput.value = '';
          searchQuery = '';
          searchClear.style.display = 'none';
          filterAndRender();
        }
      });
    }


  // Language buttons
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      setLanguage(btn.getAttribute('data-lang'));
    });
  });

  // Modal openers
  document.getElementById('btnAbout')?.addEventListener('click', () => openModal('aboutModal'));
  document.getElementById('btnAddPlace')?.addEventListener('click', () => openModal('addPlaceModal'));

  // Mobile sidebar toggle
  const mobileToggle = document.getElementById('mobileSidebarToggle');
  const sidebar = document.getElementById('sidebar');
  if (mobileToggle && sidebar) {
    mobileToggle.addEventListener('click', () => {
      sidebar.classList.toggle('mobile-open');
    });
  }

  // Pick coords on map button in Add modal (both header and inline buttons)
  const handleStartPickForAddModal = () => {
    closeModal('addPlaceModal');
    pickCoordsMode = true;
    targetPlaceForCoordsCorrection = null;
    cleanUpPickMarker();
    const banner = document.getElementById('pickCoordsBanner');
    const bannerText = document.getElementById('pickCoordsBannerText');
    const btnConfirm = document.getElementById('btnConfirmPick');
    if (bannerText) {
      bannerText.textContent = window.i18n[currentLang]?.clickMapToPick || 'Клікніце ў пункт на карце для выбару каардынат';
    }
    if (btnConfirm) btnConfirm.style.display = 'none';
    if (banner) banner.style.display = 'flex';
    showToast(window.i18n[currentLang]?.clickMapToPick || 'Клікніце ў пункт на карце для выбару каардынат');
  };

  document.getElementById('btnPickOnMap')?.addEventListener('click', handleStartPickForAddModal);
  document.getElementById('btnPickOnMapInline')?.addEventListener('click', handleStartPickForAddModal);

  // Confirm and Cancel pick mode banner
  document.getElementById('btnConfirmPick')?.addEventListener('click', () => confirmPickedCoordinates());
  document.getElementById('btnCancelPick')?.addEventListener('click', cancelPickedCoordinates);

  // Direct save to map button in Add modal
  document.getElementById('btnSavePlaceDirect')?.addEventListener('click', handleSavePlaceDirect);

  // Smart coordinates paste input
  const smartCoordsInput = document.getElementById('formCoordsSmart');
  if (smartCoordsInput) {
    smartCoordsInput.addEventListener('input', (e) => {
      const parsed = parseCoordinatesInput(e.target.value);
      if (parsed) {
        const [lat, lng] = parsed;
        const latInput = document.getElementById('formLat');
        const lngInput = document.getElementById('formLng');
        if (latInput && lngInput) {
          latInput.value = lat.toFixed(5);
          lngInput.value = lng.toFixed(5);
          showToast(`${window.i18n[currentLang]?.coordsSelected || 'Выбраныя каардынаты:'} ${lat.toFixed(5)}, ${lng.toFixed(5)}`);
        }
      }
    });
  }

  // Generate JSON button in Add modal
  document.getElementById('btnGenerateJson')?.addEventListener('click', handleGenerateJson);
  document.getElementById('btnCopyJson')?.addEventListener('click', handleCopyJson);

  // Persons modal opener & search
  document.getElementById('btnPersons')?.addEventListener('click', openAllPersonsModal);

  const personsSearchInput = document.getElementById('personsSearchInput');
  if (personsSearchInput) {
    personsSearchInput.addEventListener('input', (e) => {
      personsSearchQuery = e.target.value;
      renderPersonsGrid();
    });
  }

  // Admin keyboard shortcut (Ctrl+Shift+A / Cmd+Shift+A)
  window.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key.toLowerCase() === 'a') {
      e.preventDefault();
      toggleAdminMode();
    }
  });

  // Admin bar buttons
  document.getElementById('btnAdminToggleFilter')?.addEventListener('click', toggleAdminFilterUnverified);
  document.getElementById('btnAdminQueue')?.addEventListener('click', openAdminQueueModal);
  document.getElementById('btnAdminExport')?.addEventListener('click', openAdminExportModal);
  document.getElementById('btnAdminExit')?.addEventListener('click', () => toggleAdminMode(false));

  // Admin export modal buttons
  document.getElementById('btnAdminDownloadJson')?.addEventListener('click', handleAdminDownloadJson);
  document.getElementById('btnAdminCopyFullJson')?.addEventListener('click', handleAdminCopyJson);
}

// Global handler to filter dataset by tag
function filterByTag(tag) {
  if (!tag) return;
  const cleanTag = String(tag).replace(/^#/, '').trim();
  const searchInput = document.getElementById('searchInput');
  const searchClear = document.getElementById('searchClear');
  if (searchInput) {
    searchInput.value = '#' + cleanTag;
  }
  if (searchClear) {
    searchClear.style.display = 'block';
  }
  searchQuery = cleanTag;

  // Reset category filter so tag search matches across all categories
  activeCategory = 'all';
  renderCategoryPills();

  // Close detail view so user sees the filtered list and map markers
  if (typeof closePlaceDetail === 'function') {
    closePlaceDetail();
  }

  filterAndRender();
}
window.filterByTag = filterByTag;


// Modals management
function openModal(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.add('open');
  }
}

function closeModal(id) {
  const modal = document.getElementById(id);
  if (modal) {
    modal.classList.remove('open');
  }
}

// JSON generation from user form
function handleGenerateJson() {
  const nameBy = document.getElementById('formNameBy')?.value.trim();
  const nameRu = document.getElementById('formNameRu')?.value.trim();
  const nameEn = document.getElementById('formNameEn')?.value.trim();
  const category = document.getElementById('formCategory')?.value;
  const country = document.getElementById('formCountry')?.value.trim();
  const city = document.getElementById('formCity')?.value.trim();
  const lat = parseFloat(document.getElementById('formLat')?.value);
  const lng = parseFloat(document.getElementById('formLng')?.value);
  const descBy = document.getElementById('formDescBy')?.value.trim();
  const descRu = document.getElementById('formDescRu')?.value.trim();
  const descEn = document.getElementById('formDescEn')?.value.trim();
  const image = document.getElementById('formImage')?.value.trim();
  const tagsStr = document.getElementById('formTags')?.value.trim();
  const wikiUrl = document.getElementById('formWikiUrl')?.value.trim();
  const articleUrl = document.getElementById('formArticleUrl')?.value.trim();

  if (!nameBy || isNaN(lat) || isNaN(lng)) {
    alert('Калі ласка, увядзіце назву і каардынаты (шырату і даўгату)!');
    return;
  }

  // Generate safe ID
  const slug = nameEn ? nameEn.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-') : 'place-' + Date.now();

  const links = [];
  if (wikiUrl) {
    links.push({ title: "Вікіпедыя пра аб’ект", url: wikiUrl });
  }
  if (articleUrl) {
    links.push({ title: "Артыкул: Беларускі бэкграўнд", url: articleUrl });
  }

  const newPlaceObj = {
    id: slug,
    title: {
      by: nameBy,
      ru: nameRu || nameBy,
      en: nameEn || nameBy
    },
    category: category || 'historical',
    country: {
      by: country || '',
      ru: country || '',
      en: country || ''
    },
    city: {
      by: city || '',
      ru: city || '',
      en: city || ''
    },
    coordinates: [lat, lng],
    description: {
      by: descBy,
      ru: descRu || descBy,
      en: descEn || descBy
    },
    image: image || '',
    links: links,
    tags: tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(Boolean) : []
  };

  const jsonStr = JSON.stringify(newPlaceObj, null, 2);
  const outputBox = document.getElementById('jsonOutputBox');
  const resultContainer = document.getElementById('jsonResultContainer');

  if (outputBox && resultContainer) {
    outputBox.textContent = jsonStr;
    resultContainer.style.display = 'block';
  }

  // Record user contribution
  if (typeof recordUserContribution === 'function') {
    recordUserContribution({
      type: 'place',
      placeId: slug,
      title: newPlaceObj.title,
      image: newPlaceObj.image,
      date: Date.now()
    });
  }
}

function handleCopyJson() {
  const outputBox = document.getElementById('jsonOutputBox');
  if (outputBox && outputBox.textContent) {
    navigator.clipboard.writeText(outputBox.textContent).then(() => {
      showToast(window.i18n[currentLang].jsonCopied);
    });
  }
}

// ========================================================
// Persons Feature Implementation
// ========================================================

// Open All Persons Modal
function openAllPersonsModal() {
  personsSearchQuery = '';
  const searchInput = document.getElementById('personsSearchInput');
  if (searchInput) searchInput.value = '';
  renderPersonsGrid();
  openModal('allPersonsModal');
}

// Render grid in All Persons Modal
function renderPersonsGrid() {
  const container = document.getElementById('personsGridContainer');
  if (!container) return;

  const dict = window.i18n[currentLang] || window.i18n.by;
  let filtered = allPersons;

  if (personsSearchQuery.trim() !== '') {
    const q = personsSearchQuery.toLowerCase().trim();
    filtered = allPersons.filter(p => {
      const nameBy = (p.name?.by || '').toLowerCase();
      const nameRu = (p.name?.ru || '').toLowerCase();
      const nameEn = (p.name?.en || '').toLowerCase();
      const role = getLocalized(p.role).toLowerCase();
      const bio = getLocalized(p.bio).toLowerCase();
      return nameBy.includes(q) || nameRu.includes(q) || nameEn.includes(q) || role.includes(q) || bio.includes(q);
    });
  }

  if (filtered.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 2.5rem 1rem; text-align: center; color: var(--text-muted); font-size: 0.9rem;">
        ${dict.noPersonsFound || 'Асоб не знойдзена'}
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(p => {
    const name = getLocalized(p.name);
    const role = getLocalized(p.role);
    const places = getPlacesForPerson(p);
    const countLabel = `${places.length} ${dict.personPlacesCount || 'месцаў'}`;
    const avatar = getWikimediaThumb(p.image, 250) || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';

    return `
      <div class="person-card" onclick="openPersonDetail('${p.id}')">
        <img src="${avatar}" alt="${name}" class="person-avatar" loading="lazy" referrerpolicy="no-referrer" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'">
        <div class="person-card-name">${name}</div>
        <div class="person-card-dates">${p.dates || ''}</div>
        <div class="person-card-role">${role}</div>
        <span class="person-card-places-count">${countLabel}</span>
      </div>
    `;
  }).join('');
}

// Open Person Detail Modal
function openPersonDetail(personId, updateHash = true) {
  const person = allPersons.find(p => p.id === personId);
  if (!person) return;

  selectedPersonId = personId;
  const dict = window.i18n[currentLang] || window.i18n.by;
  const name = getLocalized(person.name);
  const role = getLocalized(person.role);
  const bio = getLocalized(person.bio);
  const avatar = getWikimediaThumb(person.image, 500) || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';
  const places = getPlacesForPerson(person);

  const titleEl = document.getElementById('personModalTitle');
  if (titleEl) {
    titleEl.textContent = name;
  }

  const bodyEl = document.getElementById('personModalBody');
  if (bodyEl) {
    const placesHtml = places.length > 0 ? places.map(pl => {
      const plTitle = getLocalized(pl.title);
      const plCity = getLocalized(pl.city);
      const plCountry = getLocalized(pl.country);
      const plThumb = getWikimediaThumb(pl.image, 250) || '';
      const catConfig = CATEGORY_CONFIG[pl.category] || CATEGORY_CONFIG.historical || {};
      const catIcon = catConfig.icon || '📍';
      const catColor = catConfig.color || '#2563eb';

      return `
        <div class="person-place-item" onclick="viewPersonPlaceOnMap('${pl.id}')">
          <div class="person-place-thumb-container" style="position:relative; width:48px; height:48px; flex-shrink:0; border-radius:6px; overflow:hidden; background:var(--bg-secondary);">
            ${plThumb ? `<img src="${plThumb}" alt="${escapeHtml(plTitle)}" class="person-place-thumb" loading="lazy" referrerpolicy="no-referrer"
                 onerror="this.style.display='none'; if(this.nextElementSibling) this.nextElementSibling.style.display='flex';"
                 style="width:100%; height:100%; object-fit:cover;">` : ''}
            <div class="person-place-thumb-fallback" style="${plThumb ? 'display:none;' : 'display:flex;'} width:100%; height:100%; align-items:center; justify-content:center; background:${catColor}15; color:${catColor}; border:1px solid var(--border-color);">
              <span class="category-pill-icon" style="background-color:${catColor}; width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#ffffff;">${catIcon}</span>
            </div>
          </div>
          <div class="person-place-info">
            <div class="person-place-title">${formatPlaceTitle(plTitle, plCity)}</div>
            <div class="person-place-meta">${plCity}, ${plCountry}</div>
          </div>
          <span class="person-place-btn">${dict.showOnMap || 'На карце &rarr;'}</span>
        </div>
      `;
    }).join('') : `
      <div style="padding: 1rem; color: var(--text-muted); font-size: 0.85rem;">
        ${dict.noResults || 'Мясцін пакуль не знойдзена'}
      </div>
    `;

    // Related persons / clan members
    let relatedPersons = [];
    if (Array.isArray(person.relatedPersonIds) && person.relatedPersonIds.length > 0) {
      relatedPersons = person.relatedPersonIds.map(id => allPersons.find(p => p.id === id)).filter(Boolean);
    } else if (person.id === 'radziwills') {
      relatedPersons = allPersons.filter(p => p.id !== 'radziwills' && p.id.includes('radziwill'));
    }

    let relatedPersonsHtml = '';
    if (relatedPersons.length > 0) {
      const relatedCards = relatedPersons.map(rp => {
        const rpName = getLocalized(rp.name);
        const rpRole = getLocalized(rp.role);
        const rpAvatar = getWikimediaThumb(rp.image, 250) || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';
        return `
          <div class="person-related-item" onclick="openPersonDetail('${rp.id}')" title="${rpRole}">
            <img src="${rpAvatar}" alt="${rpName}" class="person-related-thumb" loading="lazy" referrerpolicy="no-referrer" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'">
            <div class="person-related-info">
              <div class="person-related-name">${rpName}</div>
              <div class="person-related-role">${rpRole}</div>
            </div>
            <span class="person-related-arrow">&rarr;</span>
          </div>
        `;
      }).join('');

      relatedPersonsHtml = `
        <div class="person-related-box">
          <div class="person-places-title">
            ${dict.relatedPersonsTitle || 'Прадстаўнікі роду і звязаныя асобы'} (${relatedPersons.length})
          </div>
          <div class="person-related-list">
            ${relatedCards}
          </div>
        </div>
      `;
    }

    bodyEl.innerHTML = `
      <div class="person-detail-header">
        <img src="${avatar}" alt="${name}" class="person-detail-avatar" loading="lazy" referrerpolicy="no-referrer" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'">
        <div class="person-detail-info">
          <div class="person-detail-name">${name}</div>
          <div class="person-detail-meta">
            ${person.dates ? `<span class="person-detail-dates">${person.dates}</span>` : ''}
            <span class="person-detail-role">${role}</span>
          </div>
          ${person.wiki ? `
            <div class="person-detail-actions">
              <a href="${person.wiki}" target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm" style="font-size:0.75rem;">
                ${dict.personWikiLink || 'Вікіпедыя'} &rarr;
              </a>
            </div>
          ` : ''}
        </div>
      </div>

      <div class="person-bio-box">
        ${bio}
      </div>

      ${relatedPersonsHtml}

      <div class="person-places-title">
        ${dict.personConnectedPlaces || 'Звязаныя мясціны на карце'} (${places.length})
      </div>
      <div class="person-places-list">
        ${placesHtml}
      </div>
    `;
  }

  closeModal('allPersonsModal');
  openModal('personModal');

  if (updateHash) {
    window.location.hash = `person=${personId}`;
  }
}

// Navigate from person modal to place on map
function viewPersonPlaceOnMap(placeId) {
  closeModal('personModal');
  closeModal('allPersonsModal');
  selectPlace(placeId);
}

// ==========================================
// Admin Mode & Moderation Functions
// ==========================================

function updateAdminUI() {
  const adminBar = document.getElementById('adminBar');
  if (!adminBar) return;

  if (isAdminMode) {
    adminBar.style.display = 'flex';
    document.body.classList.add('admin-mode-active');
  } else {
    adminBar.style.display = 'none';
    document.body.classList.remove('admin-mode-active');
  }

  const unverifiedCount = allPlaces.filter(p => p.unverifiedCoordinates === true).length;
  const countEl = document.getElementById('adminBarCount');
  if (countEl) {
    countEl.textContent = unverifiedCount;
  }

  const filterBtn = document.getElementById('btnAdminToggleFilter');
  const filterLabel = document.getElementById('adminFilterLabel');
  const dict = window.i18n[currentLang] || window.i18n.by;
  if (filterBtn && filterLabel) {
    if (filterOnlyUnverified) {
      filterBtn.classList.remove('btn-warning');
      filterBtn.classList.add('btn-primary');
      filterLabel.textContent = dict.adminShowAll || 'Усе месцы';
    } else {
      filterBtn.classList.remove('btn-primary');
      filterBtn.classList.add('btn-warning');
      filterLabel.textContent = dict.adminFilterUnverified || '⚠️ Толькі неправераныя';
    }
  }
}

function toggleAdminMode(forceState) {
  if (typeof forceState === 'boolean') {
    isAdminMode = forceState;
  } else {
    isAdminMode = !isAdminMode;
  }

  localStorage.setItem('albaruthenica_admin_mode', isAdminMode ? 'true' : 'false');
  updateAdminUI();

  if (!isAdminMode) {
    filterOnlyUnverified = false;
    adminPickMode = false;
    if (activeDraggableMarker) {
      activeDraggableMarker.dragging?.disable();
      const pinEl = activeDraggableMarker.getElement()?.querySelector('.custom-pin');
      if (pinEl) pinEl.classList.remove('is-draggable');
      activeDraggableMarker = null;
    }
  }

  filterAndRender();

  if (selectedPlaceId) {
    showPlaceDetail(selectedPlaceId);
  }

  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(isAdminMode ? (dict.adminModeTitle || 'Рэжым мадэрацыі актываваны') : (dict.adminExitBtn || 'Выхад з рэжыму мадэрацыі'));
}

function toggleAdminFilterUnverified() {
  filterOnlyUnverified = !filterOnlyUnverified;
  updateAdminUI();
  filterAndRender();
}

function startAdminPickMode(placeId) {
  adminPickMode = true;
  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(dict.clickMapToPick || 'Клікніце ў пункт на карце для выбару каардынат');
}

function handleAdminMapClick(latlng) {
  if (!selectedPlaceId) return;
  const place = allPlaces.find(p => p.id === selectedPlaceId);
  if (!place) return;

  const newLat = parseFloat(latlng.lat.toFixed(5));
  const newLng = parseFloat(latlng.lng.toFixed(5));
  place.coordinates = [newLat, newLng];

  const marker = markersMap.get(selectedPlaceId);
  if (marker) {
    marker.setLatLng([newLat, newLng]);
  }

  const latInp = document.getElementById('adminInputLat');
  const lngInp = document.getElementById('adminInputLng');
  if (latInp) latInp.value = newLat;
  if (lngInp) lngInp.value = newLng;

  const locCoordEl = document.getElementById('detailCoordsCode');
  if (locCoordEl) locCoordEl.textContent = `${newLat.toFixed(4)}, ${newLng.toFixed(4)}`;

  savePlaceOverride(place.id, {
    coordinates: place.coordinates
  });

  adminPickMode = false;
  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(`${dict.coordsSelected || 'Выбраныя каардынаты:'} ${newLat}, ${newLng}`);
}

function onAdminCoordInputChange(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;
  const latInp = document.getElementById('adminInputLat');
  const lngInp = document.getElementById('adminInputLng');
  if (latInp && lngInp) {
    const lat = parseFloat(latInp.value);
    const lng = parseFloat(lngInp.value);
    if (!isNaN(lat) && !isNaN(lng)) {
      place.coordinates = [lat, lng];
      const marker = markersMap.get(placeId);
      if (marker) {
        marker.setLatLng([lat, lng]);
      }
      const locCoordEl = document.getElementById('detailCoordsCode');
      if (locCoordEl) locCoordEl.textContent = `${lat.toFixed(4)}, ${lng.toFixed(4)}`;
      savePlaceOverride(placeId, { coordinates: [lat, lng] });
    }
  }
}

function confirmPlaceCoordinates(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  const latInp = document.getElementById('adminInputLat');
  const lngInp = document.getElementById('adminInputLng');
  if (latInp && lngInp) {
    const lat = parseFloat(latInp.value);
    const lng = parseFloat(lngInp.value);
    if (!isNaN(lat) && !isNaN(lng)) {
      place.coordinates = [lat, lng];
    }
  }

  place.unverifiedCoordinates = false;
  savePlaceOverride(place.id, {
    coordinates: place.coordinates,
    unverifiedCoordinates: false
  });

  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(dict.adminCoordsUpdated || 'Каардынаты паспяхова захаваны і пацверджаны!');

  renderMarkers();
  renderSidebarList();
  updateStats();
  updateAdminUI();
  showPlaceDetail(placeId);

  if (document.getElementById('adminQueueModal')?.classList.contains('open')) {
    renderAdminQueue();
  }
}

function savePlaceCoordinates(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  const latInp = document.getElementById('adminInputLat');
  const lngInp = document.getElementById('adminInputLng');
  if (latInp && lngInp) {
    const lat = parseFloat(latInp.value);
    const lng = parseFloat(lngInp.value);
    if (!isNaN(lat) && !isNaN(lng)) {
      place.coordinates = [lat, lng];
      const marker = markersMap.get(placeId);
      if (marker) marker.setLatLng([lat, lng]);
    }
  }

  savePlaceOverride(place.id, {
    coordinates: place.coordinates
  });

  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(dict.adminCoordsUpdated || 'Каардынаты паспяхова захаваны!');

  renderMarkers();
  renderSidebarList();
  updateAdminUI();
}

function openAdminQueueModal() {
  renderAdminQueue();
  openModal('adminQueueModal');
}

function renderAdminQueue() {
  const container = document.getElementById('adminQueueListContainer');
  if (!container) return;

  const unverifiedList = allPlaces.filter(p => p.unverifiedCoordinates === true);
  const subtitle = document.getElementById('adminQueueStatsSubtitle');
  if (subtitle) {
    subtitle.textContent = `Засталося неправераных: ${unverifiedList.length} з ${allPlaces.length}`;
  }

  if (unverifiedList.length === 0) {
    container.innerHTML = `
      <div style="padding: 2.5rem 1rem; text-align: center; color: #16a34a; font-weight: 600; font-size: 0.9rem;">
        Усе каардынаты верыфікаваны. Неправераных кропак няма.
      </div>
    `;
    return;
  }

  container.innerHTML = unverifiedList.map(place => {
    const title = getLocalized(place.title);
    const city = getLocalized(place.city);
    const country = getLocalized(place.country);
    const [lat, lng] = place.coordinates;

    return `
      <div class="admin-queue-item" id="queue-item-${place.id}">
        <div class="admin-queue-info">
          <div class="admin-queue-title">${formatPlaceTitle(title)}</div>
          <div class="admin-queue-meta">
            <span>${city}, ${country}</span>
            <span>&bull;</span>
            <code>${lat.toFixed(5)}, ${lng.toFixed(5)}</code>
          </div>
        </div>
        <div class="admin-queue-actions">
          <button class="btn btn-secondary btn-sm" onclick="adminGoToPlace('${place.id}')">
            На карту
          </button>
          <button class="btn btn-primary btn-sm" onclick="confirmPlaceCoordinates('${place.id}')">
            Пацвердзіць
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function adminGoToPlace(placeId) {
  closeModal('adminQueueModal');
  selectPlace(placeId);
}

function openAdminExportModal() {
  const output = document.getElementById('adminExportOutput');
  if (output) {
    output.textContent = JSON.stringify(allPlaces, null, 2);
  }
  openModal('adminExportModal');
}

function handleAdminDownloadJson() {
  const jsonStr = JSON.stringify(allPlaces, null, 2);
  const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'places.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  showToast('Файл places.json спампаваны');
}

function handleAdminCopyJson() {
  const jsonStr = JSON.stringify(allPlaces, null, 2);
  navigator.clipboard.writeText(jsonStr).then(() => {
    showToast('Поўны places.json скапіяваны ў буфер абмену');
  });
}

// Global scope exposures for inline onclick handlers
window.selectPlace = selectPlace;
window.closePlaceDetail = closePlaceDetail;
window.copyCurrentShareLink = copyCurrentShareLink;
window.openModal = openModal;
window.closeModal = closeModal;
window.openAllPersonsModal = openAllPersonsModal;
window.openPersonDetail = openPersonDetail;
window.viewPersonPlaceOnMap = viewPersonPlaceOnMap;
window.openNestedItemModal = openNestedItemModal;
window.handlePersonClickFromItem = handlePersonClickFromItem;

// Admin functions global exposure
window.toggleAdminMode = toggleAdminMode;
window.confirmPlaceCoordinates = confirmPlaceCoordinates;
window.savePlaceCoordinates = savePlaceCoordinates;
window.startAdminPickMode = startAdminPickMode;
window.onAdminCoordInputChange = onAdminCoordInputChange;
window.openAdminQueueModal = openAdminQueueModal;
window.openAdminExportModal = openAdminExportModal;
window.adminGoToPlace = adminGoToPlace;
window.toggleAdminFilterUnverified = toggleAdminFilterUnverified;
window.handleAdminDownloadJson = handleAdminDownloadJson;
window.handleAdminCopyJson = handleAdminCopyJson;

// ========================================================
// Add Image & Fallback Handling
// ========================================================

function handleHeroImageError(placeId) {
  const heroWrap = document.getElementById('detailHeroWrap');
  if (!heroWrap) return;
  const dict = window.i18n[currentLang] || window.i18n.by;
  heroWrap.className = 'detail-no-image-wrap';
  heroWrap.innerHTML = `
    <div class="detail-no-image-content">
      <div class="detail-no-image-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
          <circle cx="8.5" cy="8.5" r="1.5"/>
          <polyline points="21 15 16 10 5 21"/>
        </svg>
      </div>
      <div class="detail-no-image-text">
        <span class="detail-no-image-title">${dict.noImageTitle || 'Выява пакуль адсутнічае'}</span>
        <span class="detail-no-image-sub">${dict.noImagePrompt || 'Маеце фатаграфію ці выяву гэтага месца? Дапамажыце праекту!'}</span>
      </div>
      <button type="button" class="btn btn-primary btn-sm detail-add-photo-btn" onclick="openAddImageModal('${placeId}')">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:4px; vertical-align:-1px;">
          <line x1="12" y1="5" x2="12" y2="19"></line>
          <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
        ${dict.btnAddImage || 'Дадаць выяву'}
      </button>
    </div>
  `;
}

function openAddImageModal(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  const dict = window.i18n[currentLang] || window.i18n.by;
  const title = getLocalized(place.title);
  const city = getLocalized(place.city);
  const country = getLocalized(place.country);

  const placeIdInput = document.getElementById('addImagePlaceId');
  if (placeIdInput) placeIdInput.value = placeId;

  const subEl = document.getElementById('addImageModalSubtitle');
  if (subEl) {
    subEl.textContent = `${title} (${city}, ${country})`;
  }

  // Reset inputs
  const urlInp = document.getElementById('addImageUrlInput');
  if (urlInp) urlInp.value = '';

  const authInp = document.getElementById('addImageAuthorInput');
  if (authInp) authInp.value = '';

  const fileInput = document.getElementById('addImageFileInput');
  if (fileInput) fileInput.value = '';

  const previewBox = document.getElementById('addImagePreviewContainer');
  const previewImg = document.getElementById('addImagePreviewImg');
  if (previewBox) previewBox.style.display = 'none';
  if (previewImg) previewImg.src = '';

  switchAddImageTab('url');
  openModal('addImageModal');
}

function switchAddImageTab(tab) {
  const tabUrl = document.getElementById('tabImgUrl');
  const tabFile = document.getElementById('tabImgFile');
  const secUrl = document.getElementById('sectionImgUrl');
  const secFile = document.getElementById('sectionImgFile');

  if (tab === 'url') {
    tabUrl?.classList.add('active');
    tabFile?.classList.remove('active');
    if (secUrl) secUrl.style.display = 'block';
    if (secFile) secFile.style.display = 'none';
  } else {
    tabUrl?.classList.remove('active');
    tabFile?.classList.add('active');
    if (secUrl) secUrl.style.display = 'none';
    if (secFile) secFile.style.display = 'block';
  }
}

function previewAddImageUrl(url) {
  const previewBox = document.getElementById('addImagePreviewContainer');
  const previewImg = document.getElementById('addImagePreviewImg');
  if (!url || !url.trim().startsWith('http')) {
    if (previewBox) previewBox.style.display = 'none';
    return;
  }
  if (previewImg && previewBox) {
    previewImg.src = url.trim();
    previewBox.style.display = 'block';
  }
}

function handleImageFileSelected(input) {
  const file = input.files?.[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = (e) => {
    const dataUrl = e.target.result;
    const previewBox = document.getElementById('addImagePreviewContainer');
    const previewImg = document.getElementById('addImagePreviewImg');
    if (previewImg && previewBox) {
      previewImg.src = dataUrl;
      previewBox.style.display = 'block';
    }
  };
  reader.readAsDataURL(file);
}

function submitAddedImage() {
  const placeIdInput = document.getElementById('addImagePlaceId');
  if (!placeIdInput) return;
  const placeId = placeIdInput.value;
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  const dict = window.i18n[currentLang] || window.i18n.by;
  let finalImage = '';

  const activeTab = document.getElementById('tabImgUrl')?.classList.contains('active') ? 'url' : 'file';
  if (activeTab === 'url') {
    const url = document.getElementById('addImageUrlInput')?.value.trim();
    if (!url) {
      showToast(dict.imageErrorToast || 'Калі ласка, увядзіце спасылку на выяву.');
      return;
    }
    finalImage = url;
  } else {
    const previewImg = document.getElementById('addImagePreviewImg');
    if (!previewImg || !previewImg.src || previewImg.src === window.location.href) {
      showToast(dict.imageErrorToast || 'Калі ласка, выберыце файл выявы.');
      return;
    }
    finalImage = previewImg.src;
  }

  const author = document.getElementById('addImageAuthorInput')?.value.trim() || '';

  // Update place in memory and localStorage overrides
  place.image = finalImage;
  savePlaceOverride(place.id, { image: finalImage, imageAuthor: author });

  // Record user contribution if authenticated or guest
  recordUserContribution({
    type: 'image',
    placeId: place.id,
    title: place.title,
    image: finalImage,
    author: author,
    date: Date.now()
  });

  closeModal('addImageModal');
  renderSidebarList();
  showPlaceDetail(place.id);
  showToast(dict.imageSuccessToast || 'Выява паспяхова дададзена! Дзякуй за ваш унёсак!');
}

// ========================================================
// User Authentication & Registration System (Google, Apple, Email)
// ========================================================

let currentUser = null;

function initAuth() {
  try {
    const stored = localStorage.getItem('albaruthenica_current_user');
    if (stored) {
      currentUser = JSON.parse(stored);
    }
  } catch (e) {
    currentUser = null;
  }
  updateAuthUI();
}

function saveCurrentUser(user) {
  currentUser = user;
  if (user) {
    localStorage.setItem('albaruthenica_current_user', JSON.stringify(user));
  } else {
    localStorage.removeItem('albaruthenica_current_user');
  }
  updateAuthUI();
}

function updateAuthUI() {
  const container = document.getElementById('userAuthContainer');
  if (!container) return;
  const dict = window.i18n[currentLang] || window.i18n.by;

  if (!currentUser) {
    container.innerHTML = `
      <button id="btnSignIn" class="btn btn-secondary btn-sm" onclick="openAuthModal()">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px; vertical-align: -2px;">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
          <circle cx="12" cy="7" r="4"></circle>
        </svg>
        <span class="btn-text-label">${dict.btnSignIn || 'Увайсці'}</span>
      </button>
    `;
  } else {
    const initial = (currentUser.name || currentUser.email || 'U')[0].toUpperCase();
    const avatarHtml = currentUser.avatar ? 
      `<img src="${currentUser.avatar}" alt="${currentUser.name}" class="user-profile-avatar" referrerpolicy="no-referrer">` :
      `<div class="user-profile-avatar">${initial}</div>`;

    const providerIcon = currentUser.provider === 'google' ? 'Google' : (currentUser.provider === 'apple' ? 'Apple' : 'Email');

    container.innerHTML = `
      <div class="user-profile-menu-wrap" style="position: relative;">
        <button type="button" class="user-profile-btn" onclick="toggleUserDropdown(event)">
          ${avatarHtml}
          <span class="user-profile-name">${currentUser.name || currentUser.email}</span>
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="6 9 12 15 18 9"></polyline>
          </svg>
        </button>
        <div class="user-profile-dropdown" id="userProfileDropdown">
          <div class="user-dropdown-header">
            <div class="user-dropdown-name">${currentUser.name || 'Карыстальнік'}</div>
            <div class="user-dropdown-email">${currentUser.email || ''}</div>
            <span class="user-provider-tag">${providerIcon}</span>
          </div>
          <button type="button" class="user-dropdown-item" onclick="openUserProfileModal()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            ${dict.userProfileTitle || 'Профіль і ўнёскі'}
          </button>
          <button type="button" class="user-dropdown-item danger" onclick="handleSignOut()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
            ${dict.btnSignOut || 'Выйсці'}
          </button>
        </div>
      </div>
    `;
  }
}

function toggleUserDropdown(event) {
  event?.stopPropagation();
  const dropdown = document.getElementById('userProfileDropdown');
  if (dropdown) {
    dropdown.classList.toggle('open');
  }
}

// Close dropdown on outside click
document.addEventListener('click', (e) => {
  const dropdown = document.getElementById('userProfileDropdown');
  if (dropdown && dropdown.classList.contains('open') && !e.target.closest('.user-profile-menu-wrap')) {
    dropdown.classList.remove('open');
  }
});

function openAuthModal() {
  openModal('authModal');
}

function closeAuthModal() {
  closeModal('authModal');
}

function switchAuthMode(mode) {
  const tabLogin = document.getElementById('authTabLoginBtn');
  const tabReg = document.getElementById('authTabRegisterBtn');
  const nameGroup = document.getElementById('authNameGroup');
  const submitBtn = document.getElementById('authSubmitBtn');
  const dict = window.i18n[currentLang] || window.i18n.by;

  if (mode === 'login') {
    tabLogin?.classList.add('active');
    tabReg?.classList.remove('active');
    if (nameGroup) nameGroup.style.display = 'none';
    if (submitBtn) submitBtn.innerHTML = `<span>${dict.authSubmitLogin || 'Увайсці ў акаўнт'}</span>`;
  } else {
    tabLogin?.classList.remove('active');
    tabReg?.classList.add('active');
    if (nameGroup) nameGroup.style.display = 'block';
    if (submitBtn) submitBtn.innerHTML = `<span>${dict.authSubmitRegister || 'Зарэгістравацца'}</span>`;
  }
}

// Google Sign-in flow
function handleGoogleSignIn() {
  closeModal('authModal');
  openModal('googleAuthPromptModal');
}

function confirmGoogleLogin(name, email) {
  const user = {
    id: 'google_' + Math.random().toString(36).substring(2, 10),
    name: name,
    email: email,
    avatar: 'https://lh3.googleusercontent.com/a/default-user=s96-c',
    provider: 'google',
    createdAt: Date.now(),
    contributions: getUserContributions()
  };
  saveCurrentUser(user);
  closeModal('googleAuthPromptModal');
  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(`${dict.authSuccessLogin || 'Вітаем!'} (${name})`);
}

function confirmCustomGoogleLogin() {
  const nameInput = document.getElementById('customGoogleName')?.value.trim();
  const emailInput = document.getElementById('customGoogleEmail')?.value.trim();
  if (!emailInput) {
    showToast('Калі ласка, увядзіце email.');
    return;
  }
  confirmGoogleLogin(nameInput || emailInput.split('@')[0], emailInput);
}

// Apple Sign-in flow
function handleAppleSignIn() {
  closeModal('authModal');
  openModal('appleAuthPromptModal');
}

function confirmAppleLogin() {
  const name = document.getElementById('appleUserNameInput')?.value.trim() || 'Apple Карыстальнік';
  const hideEmail = document.getElementById('appleHideEmailCheckbox')?.checked;
  const email = hideEmail ? 'privaterelay_' + Math.random().toString(36).substring(2, 8) + '@privaterelay.appleid.com' : 'user@icloud.com';

  const user = {
    id: 'apple_' + Math.random().toString(36).substring(2, 10),
    name: name,
    email: email,
    avatar: '',
    provider: 'apple',
    createdAt: Date.now(),
    contributions: getUserContributions()
  };
  saveCurrentUser(user);
  closeModal('appleAuthPromptModal');
  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(`${dict.authSuccessLogin || 'Вітаем!'} (${name})`);
}

// Email/Password login & registration flow
function handleEmailAuthSubmit(e) {
  e.preventDefault();
  const isRegister = document.getElementById('authTabRegisterBtn')?.classList.contains('active');
  const email = document.getElementById('authEmailInput')?.value.trim();
  const name = document.getElementById('authNameInput')?.value.trim() || email.split('@')[0];
  const dict = window.i18n[currentLang] || window.i18n.by;

  if (!email) return;

  const user = {
    id: 'usr_' + Math.random().toString(36).substring(2, 10),
    name: name,
    email: email,
    avatar: '',
    provider: 'email',
    createdAt: Date.now(),
    contributions: getUserContributions()
  };
  saveCurrentUser(user);
  closeModal('authModal');
  showToast(isRegister ? (dict.authSuccessRegister || 'Акаўнт паспяхова створаны!') : (dict.authSuccessLogin || 'Вы паспяхова ўвайшлі!'));
}

function handleSignOut() {
  saveCurrentUser(null);
  closeModal('userProfileModal');
  const dropdown = document.getElementById('userProfileDropdown');
  if (dropdown) dropdown.classList.remove('open');
  const dict = window.i18n[currentLang] || window.i18n.by;
  showToast(dict.authLoggedOut || 'Вы выйшлі з уліковага запісу.');
}

// Contributions management
function getUserContributions() {
  try {
    const list = localStorage.getItem('albaruthenica_user_contributions');
    return list ? JSON.parse(list) : [];
  } catch (e) {
    return [];
  }
}

function recordUserContribution(item) {
  const list = getUserContributions();
  list.unshift(item);
  localStorage.setItem('albaruthenica_user_contributions', JSON.stringify(list));
  if (currentUser) {
    currentUser.contributions = list;
    localStorage.setItem('albaruthenica_current_user', JSON.stringify(currentUser));
  }
}

function openUserProfileModal() {
  const bodyEl = document.getElementById('userProfileBody');
  if (!bodyEl) return;
  const dict = window.i18n[currentLang] || window.i18n.by;

  if (!currentUser) {
    bodyEl.innerHTML = `<p>${dict.noResults || 'Карыстальнік не аўтарызаваны.'}</p>`;
    openModal('userProfileModal');
    return;
  }

  const initial = (currentUser.name || currentUser.email || 'U')[0].toUpperCase();
  const avatarHtml = currentUser.avatar ? 
    `<img src="${currentUser.avatar}" alt="${currentUser.name}" class="user-profile-big-avatar" referrerpolicy="no-referrer">` :
    `<div class="user-profile-big-avatar">${initial}</div>`;

  const contributions = getUserContributions();
  const imageCount = contributions.filter(c => c.type === 'image').length;
  const placeCount = contributions.filter(c => c.type === 'place').length;

  const contribListHtml = contributions.length > 0 ? contributions.map(c => {
    const title = getLocalized(c.title) || c.placeId || 'Унёсак';
    const typeLabel = c.type === 'image' ? '📷 Фотаздымак' : '📍 Месца';
    const dateStr = c.date ? new Date(c.date).toLocaleDateString() : '';
    return `
      <div class="user-contrib-item">
        <div>
          <span style="font-weight: 600;">${title}</span>
          <div style="font-size: 0.72rem; color: var(--text-muted);">${typeLabel} &bull; ${dateStr}</div>
        </div>
        ${c.image ? `<img src="${c.image}" style="width: 32px; height: 32px; object-fit: cover; border-radius: 2px;" referrerpolicy="no-referrer">` : ''}
      </div>
    `;
  }).join('') : `
    <div style="padding: 0.75rem; color: var(--text-muted); font-size: 0.8rem; text-align: center;">
      ${dict.userNoContributions || 'У вас пакуль няма захаваных унёскаў на гэтай прыладзе.'}
    </div>
  `;

  bodyEl.innerHTML = `
    <div class="user-profile-header-card">
      ${avatarHtml}
      <div>
        <div style="font-size: 1rem; font-weight: 700; color: var(--text-main);">${currentUser.name}</div>
        <div style="font-size: 0.8rem; color: var(--text-muted);">${currentUser.email}</div>
        <span class="user-provider-tag" style="margin-top: 0.25rem;">${currentUser.provider.toUpperCase()}</span>
      </div>
    </div>

    <div class="user-profile-stats-grid">
      <div class="user-profile-stat-box">
        <div class="user-profile-stat-num">${placeCount}</div>
        <div class="user-profile-stat-lbl">Дададзеныя месцы</div>
      </div>
      <div class="user-profile-stat-box">
        <div class="user-profile-stat-num">${imageCount}</div>
        <div class="user-profile-stat-lbl">Дададзеныя выявы</div>
      </div>
    </div>

    <div style="margin-top: 1rem;">
      <div style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 0.5rem;">
        ${dict.userContributions || 'Мае ўнёскі'} (${contributions.length})
      </div>
      <div class="user-contributions-list">
        ${contribListHtml}
      </div>
    </div>
  `;

  const dropdown = document.getElementById('userProfileDropdown');
  if (dropdown) dropdown.classList.remove('open');
  openModal('userProfileModal');
}

// Parse pasted coordinates or map links
function parseCoordinatesInput(str) {
  if (!str) return null;
  str = str.trim();

  // 1. Google Maps URL patterns
  const gmapAt = str.match(/@(-?\d+\.\d+),(-?\d+\.\d+)/);
  if (gmapAt) {
    return [parseFloat(gmapAt[1]), parseFloat(gmapAt[2])];
  }
  const gmapQuery = str.match(/[?&](?:q|ll|query)=(-?\d+\.\d+),(-?\d+\.\d+)/);
  if (gmapQuery) {
    return [parseFloat(gmapQuery[1]), parseFloat(gmapQuery[2])];
  }

  // 2. OpenStreetMap URL pattern
  const osmMatch = str.match(/#map=\d+\/(-?\d+\.\d+)\/(-?\d+\.\d+)/);
  if (osmMatch) {
    return [parseFloat(osmMatch[1]), parseFloat(osmMatch[2])];
  }

  // 3. Simple coordinate pair: "54.6872, 25.2797" or "54.6872 25.2797"
  const pairMatch = str.match(/^(-?\d{1,2}(?:\.\d+)?)[,\s]+(-?\d{1,3}(?:\.\d+)?)$/);
  if (pairMatch) {
    const lat = parseFloat(pairMatch[1]);
    const lng = parseFloat(pairMatch[2]);
    if (!isNaN(lat) && !isNaN(lng) && Math.abs(lat) <= 90 && Math.abs(lng) <= 180) {
      return [lat, lng];
    }
  }

  return null;
}

// ========================================================
// Coordinate Picking & Custom Place Management
// ========================================================

// Start user map picking for an existing place
function startPlaceCoordinateCorrection(placeId) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  targetPlaceForCoordsCorrection = placeId;
  pickCoordsMode = false;
  cleanUpPickMarker();
  closePlaceDetail();

  const banner = document.getElementById('pickCoordsBanner');
  const bannerText = document.getElementById('pickCoordsBannerText');
  const btnConfirm = document.getElementById('btnConfirmPick');
  const title = getLocalized(place.title);
  if (bannerText) {
    bannerText.textContent = `${window.i18n[currentLang]?.clickMapToPickForPlace || 'Клікніце на карце, каб указаць каардынаты для'}: «${title}»`;
  }
  if (btnConfirm) btnConfirm.style.display = 'none';
  if (banner) banner.style.display = 'flex';
  showToast(bannerText ? bannerText.textContent : 'Клікніце ў пункт на карце');
}

// Handle map click during picking mode
function handleMapPickClick(latlng) {
  const latFixed = parseFloat(latlng.lat.toFixed(5));
  const lngFixed = parseFloat(latlng.lng.toFixed(5));
  pendingPickedCoords = { lat: latFixed, lng: lngFixed };

  if (!tempPickMarker) {
    const pinIcon = L.divIcon({
      className: 'temp-pick-marker-icon',
      html: '<div style="background:#dc2626; color:#ffffff; width:34px; height:34px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 3px 12px rgba(220,38,38,0.6); border:2px solid #ffffff; font-size:18px; cursor:grab;">📍</div>',
      iconSize: [34, 34],
      iconAnchor: [17, 34],
      popupAnchor: [0, -34]
    });
    tempPickMarker = L.marker([latFixed, lngFixed], { icon: pinIcon, draggable: true }).addTo(map);

    tempPickMarker.on('dragend', (evt) => {
      const pos = evt.target.getLatLng();
      const dLat = parseFloat(pos.lat.toFixed(5));
      const dLng = parseFloat(pos.lng.toFixed(5));
      pendingPickedCoords = { lat: dLat, lng: dLng };
      updatePickMarkerPopup();
      updatePickBannerCoords();
    });
  } else {
    tempPickMarker.setLatLng([latFixed, lngFixed]);
  }

  updatePickMarkerPopup();
  updatePickBannerCoords();
  tempPickMarker.openPopup();
}

// Update the popup attached to the temporary pick marker
function updatePickMarkerPopup() {
  if (!tempPickMarker || !pendingPickedCoords) return;
  const { lat, lng } = pendingPickedCoords;
  const isCorrection = !!targetPlaceForCoordsCorrection;
  const targetPlace = isCorrection ? allPlaces.find(p => p.id === targetPlaceForCoordsCorrection) : null;
  const placeTitle = targetPlace ? getLocalized(targetPlace.title) : '';

  const saveLabel = window.i18n[currentLang]?.btnConfirmCoords || '✅ Захаваць і прымяніць';
  const cancelLabel = window.i18n[currentLang]?.btnCancelPick || '✕ Выйсці з выбару';
  const headerHtml = isCorrection
    ? `<div class="popup-title">📍 Новыя каардынаты для:<br><strong>«${escapeHtml(placeTitle)}»</strong></div>`
    : `<div class="popup-title">📍 Выбраная кропка</div>`;

  const popupHtml = `
    <div class="pick-coords-popup">
      ${headerHtml}
      <div class="popup-coords">${lat}, ${lng}</div>
      <div class="popup-hint">(перацягніце маркер для ўдакладнення)</div>
      <div class="popup-actions">
        <button type="button" class="btn btn-primary btn-sm" onclick="window.confirmPickedCoordinates()">
          ${saveLabel}
        </button>
        <button type="button" class="btn btn-secondary btn-sm" onclick="window.cancelPickedCoordinates()">
          ${cancelLabel}
        </button>
      </div>
    </div>
  `;

  tempPickMarker.bindPopup(popupHtml, { minWidth: 220, closeOnClick: false, autoClose: false });
}

// Update the floating top banner with current coordinates
function updatePickBannerCoords() {
  const banner = document.getElementById('pickCoordsBanner');
  const bannerText = document.getElementById('pickCoordsBannerText');
  const btnConfirm = document.getElementById('btnConfirmPick');
  if (!banner || !bannerText) return;

  if (pendingPickedCoords) {
    const { lat, lng } = pendingPickedCoords;
    const saveLabel = window.i18n[currentLang]?.btnConfirmCoords || '✅ Захаваць і прымяніць';
    bannerText.innerHTML = `📍 Выбрана: <span class="coords-indicator">${lat}, ${lng}</span>`;
    if (btnConfirm) {
      btnConfirm.textContent = saveLabel;
      btnConfirm.style.display = 'inline-block';
    }
  }
}

// Confirm picked coordinates (from marker popup or banner button)
function confirmPickedCoordinates(customLat, customLng) {
  const lat = customLat !== undefined ? customLat : pendingPickedCoords?.lat;
  const lng = customLng !== undefined ? customLng : pendingPickedCoords?.lng;

  if (lat === undefined || lng === undefined) return;

  // Case 1: Correcting coordinates of an existing place
  if (targetPlaceForCoordsCorrection) {
    const placeId = targetPlaceForCoordsCorrection;
    const place = allPlaces.find(p => p.id === placeId);
    if (place) {
      place.coordinates = [lat, lng];
      place.unverifiedCoordinates = false;
      place.isUnverifiedCoordinates = false;

      // Centralized savePlaceOverride (writes to both place_overrides and overrides)
      savePlaceOverride(placeId, {
        coordinates: [lat, lng],
        unverifiedCoordinates: false,
        isUnverifiedCoordinates: false
      });

      // If user-created place, update in albaruthenica_user_places
      if (place.isUserCreated) {
        try {
          const userPlaces = JSON.parse(localStorage.getItem('albaruthenica_user_places') || '[]');
          const idx = userPlaces.findIndex(p => p.id === placeId);
          if (idx >= 0) {
            userPlaces[idx].coordinates = [lat, lng];
            userPlaces[idx].unverifiedCoordinates = false;
            userPlaces[idx].isUnverifiedCoordinates = false;
            localStorage.setItem('albaruthenica_user_places', JSON.stringify(userPlaces));
          }
        } catch (e) {
          console.error('Error updating user place coords:', e);
        }
      }

      // Re-render markers to update Leaflet markerCluster properly
      renderMarkers();
      renderSidebarList();
      updateStats();

      logUserContribution('coords', placeId, {
        title: getLocalized(place.title),
        coordinates: [lat, lng]
      });

      showToast(`${window.i18n[currentLang]?.coordsSaved || 'Каардынаты паспяхова захаваныя і прымененыя!'}: ${lat}, ${lng}`);
    }

    cleanUpPickMarker();
    targetPlaceForCoordsCorrection = null;
    pickCoordsMode = false;
    const banner = document.getElementById('pickCoordsBanner');
    if (banner) banner.style.display = 'none';
    if (map && typeof map.closePopup === 'function') map.closePopup();
    selectPlace(placeId);
    return;
  }

  // Case 2: Picking coordinates for Add Place modal
  if (pickCoordsMode) {
    const latInput = document.getElementById('formLat');
    const lngInput = document.getElementById('formLng');
    const smartInput = document.getElementById('formCoordsSmart');
    if (latInput && lngInput) {
      latInput.value = lat;
      lngInput.value = lng;
    }
    if (smartInput) {
      smartInput.value = `${lat}, ${lng}`;
    }

    showToast(`${window.i18n[currentLang]?.coordsSelected || 'Выбраныя каардынаты:'} ${lat}, ${lng}`);
    cleanUpPickMarker();
    pickCoordsMode = false;
    const banner = document.getElementById('pickCoordsBanner');
    if (banner) banner.style.display = 'none';
    if (map && typeof map.closePopup === 'function') map.closePopup();
    openModal('addPlaceModal');
  }
}

// Cancel coordinate picking
function cancelPickedCoordinates() {
  const prevTarget = targetPlaceForCoordsCorrection;
  const wasAdd = pickCoordsMode;
  cleanUpPickMarker();
  targetPlaceForCoordsCorrection = null;
  pickCoordsMode = false;

  const banner = document.getElementById('pickCoordsBanner');
  if (banner) banner.style.display = 'none';
  if (map && typeof map.closePopup === 'function') map.closePopup();

  if (prevTarget) {
    selectPlace(prevTarget);
  } else if (wasAdd) {
    openModal('addPlaceModal');
  }
}

// Remove temporary pick marker
function cleanUpPickMarker() {
  if (tempPickMarker) {
    map.removeLayer(tempPickMarker);
    tempPickMarker = null;
  }
  pendingPickedCoords = null;
}

// Save a place directly from Add Place modal to map & localStorage
function handleSavePlaceDirect() {
  const nameBy = document.getElementById('formNameBy')?.value.trim();
  const nameRu = document.getElementById('formNameRu')?.value.trim();
  const nameEn = document.getElementById('formNameEn')?.value.trim();
  const category = document.getElementById('formCategory')?.value;
  const country = document.getElementById('formCountry')?.value.trim();
  const city = document.getElementById('formCity')?.value.trim();
  let lat = parseFloat(document.getElementById('formLat')?.value);
  let lng = parseFloat(document.getElementById('formLng')?.value);
  const descBy = document.getElementById('formDescBy')?.value.trim();
  const descRu = document.getElementById('formDescRu')?.value.trim();
  const descEn = document.getElementById('formDescEn')?.value.trim();
  const image = document.getElementById('formImage')?.value.trim();
  const tagsStr = document.getElementById('formTags')?.value.trim();
  const wikiUrl = document.getElementById('formWikiUrl')?.value.trim();
  const articleUrl = document.getElementById('formArticleUrl')?.value.trim();

  // If lat or lng is missing, try parsing from smart input
  if (isNaN(lat) || isNaN(lng)) {
    const smartVal = document.getElementById('formCoordsSmart')?.value.trim();
    if (smartVal) {
      const parsed = parseCoordinatesInput(smartVal);
      if (parsed) {
        lat = parsed[0];
        lng = parsed[1];
        if (document.getElementById('formLat')) document.getElementById('formLat').value = lat.toFixed(5);
        if (document.getElementById('formLng')) document.getElementById('formLng').value = lng.toFixed(5);
      }
    }
  }

  if (!nameBy) {
    alert(window.i18n[currentLang]?.alertEnterName || 'Калі ласка, увядзіце назву месца!');
    document.getElementById('formNameBy')?.focus();
    return;
  }

  if (isNaN(lat) || isNaN(lng)) {
    alert(window.i18n[currentLang]?.alertEnterCoords || 'Калі ласка, укажыце каардынаты (шырату і даўгату) альбо выберыце кропку на карце!');
    document.getElementById('formCoordsSmart')?.focus();
    return;
  }

  // Generate safe ID slug
  const baseSlug = nameEn 
    ? nameEn.toLowerCase().replace(/[^a-z0-9]/g, '-').replace(/-+/g, '-') 
    : 'user-place-' + Date.now();
  const slug = (baseSlug.length > 2) ? baseSlug : 'place-' + Date.now();

  const links = [];
  if (wikiUrl) {
    links.push({ title: "Вікіпедыя пра аб’ект", url: wikiUrl });
  }
  if (articleUrl) {
    links.push({ title: "Артыкул: Беларускі бэкграўнд", url: articleUrl });
  }

  const newPlaceObj = {
    id: slug,
    title: {
      by: nameBy,
      ru: nameRu || nameBy,
      en: nameEn || nameBy
    },
    category: category || 'historical',
    country: {
      by: country || '',
      ru: country || '',
      en: country || ''
    },
    city: {
      by: city || '',
      ru: city || '',
      en: city || ''
    },
    coordinates: [parseFloat(lat.toFixed(5)), parseFloat(lng.toFixed(5))],
    description: {
      by: descBy || '',
      ru: descRu || descBy || '',
      en: descEn || descBy || ''
    },
    image: image || '',
    links: links,
    tags: tagsStr ? tagsStr.split(',').map(t => t.trim()).filter(Boolean) : [],
    isUserCreated: true
  };

  // Persist to localStorage
  try {
    const userPlaces = JSON.parse(localStorage.getItem('albaruthenica_user_places') || '[]');
    const existingIndex = userPlaces.findIndex(p => p.id === newPlaceObj.id);
    if (existingIndex >= 0) {
      userPlaces[existingIndex] = newPlaceObj;
    } else {
      userPlaces.unshift(newPlaceObj);
    }
    localStorage.setItem('albaruthenica_user_places', JSON.stringify(userPlaces));
  } catch (err) {
    console.error('Failed to save to localStorage:', err);
  }

  // Prepend to in-memory allPlaces
  const inMemoryIndex = allPlaces.findIndex(p => p.id === newPlaceObj.id);
  if (inMemoryIndex >= 0) {
    allPlaces[inMemoryIndex] = newPlaceObj;
  } else {
    allPlaces.unshift(newPlaceObj);
  }

  // Re-render markers and list
  renderMarkers();
  renderSidebarList();
  updateStats();

  // Log contribution
  logUserContribution('add', newPlaceObj.id, {
    title: nameBy,
    category: newPlaceObj.category,
    coordinates: newPlaceObj.coordinates
  });

  // Close modal and reset form
  closeModal('addPlaceModal');
  document.getElementById('addPlaceForm')?.reset();
  const jsonResultContainer = document.getElementById('jsonResultContainer');
  if (jsonResultContainer) jsonResultContainer.style.display = 'none';

  // Fly to and open detail for new place
  selectPlace(newPlaceObj.id);

  showToast(window.i18n[currentLang]?.placeSavedDirect || 'Месца паспяхова захавана і дададзена на карту!');
}

// Delete user-created place
function deleteUserPlace(placeId) {
  if (!confirm('Вы сапраўды хочаце выдаліць гэтае месца з вашай карты?')) return;
  try {
    const userPlaces = JSON.parse(localStorage.getItem('albaruthenica_user_places') || '[]');
    const updated = userPlaces.filter(p => p.id !== placeId);
    localStorage.setItem('albaruthenica_user_places', JSON.stringify(updated));
  } catch (err) {
    console.error('Error removing from localStorage:', err);
  }

  allPlaces = allPlaces.filter(p => p.id !== placeId);
  closePlaceDetail();
  renderMarkers();
  renderSidebarList();
  updateStats();
  showToast('Месца выдалена з вашай карты.');
}

// Open Image Lightbox
function openImageLightbox(src, caption = '') {
  const modal = document.getElementById('imageLightboxModal');
  const img = document.getElementById('lightboxImg');
  const cap = document.getElementById('lightboxCaption');
  if (!modal || !img) return;
  img.src = src;
  if (cap) cap.textContent = caption;
  openModal('imageLightboxModal');
}

// Window global exposures for image, coordinate and auth actions
window.handleHeroImageError = handleHeroImageError;
window.openAddImageModal = openAddImageModal;
window.switchAddImageTab = switchAddImageTab;
window.previewAddImageUrl = previewAddImageUrl;
window.handleImageFileSelected = handleImageFileSelected;
window.submitAddedImage = submitAddedImage;

window.openAuthModal = openAuthModal;
window.closeAuthModal = closeAuthModal;
window.switchAuthMode = switchAuthMode;
window.handleGoogleSignIn = handleGoogleSignIn;
window.confirmGoogleLogin = confirmGoogleLogin;
window.confirmCustomGoogleLogin = confirmCustomGoogleLogin;
window.handleAppleSignIn = handleAppleSignIn;
window.confirmAppleLogin = confirmAppleLogin;
window.handleEmailAuthSubmit = handleEmailAuthSubmit;
window.handleSignOut = handleSignOut;
window.openUserProfileModal = openUserProfileModal;
window.toggleUserDropdown = toggleUserDropdown;

window.parseCoordinatesInput = parseCoordinatesInput;
window.startPlaceCoordinateCorrection = startPlaceCoordinateCorrection;
window.confirmPickedCoordinates = confirmPickedCoordinates;
window.cancelPickedCoordinates = cancelPickedCoordinates;
window.handleSavePlaceDirect = handleSavePlaceDirect;
window.deleteUserPlace = deleteUserPlace;
window.openImageLightbox = openImageLightbox;


