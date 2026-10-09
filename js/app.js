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

// Admin moderation state
let isAdminMode = localStorage.getItem('albaruthenica_admin_mode') === 'true';
let filterOnlyUnverified = false;
let adminPickMode = false;
let activeDraggableMarker = null;

// Category config with distinct colors and crisp SVG glyph icons
const CATEGORY_CONFIG = {
  monument: {
    color: '#d97706',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm-3 8a3 3 0 0 0-3 3v2h12v-2a3 3 0 0 0-3-3H9zm-5 7h16v2H4v-2zm-2 3h20v2H2v-2z"/></svg>`
  },
  historical: {
    color: '#dc2626',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M2 4h4v3h2V4h4v3h2V4h4v3h2V4h2v16H2V4zm2 14h16V9h-2v2h-4V9h-2v2h-4V9H4v9zm7-5a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v5h-4v-5z"/></svg>`
  },
  culture: {
    color: '#2563eb',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2L2 7v2h20V7L12 2zM4 11v7h3v-7H4zm6 0v7h4v-7h-4zm7 0v7h3v-7h-3zM2 20v2h20v-2H2z"/></svg>`
  },
  church: {
    color: '#7c3aed',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M11 2h2v2h2v2h-2v2h2l1 2v12h-2v-4a2 2 0 0 0-4 0v4H4V10l1-2h2V6H5V4h2V2h2v2h2V2zm-3 8v2h8v-2H8z"/></svg>`
  },
  plaque: {
    color: '#059669',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M4 3h16a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zm2 4v2h12V7H6zm0 4v2h12v-2H6zm0 4v2h8v-2H6z"/></svg>`
  },
  grave: {
    color: '#475569',
    icon: `<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12 2C8.69 2 6 4.69 6 8v12h12V8c0-3.31-2.69-6-6-6zm0 4c.55 0 1 .45 1 1v1h1c.55 0 1 .45 1 1s-.45 1-1 1h-1v4c0 .55-.45 1-1 1s-1-.45-1-1v-4H9c-.55 0-1-.45-1-1s.45-1 1-1h1V7c0-.55.45-1 1-1zm-8 16h16v2H4v-2z"/></svg>`
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

document.addEventListener('DOMContentLoaded', () => {
  // Check admin parameter in URL query or hash: ?admin or #admin
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('admin') || window.location.hash === '#admin') {
    isAdminMode = true;
    localStorage.setItem('albaruthenica_admin_mode', 'true');
  }

  initI18n();
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
let activeBaseLayerKey = 'voyager';

function setLanguage(lang) {
  if (['by', 'ru', 'en'].includes(lang)) {
    currentLang = lang;
    localStorage.setItem('albaruthenica_lang', lang);
    initI18n();
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

  // Map click for coordinate picker (Add Place modal OR Admin moderation)
  map.on('click', (e) => {
    if (adminPickMode && selectedPlaceId) {
      handleAdminMapClick(e.latlng);
      return;
    }

    if (pickCoordsMode) {
      const { lat, lng } = e.latlng;
      const latFixed = lat.toFixed(5);
      const lngFixed = lng.toFixed(5);

      const latInput = document.getElementById('formLat');
      const lngInput = document.getElementById('formLng');
      if (latInput && lngInput) {
        latInput.value = latFixed;
        lngInput.value = lngFixed;
      }

      if (tempPickMarker) {
        tempPickMarker.setLatLng([lat, lng]);
      } else {
        tempPickMarker = L.marker([lat, lng]).addTo(map);
      }

      showToast(`${window.i18n[currentLang].coordsSelected} ${latFixed}, ${lngFixed}`);
      pickCoordsMode = false;
      document.getElementById('pickCoordsBanner').style.display = 'none';
      openModal('addPlaceModal');
    }
  });
}

// Setup base layers (Voyager, OSM, Satellite)
function setupBaseLayers() {
  const voyagerLayer = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  });

  const osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19,
    referrerPolicy: 'strict-origin-when-cross-origin'
  });

  const satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
    maxZoom: 19
  });

  baseLayers = {
    voyager: voyagerLayer,
    osm: osmLayer,
    satellite: satelliteLayer
  };

  // Add default layer (Voyager)
  baseLayers[activeBaseLayerKey].addTo(map);

  map.on('baselayerchange', (e) => {
    if (e.layer === baseLayers.satellite) activeBaseLayerKey = 'satellite';
    else if (e.layer === baseLayers.osm) activeBaseLayerKey = 'osm';
    else activeBaseLayerKey = 'voyager';
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
    [dict.layerVoyager || '🎨 Светлая (CartoDB)']: baseLayers.voyager,
    [dict.layerOSM || '🗺️ OpenStreetMap']: baseLayers.osm,
    [dict.layerSatellite || '🛰️ Спадарожнік (Esri)']: baseLayers.satellite
  };

  layerControl = L.control.layers(layerLabels, null, {
    position: 'topright',
    collapsed: false
  }).addTo(map);
}

