// Albaruthenica - Main Application Logic

let map;
let markerCluster;
let allPlaces = [];
let markersMap = new Map();
let currentLang = localStorage.getItem('albaruthenica_lang') || 'by';
let activeCategory = 'all';
let searchQuery = '';
let selectedPlaceId = null;
let pickCoordsMode = false;
let tempPickMarker = null;

// Category icons config
const CATEGORY_ICONS = {
  monument: '🏛️',
  grave: '🕯️',
  church: '⛪',
  culture: '📚',
  historical: '🏰',
  plaque: '📜'
};

document.addEventListener('DOMContentLoaded', () => {
  initI18n();
  initMap();
  loadPlaces();
  setupEventListeners();
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
    updateLayerControl();
    renderSidebarList();
    if (selectedPlaceId) {
      showPlaceDetail(selectedPlaceId, false);
    }
    updateAllMarkersTooltips();
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

  // Map click for coordinate picker in "Add Place" modal
  map.on('click', (e) => {
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

// Setup base layers (OSM, Satellite, Light CartoDB)
function setupBaseLayers() {
  const osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    maxZoom: 19
  });

  const satelliteLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
    maxZoom: 19
  });

  const voyagerLayer = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  });

  baseLayers = {
    osm: osmLayer,
    satellite: satelliteLayer,
    voyager: voyagerLayer
  };

  // Add default layer (OSM)
  baseLayers[activeBaseLayerKey].addTo(map);

  map.on('baselayerchange', (e) => {
    if (e.layer === baseLayers.satellite) activeBaseLayerKey = 'satellite';
    else if (e.layer === baseLayers.voyager) activeBaseLayerKey = 'voyager';
    else activeBaseLayerKey = 'osm';
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
    [dict.layerOSM || '🗺️ OpenStreetMap']: baseLayers.osm,
    [dict.layerSatellite || '🛰️ Спадарожнік (Esri)']: baseLayers.satellite,
    [dict.layerVoyager || '🎨 Светлая (CartoDB)']: baseLayers.voyager
  };

  layerControl = L.control.layers(layerLabels, null, {
    position: 'topright',
    collapsed: false
  }).addTo(map);
}

// Fetch places data
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
  renderMarkers();
  renderSidebarList();
  updateStats();

  // Check if initial hash matches a place
  checkUrlHash();
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

  container.innerHTML = categories.map(cat => `
    <button class="category-pill ${activeCategory === cat.id ? 'active' : ''}" data-cat="${cat.id}">
      ${cat.label}
    </button>
  `).join('');

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

// Create custom pin HTML icon
function createCustomMarkerIcon(category) {
  const icon = CATEGORY_ICONS[category] || '📍';
  return L.divIcon({
    className: 'custom-pin-container',
    html: `<div class="custom-pin category-${category}">${icon}</div>`,
    iconSize: [32, 32],
    iconAnchor: [16, 16],
    popupAnchor: [0, -18]
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
      icon: createCustomMarkerIcon(place.category)
    });

    // Custom popup
    const popupHtml = `
      <div class="popup-card">
        ${place.image ? `<img src="${place.image}" alt="${title}" class="popup-img" loading="lazy">` : ''}
        <div class="popup-body">
          <span class="place-card-category category-${place.category}">${categoryName}</span>
          <div class="popup-title">${title}</div>
          <div class="popup-loc">📍 ${city}, ${country}</div>
          <button class="btn btn-primary btn-sm" style="width: 100%" onclick="selectPlace('${place.id}')">
            ${window.i18n[currentLang].detailsHeading}
          </button>
        </div>
      </div>
    `;

    marker.bindPopup(popupHtml);

    marker.on('click', () => {
      highlightSidebarCard(place.id);
    });

    markerCluster.addLayer(marker);
    markersMap.set(place.id, marker);
  });
}

function updateAllMarkersTooltips() {
  renderMarkers();
}

// Filter logic
function getFilteredPlaces() {
  return allPlaces.filter(place => {
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

    const nestedBadge = (place.items && place.items.length > 0) ? `
      <span class="place-card-nested-badge">
        📦 ${place.items.length} ${dict.nestedObjectsBadge || 'аб’ектаў'}
      </span>
    ` : '';

    return `
      <div class="place-card ${selectedPlaceId === place.id ? 'active' : ''}" 
           id="card-${place.id}"
           onclick="selectPlace('${place.id}')">
        <img src="${thumb}" alt="${title}" class="place-card-thumb" loading="lazy">
        <div class="place-card-content">
          <div>
            <div class="place-card-title">${title}</div>
            <div class="place-card-meta">📍 ${city}, ${country}</div>
          </div>
          <div class="place-card-badges">
            <span class="place-card-category category-${place.category}">
              ${CATEGORY_ICONS[place.category] || ''} ${categoryName}
            </span>
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

  const heroImg = place.image ? `<img src="${place.image}" alt="${title}" class="detail-hero-img">` : '';

  const tagsHtml = (place.tags || []).map(t => `<span class="detail-tag">#${t}</span>`).join('');

  // Nested sub-items (artworks, graves, exhibits)
  let nestedItemsHtml = '';
  if (place.items && Array.isArray(place.items) && place.items.length > 0) {
    nestedItemsHtml = `
      <div class="nested-items-section">
        <strong style="font-size: 0.95rem; color: #0f172a;">${dict.nestedObjectsTitle || '🏛️ Укладзеныя аб’екты, творы і пахаванні:'}</strong>
        ${place.items.map(it => `
          <div class="nested-item-card">
            <div class="nested-item-title">${it.title}</div>
            <div class="nested-item-meta">
              ${it.author ? `<span class="nested-item-author-badge">🎨 ${it.author}</span>` : ''}
              ${it.person ? `<span class="nested-item-author-badge">🕯️ ${it.person}</span>` : ''}
              ${it.year ? `<span>📅 ${it.year}</span>` : ''}
            </div>
            ${it.description ? `<div class="nested-item-desc">${it.description}</div>` : ''}
            ${it.image ? `<img src="${it.image}" alt="${it.title}" class="nested-item-thumb" loading="lazy">` : ''}
          </div>
        `).join('')}
      </div>
    `;
  }

  // Categorized links (Wikipedia, background articles, catalog)
  const linksHtml = (place.links || []).map(l => {
    let icon = '🔗';
    const titleLower = (l.title || '').toLowerCase();
    if (titleLower.includes('вікіпедыя') || titleLower.includes('wikipedia') || titleLower.includes('википедия')) {
      icon = '🌐';
    } else if (titleLower.includes('артыкул') || titleLower.includes('статья') || titleLower.includes('article') || titleLower.includes('бэкграўнд')) {
      icon = '📖';
    } else if (titleLower.includes('музей') || titleLower.includes('галерэя') || titleLower.includes('сайт') || titleLower.includes('калекцыя')) {
      icon = '🏛️';
    }
    return `
      <a href="${l.url}" target="_blank" rel="noopener noreferrer" class="detail-link-item">
        <span class="link-icon">${icon}</span>
        <span class="link-text">${l.title}</span>
        <span class="link-arrow">↗</span>
      </a>
    `;
  }).join('');

  drawer.innerHTML = `
    <div class="detail-header-actions">
      <button class="btn btn-secondary btn-sm" onclick="closePlaceDetail()">
        ← ${dict.sidebarTitle}
      </button>
      <button class="btn btn-secondary btn-sm" onclick="copyCurrentShareLink()">
        📋 ${dict.btnCopyLink}
      </button>
    </div>
    ${heroImg}
    <div class="detail-body">
      <span class="place-card-category category-${place.category}">
        ${CATEGORY_ICONS[place.category] || ''} ${categoryName}
      </span>
      <h2 class="detail-title">${title}</h2>
      <div class="detail-location">
        📍 <strong>${city}, ${country}</strong> &bull; <code>${lat.toFixed(4)}, ${lng.toFixed(4)}</code>
      </div>
      <div class="detail-description">
        ${desc}
      </div>

      ${nestedItemsHtml}

      ${tagsHtml ? `<div><strong>${dict.tagsHeading}:</strong><div class="detail-tags" style="margin-top:0.35rem">${tagsHtml}</div></div>` : ''}
      
      <div class="detail-actions-row">
        <a href="https://www.google.com/maps/search/?api=1&query=${lat},${lng}" 
           target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
          🗺️ ${dict.btnOpenGoogleMaps}
        </a>
        <a href="https://www.openstreetmap.org/?mlat=${lat}&mlon=${lng}#map=16/${lat}/${lng}" 
           target="_blank" rel="noopener noreferrer" class="btn btn-secondary btn-sm">
          🧭 ${dict.btnOpenOSM}
        </a>
      </div>

      ${linksHtml ? `
        <div style="margin-top: 0.5rem;">
          <strong style="font-size: 0.85rem; color: #1e293b;">${dict.sourcesHeading}:</strong>
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

// Check url hash on load
function checkUrlHash() {
  const hash = window.location.hash;
  if (hash.startsWith('#place=')) {
    const id = hash.replace('#place=', '');
    if (allPlaces.some(p => p.id === id)) {
      setTimeout(() => selectPlace(id, false), 300);
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

// Global scope exposures for inline onclick handlers
window.selectPlace = selectPlace;
window.closePlaceDetail = closePlaceDetail;
window.copyCurrentShareLink = copyCurrentShareLink;
window.openModal = openModal;
window.closeModal = closeModal;