// Client-side overrides for coordinates & verification status (moderation)
function getPlaceOverrides() {
  try {
    return JSON.parse(localStorage.getItem('albaruthenica_place_overrides') || '{}');
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
  localStorage.setItem('albaruthenica_place_overrides', JSON.stringify(overrides));
  updateAdminUI();
}

// Fetch places & persons data
async function loadPlaces() {
  try {
    const response = await fetch('data/places.json');
    if (!response.ok) throw new Error('Failed to load places.json');
    allPlaces = await response.json();
  } catch (error) {
    console.warn('Fetch places.json failed, falling back to window.INITIAL_PLACES:', error);
    if (window.INITIAL_PLACES && Array.isArray(window.INITIAL_PLACES)) {
      allPlaces = window.INITIAL_PLACES;
    }
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
      }
    }
  });

  try {
    const responsePersons = await fetch('data/persons.json');
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
    { id: 'monument', label: dict.categories.monument },
    { id: 'grave', label: dict.categories.grave },
    { id: 'church', label: dict.categories.church },
    { id: 'culture', label: dict.categories.culture },
    { id: 'historical', label: dict.categories.historical },
    { id: 'plaque', label: dict.categories.plaque }
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

    const popupHtml = `
      <div class="popup-card">
        ${place.image ? `<img src="${place.image}" alt="${title}" class="popup-img" loading="lazy" referrerpolicy="no-referrer">` : ''}
        <div class="popup-body">
          <span class="place-card-category cat-${place.category}">${categoryName}</span>
          ${unverifiedPopupNotice}
          <div class="popup-title">${title}</div>
          <div class="popup-loc">${city}, ${country}</div>
          <button class="btn btn-primary btn-sm" style="width: 100%" onclick="selectPlace('${place.id}')">
            ${window.i18n[currentLang].detailsHeading}
          </button>
        </div>
      </div>
    `;

    marker.bindPopup(popupHtml, { maxWidth: 280, minWidth: 220 });
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
    if (activeCategory !== 'all' && place.category !== activeCategory) {
      return false;
    }

    // Search query check
    if (searchQuery.trim() !== '') {
      const q = searchQuery.toLowerCase().trim();
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
    const thumb = place.image || 'https://images.unsplash.com/photo-1517824806704-9040b037703b?auto=format&fit=crop&w=200&q=80';

    const unverifiedBadge = place.unverifiedCoordinates ? `
      <span class="unverified-coords-badge" title="${dict.unverifiedCoordsNotice || ''}">
        ${dict.unverifiedCoordsBadge || 'Неправерана'}
      </span>
    ` : '';

    const nestedBadge = (place.items && place.items.length > 0) ? `
      <span class="place-card-nested-badge">
        ${place.items.length} ${dict.nestedObjectsBadge || 'аб’ектаў'}
      </span>
    ` : '';

    return `
      <div class="place-card ${selectedPlaceId === place.id ? 'active' : ''}" 
           id="card-${place.id}"
           onclick="selectPlace('${place.id}')">
        <img src="${thumb}" alt="${title}" class="place-card-thumb" loading="lazy" referrerpolicy="no-referrer">
        <div class="place-card-content">
          <div>
            <div class="place-card-title">${title}</div>
            <div class="place-card-meta">${city}, ${country}</div>
          </div>
          <div class="place-card-badges">
            <span class="place-card-category">
              ${categoryName}
            </span>
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

  counterEl.innerHTML = `
    ${dict.statsFound} <strong>${filtered.length}</strong> ${dict.statsPlaces} 
    (<strong>${countries.size}</strong> ${dict.statsCountries})
  `;
}

// Select a place (click from card or map)
function selectPlace(placeId, updateHash = true) {
  const place = allPlaces.find(p => p.id === placeId);
  if (!place) return;

  selectedPlaceId = placeId;
  highlightSidebarCard(placeId);

  // Pan map smoothly to place
  const [lat, lng] = place.coordinates;
  map.flyTo([lat, lng], 13, { duration: 1.2 });

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

  const title = getLocalized(place.title);
  const city = getLocalized(place.city);
  const country = getLocalized(place.country);
  const desc = getLocalized(place.description);
  const categoryName = window.i18n[currentLang].categories[place.category] || place.category;
  const [lat, lng] = place.coordinates;
  const dict = window.i18n[currentLang];

  const heroImg = place.image ? `<img src="${place.image}" alt="${title}" class="detail-hero-img" loading="lazy" referrerpolicy="no-referrer">` : '';

  const tagsHtml = (place.tags || []).map(t => `<span class="detail-tag">#${t}</span>`).join('');

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
              <img src="${p.image || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'}" 
                   alt="${getLocalized(p.name)}" class="associated-person-avatar" loading="lazy" referrerpolicy="no-referrer"
                   onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png'">
              <span>${getLocalized(p.name)}</span>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // Nested sub-items (artworks, graves, exhibits)
  let nestedItemsHtml = '';
  if (place.items && Array.isArray(place.items) && place.items.length > 0) {
    nestedItemsHtml = `
      <div class="nested-items-section">
        <div class="nested-items-header">
          <strong>${dict.nestedObjectsTitle || 'Укладзеныя аб’екты, творы і пахаванні:'}</strong>
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

          return `
          <div class="nested-item-card" onclick="openNestedItemModal('${place.id}', ${idx})" title="${dict.clickToViewDetails || 'Націсніце для прагляду дэталяў'}">
            <div class="nested-item-card-header">
              <div class="nested-item-title">${it.title}</div>
              ${it.year ? `<span class="nested-item-year">${it.year}</span>` : ''}
            </div>
            ${personBadge ? `<div class="nested-item-meta">${personBadge}</div>` : ''}
            ${it.description ? `<div class="nested-item-desc">${it.description}</div>` : ''}
            ${it.image ? `<div class="nested-item-image-wrapper"><img src="${it.image}" alt="${it.title}" class="nested-item-thumb" loading="lazy" referrerpolicy="no-referrer"></div>` : ''}
            <div class="nested-item-card-footer">
              <span class="nested-item-view-btn">${dict.viewDetails || 'Падрабязней'} &rarr;</span>
            </div>
          </div>
        `}).join('')}
        </div>
      </div>
    `;
  }

  // Categorized links (Wikipedia, background articles, catalog)
  const linksHtml = (place.links || []).map(l => {
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
      <div style="font-weight: 700; color: var(--text-main); margin-bottom: 2px; text-transform: uppercase; font-size: 0.72rem; letter-spacing: 0.04em;">
        ${dict.unverifiedCoordsBadge || 'Неправераныя каардынаты'}
      </div>
      <div style="font-size: 0.78rem; color: #52525b; line-height: 1.4;">
        ${dict.unverifiedCoordsNotice || 'Каардынаты гэтага пункта дададзены аўтаматычна з гістарычных крыніц і патрабуюць верыфікацыі.'}
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
      <h2 class="detail-title">${title}</h2>
      <div class="detail-location">
        <strong>${city}, ${country}</strong> &bull; <code id="detailCoordsCode">${lat.toFixed(4)}, ${lng.toFixed(4)}</code>
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
            <img src="${it.image}" alt="${it.title}" class="nested-detail-image" loading="lazy" referrerpolicy="no-referrer">
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
      searchQuery = e.target.value;
      if (searchClear) {
        searchClear.style.display = searchQuery ? 'block' : 'none';
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

  // Pick coords on map button in Add modal
  document.getElementById('btnPickOnMap')?.addEventListener('click', () => {
    closeModal('addPlaceModal');
    pickCoordsMode = true;
    document.getElementById('pickCoordsBanner').style.display = 'flex';
    showToast(window.i18n[currentLang].clickMapToPick);
  });

  // Cancel pick mode banner
  document.getElementById('btnCancelPick')?.addEventListener('click', () => {
    pickCoordsMode = false;
    document.getElementById('pickCoordsBanner').style.display = 'none';
    openModal('addPlaceModal');
  });

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
    const avatar = p.image || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';

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
  const avatar = person.image || 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';
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
      const plThumb = pl.image || '';

      return `
        <div class="person-place-item" onclick="viewPersonPlaceOnMap('${pl.id}')">
          ${plThumb ? `<img src="${plThumb}" alt="${plTitle}" class="person-place-thumb" loading="lazy" referrerpolicy="no-referrer">` : `<div class="person-place-thumb" style="display:flex;align-items:center;justify-content:center;font-size:0.75rem;color:var(--text-muted);border:1px solid var(--border-color);"></div>`}
          <div class="person-place-info">
            <div class="person-place-title">${plTitle}</div>
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
          <div class="admin-queue-title">${title}</div>
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

