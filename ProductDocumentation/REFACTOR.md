# Project Refactor: Enterprise Web Application Structure

**Status:** 📋 PLANNING  
**Target Duration:** 2-3 development sessions  
**Estimated Effort:** 8-12 hours total  
**Created:** January 3, 2026  
**Priority:** HIGH - Prerequisite for React/Node.js migration

---

## 0. Business Context & Vision

### Why Refactor Now?
The project has grown from a simple static HTML page to a feature-rich application (1,916 lines in a single file). Before adding more features or migrating to React + Node.js, we need a clean foundation.

### Current Pain Points
1. **Monolithic File:** `index.html` contains ~1,000 lines of CSS, ~870 lines of JavaScript, and HTML all in one file
2. **Hard to Maintain:** Finding and editing specific code requires scrolling through nearly 2,000 lines
3. **No Code Reuse:** Can't share styles or utilities across pages (e.g., `privacy-policy.html`)
4. **Not Framework-Ready:** React/Vue require modular JS; current structure doesn't support that
5. **Root Level Clutter:** Python scripts, data files, and app files all mixed in root directory

### Target Architecture
A clean separation that mirrors professional web applications and sets us up for React + Node.js:

```
NailPolishInventory/
├── src/                    # All application source code
│   ├── css/               # Stylesheets
│   │   ├── variables.css  # Design tokens (colors, spacing, typography)
│   │   ├── base.css       # Reset, global styles
│   │   ├── components.css # Reusable components (buttons, cards, filters)
│   │   ├── layout.css     # Page structure, grid, navigation
│   │   └── animations.css # Keyframes, transitions
│   ├── js/                # JavaScript modules
│   │   ├── main.js        # App initialization, orchestration
│   │   ├── storage.js     # localStorage utilities (favorites, next appt)
│   │   ├── filters.js     # Filter logic and UI
│   │   ├── gallery.js     # Card creation, grid management
│   │   └── data.js        # CSV loading, parsing
│   └── pages/             # HTML pages
│       ├── index.html     # Main gallery page (minimal - just structure)
│       └── privacy-policy.html
├── public/                 # Static assets (served as-is)
│   └── images/            # Polish images
├── data/                   # Data files
│   └── polishes.csv       # Polish inventory data
├── scripts/                # Development/utility scripts (not shipped)
│   ├── mirror_images.py
│   └── fix_colors_accurate.py
├── docs/                   # Documentation
│   ├── ROADMAP.md
│   ├── TICKETS.md
│   └── ...
└── [config files]          # package.json, .gitignore, README.md
```

### Success Criteria
- [ ] All existing functionality works exactly as before
- [ ] CSS in separate files, organized by purpose
- [ ] JavaScript in separate files, organized by feature
- [ ] HTML files are minimal (structure only, <100 lines each)
- [ ] Easy to locate any piece of code
- [ ] Ready for React migration (modular JS structure)
- [ ] Ready for Node.js backend (clear separation of concerns)

---

## 1. Current State Analysis

### 1.1 File Inventory

| File | Lines | Purpose | Action |
|------|-------|---------|--------|
| `index.html` | 1,916 | Main app (CSS + JS + HTML) | **SPLIT** into modules |
| `privacy-policy.html` | ~400 | Privacy policy page | Move to `src/pages/` |
| `polishes.csv` | ~65 | Polish data | Move to `data/` |
| `images/` | ~60 files | Polish images | Move to `public/images/` |
| `helpers/*.py` | ~5 files | Python utilities | Move to `scripts/` |
| `ProductDocumentation/` | ~10 files | Documentation | Move to `docs/` |
| Root Python files | 5 files | One-off scripts | Move to `scripts/` |
| `public/` | Empty? | Leftover folder | Remove if empty |
| `reference/` | Various | Reference materials | Keep gitignored |

### 1.2 index.html Breakdown

| Section | Lines | Content |
|---------|-------|---------|
| Head (meta, fonts) | 1-10 | Document setup |
| **CSS (style tag)** | 11-1008 | ~1,000 lines of styles |
| HTML Body | 1009-1077 | ~70 lines of structure |
| **JavaScript (script tag)** | 1078-1916 | ~840 lines of code |

### 1.3 CSS Analysis (Lines 11-1008)

| Section | Approx Lines | Target File |
|---------|--------------|-------------|
| Design System Variables | 11-100 | `variables.css` |
| Reset/Base Styles | 100-150 | `base.css` |
| Layout (container, nav) | 150-350 | `layout.css` |
| Filter Components | 350-600 | `components.css` |
| Card/Grid Components | 600-800 | `components.css` |
| Animations/Effects | 800-900 | `animations.css` |
| Responsive/Media Queries | 900-1008 | `layout.css` |

### 1.4 JavaScript Analysis (Lines 1078-1916)

| Section | Approx Lines | Target File |
|---------|--------------|-------------|
| DOM References | 1078-1110 | `main.js` |
| State Variables | 1110-1130 | `main.js` |
| localStorage Utilities | 1130-1230 | `storage.js` |
| CSV Parsing | 1230-1350 | `data.js` |
| Filter Logic | 1350-1550 | `filters.js` |
| Card Creation | 1550-1700 | `gallery.js` |
| Event Listeners | 1700-1850 | `main.js` |
| Initialization | 1850-1916 | `main.js` |

---

## 2. Technical Approach

### 2.1 Module System Strategy

**For This Refactor (No Build Tools):**
- Use multiple `<script>` tags in order of dependency
- Use global scope carefully with namespacing (e.g., `window.NailPolish = {}`)
- CSS loaded via multiple `<link>` tags

**Future (React Migration):**
- ES6 modules with import/export
- Bundler (Vite) handles dependencies
- CSS modules or styled-components

### 2.2 File Loading Order

```html
<!-- CSS - Order matters for cascading -->
<link rel="stylesheet" href="../css/variables.css">
<link rel="stylesheet" href="../css/base.css">
<link rel="stylesheet" href="../css/layout.css">
<link rel="stylesheet" href="../css/components.css">
<link rel="stylesheet" href="../css/animations.css">

<!-- JS - Order matters for dependencies -->
<script src="../js/storage.js"></script>    <!-- No dependencies -->
<script src="../js/data.js"></script>       <!-- No dependencies -->
<script src="../js/filters.js"></script>    <!-- Depends on storage -->
<script src="../js/gallery.js"></script>    <!-- Depends on storage, data -->
<script src="../js/main.js"></script>       <!-- Orchestrates everything -->
```

### 2.3 JavaScript Module Pattern

Each JS file will expose its functions via a namespace:

```javascript
// storage.js
window.NailPolish = window.NailPolish || {};
window.NailPolish.storage = {
  getPolishId: function(number, name) { ... },
  getStoredList: function(key) { ... },
  saveStoredList: function(key, list) { ... },
  toggleInList: function(key, polishId) { ... },
  isInList: function(key, polishId) { ... }
};

// Usage in other files:
const { getPolishId, isInList } = window.NailPolish.storage;
```

### 2.4 Path Strategy

With files in `src/pages/`, relative paths change:

| Resource | From `index.html` | New Path |
|----------|-------------------|----------|
| CSS files | N/A (inline) | `../css/filename.css` |
| JS files | N/A (inline) | `../js/filename.js` |
| Images | `images/` | `../../public/images/` |
| CSV data | `polishes.csv` | `../../data/polishes.csv` |

---

## 3. Implementation Phases

### Phase 1: Directory Structure (30 min)
**Goal:** Create folder structure, move non-code files

**Tasks:**
- [ ] Create `src/css/`, `src/js/`, `src/pages/` directories
- [ ] Create `public/` directory
- [ ] Create `data/` directory  
- [ ] Create `scripts/` directory
- [ ] Move `images/` → `public/images/`
- [ ] Move `polishes.csv` → `data/polishes.csv`
- [ ] Move `*.py` scripts → `scripts/`
- [ ] Move `helpers/*` → `scripts/`
- [ ] Move `ProductDocumentation/` → `docs/`
- [ ] Remove empty `public/` if leftover from previous attempt
- [ ] Update `.gitignore` paths if needed

**Verification:** 
- Directory structure matches target
- No broken file references yet (we haven't moved HTML)

---

### Phase 2: Extract CSS (1-2 hours)
**Goal:** Split CSS into logical files

**Files to Create:**

#### 2.1 `src/css/variables.css`
- All CSS custom properties (`:root { ... }`)
- Design tokens: colors, spacing, typography, shadows, transitions
- ~90 lines

#### 2.2 `src/css/base.css`
- CSS reset / normalize
- `*, *::before, *::after` rules
- `html`, `body` base styles
- ~50 lines

#### 2.3 `src/css/layout.css`
- `.container` styles
- `.nav-header`, `.nav-content`, `.nav-links` styles
- `.grid` layout
- All `@media` responsive breakpoints
- ~200 lines

#### 2.4 `src/css/components.css`
- `.filter-bar`, `.filter-group`, `.filter-options` styles
- `.filter-option` checkbox/label styles
- Color filter background colors
- `.card`, `.card-link`, `.card-img`, `.card-body` styles
- `.card-icons`, `.icon-btn`, `.favorite-btn`, `.nextappt-btn` styles
- Button styles (`.btn-clear-filters`)
- ~400 lines

#### 2.5 `src/css/animations.css`
- `@keyframes` definitions (shimmer, catEyeStripe, moodGradient, sheerGlow, sparkle)
- `.finish-*` effect classes
- Transition utilities
- ~150 lines

**Verification:**
- Create a test HTML that loads all CSS files
- Visually compare to current site
- All colors, spacing, effects identical

---

### Phase 3: Extract JavaScript (2-3 hours)
**Goal:** Split JavaScript into logical modules

**Files to Create:**

#### 3.1 `src/js/storage.js` (~100 lines)
```javascript
/**
 * LocalStorage utilities for personalization features
 * Handles: favorites, next appointment selections
 */
window.NailPolish = window.NailPolish || {};
window.NailPolish.storage = {
  KEYS: {
    FAVORITES: 'nailpolish_favorites',
    NEXT_APPT: 'nailpolish_nextappt'
  },
  getPolishId: function(number, name) { ... },
  getStoredList: function(key) { ... },
  saveStoredList: function(key, list) { ... },
  toggleInList: function(key, polishId) { ... },
  isInList: function(key, polishId) { ... }
};
```

#### 3.2 `src/js/data.js` (~150 lines)
```javascript
/**
 * Data loading and parsing utilities
 * Handles: CSV fetch, parsing, validation
 */
window.NailPolish = window.NailPolish || {};
window.NailPolish.data = {
  CSV_PATH: '../../data/polishes.csv',
  parseCSV: function(text) { ... },
  loadPolishes: async function() { ... },
  // Color and finish constants
  COLORS: ['Red', 'Pink', 'Orange', ...],
  FINISHES: ['Cream', 'Shimmer', 'Cat Eye', ...]
};
```

#### 3.3 `src/js/filters.js` (~200 lines)
```javascript
/**
 * Filter logic and UI management
 * Handles: color filters, finish filters, personal filters, clear all
 */
window.NailPolish = window.NailPolish || {};
window.NailPolish.filters = {
  state: {
    selectedColors: new Set(),
    selectedFinishes: new Set(),
    showFavorites: false,
    showNextAppt: false
  },
  applyFilters: function() { ... },
  updateFilterControls: function() { ... },
  clearAllFilters: function() { ... },
  createColorFilters: function(container) { ... },
  createFinishFilters: function(container) { ... },
  setupEventListeners: function() { ... }
};
```

#### 3.4 `src/js/gallery.js` (~200 lines)
```javascript
/**
 * Gallery/card management
 * Handles: card creation, grid updates, image handling
 */
window.NailPolish = window.NailPolish || {};
window.NailPolish.gallery = {
  gridElement: null,
  allPolishes: [],
  createCard: function(polish) { ... },
  renderGallery: function(polishes) { ... },
  updateCardIcons: function(polishId) { ... },
  getImagePath: function(polish) { ... }
};
```

#### 3.5 `src/js/main.js` (~100 lines)
```javascript
/**
 * Application entry point
 * Orchestrates initialization and ties modules together
 */
(function() {
  'use strict';
  
  const { storage, data, filters, gallery } = window.NailPolish;
  
  async function initializeApp() {
    // 1. Load data
    const polishes = await data.loadPolishes();
    gallery.allPolishes = polishes;
    
    // 2. Setup filters
    filters.createColorFilters(document.getElementById('color-filters'));
    filters.createFinishFilters(document.getElementById('finish-filters'));
    filters.setupEventListeners();
    
    // 3. Render gallery
    gallery.renderGallery(polishes);
    
    // 4. Apply initial filters (none)
    filters.applyFilters();
  }
  
  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', initializeApp);
})();
```

**Verification:**
- All console.log statements work
- Favorites toggle works
- Filters work (color, finish, personal)
- Clear All works
- Data loads and displays

---

### Phase 4: Update HTML Files (1 hour)
**Goal:** Create minimal HTML files with external references

#### 4.1 `src/pages/index.html` (Target: <100 lines)
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Studio Claire - Browse my nail polish collection">
  <title>Studio Claire</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  
  <!-- Stylesheets -->
  <link rel="stylesheet" href="../css/variables.css">
  <link rel="stylesheet" href="../css/base.css">
  <link rel="stylesheet" href="../css/layout.css">
  <link rel="stylesheet" href="../css/components.css">
  <link rel="stylesheet" href="../css/animations.css">
</head>
<body>
  <!-- Navigation -->
  <nav class="nav-header">...</nav>
  
  <!-- Main Content -->
  <div class="container">
    <div class="filter-bar">...</div>
    <div class="grid"></div>
  </div>
  
  <!-- Scripts -->
  <script src="../js/storage.js"></script>
  <script src="../js/data.js"></script>
  <script src="../js/filters.js"></script>
  <script src="../js/gallery.js"></script>
  <script src="../js/main.js"></script>
</body>
</html>
```

#### 4.2 Update `privacy-policy.html`
- Move to `src/pages/`
- Update any relative paths
- Could share base CSS if needed

**Verification:**
- Site loads from `src/pages/index.html`
- All functionality works
- Privacy policy page works
- Images load correctly

---

### Phase 5: Update Development Workflow (30 min)
**Goal:** Update serving and documentation

**Tasks:**
- [ ] Update README with new structure and commands
- [ ] Update STANDUP.md with new file locations
- [ ] Test local server: `python -m http.server 8000` from root
- [ ] Verify paths work: `http://localhost:8000/src/pages/index.html`
- [ ] Consider adding npm scripts for serving (future)

**New Quick Start:**
```bash
# Development
cd NailPolishInventory
python -m http.server 8000
# Open http://localhost:8000/src/pages/index.html
```

---

### Phase 6: Cleanup & Verification (30 min)
**Goal:** Remove old files, final testing

**Tasks:**
- [ ] Delete old `index.html` from root (after confirming new one works)
- [ ] Remove any duplicate/orphaned files
- [ ] Remove empty directories
- [ ] Full functionality test:
  - [ ] Gallery loads with all 60 polishes
  - [ ] Color filters work (single and multi-select)
  - [ ] Finish filters work
  - [ ] Favorites work (heart icon toggles, persists)
  - [ ] Next Appt works (calendar icon toggles, persists)
  - [ ] "My Picks" filters work
  - [ ] Clear All Filters works
  - [ ] Images load (local images)
  - [ ] Links to product pages work
  - [ ] Mobile responsive
- [ ] Git commit with clear message

---

## 4. Risk Mitigation

### 4.1 Rollback Strategy
- Keep original `index.html` until Phase 6 verification complete
- Use git branches: `refactor/file-structure`
- Commit after each phase

### 4.2 Common Issues

| Risk | Mitigation |
|------|------------|
| Path breaks after move | Test each phase incrementally |
| CSS cascade order wrong | Follow dependency order in head |
| JS load order wrong | Test each module independently |
| localStorage keys change | Keep exact same key names |
| Images don't load | Verify relative paths from new location |

### 4.3 What NOT to Change
- localStorage key names (`nailpolish_favorites`, `nailpolish_nextappt`)
- CSS class names (used by JS)
- HTML structure (IDs, classes)
- Any business logic
- Filter behavior (AND/OR logic)

---

## 5. Future Considerations

### 5.1 React Migration Path
After this refactor, React migration becomes straightforward:
- `storage.js` → custom hook `useLocalStorage`
- `data.js` → data fetching with `useEffect` or React Query
- `filters.js` → `FilterContext` with `useReducer`
- `gallery.js` → `<GalleryCard>` component
- CSS files → CSS modules or Tailwind

### 5.2 Node.js Backend Path
Clean separation enables backend addition:
- `data/polishes.csv` → PostgreSQL/MongoDB
- Add `server/` directory for Express.js
- API endpoints replace CSV fetch
- Could add user authentication for cross-device sync

### 5.3 Build Tool Integration (Vite)
Current structure supports easy Vite setup:
```
npm init vite@latest . -- --template react
```
- `src/` already exists
- Just need to convert JS to ES modules
- CSS files stay the same or convert to modules

---

## 6. Checklist Summary

### Pre-Flight
- [ ] Commit current working state
- [ ] Create feature branch `refactor/file-structure`

### Phase 1: Directory Structure
- [ ] Create all new directories
- [ ] Move static assets (images, data, scripts)
- [ ] Move documentation

### Phase 2: CSS Extraction
- [ ] Create `variables.css`
- [ ] Create `base.css`
- [ ] Create `layout.css`
- [ ] Create `components.css`
- [ ] Create `animations.css`
- [ ] Test CSS loads correctly

### Phase 3: JS Extraction
- [ ] Create `storage.js`
- [ ] Create `data.js`
- [ ] Create `filters.js`
- [ ] Create `gallery.js`
- [ ] Create `main.js`
- [ ] Test all functionality

### Phase 4: HTML Updates
- [ ] Create minimal `index.html`
- [ ] Update `privacy-policy.html`
- [ ] Test all pages

### Phase 5: Workflow Updates
- [ ] Update README
- [ ] Update STANDUP
- [ ] Test local development

### Phase 6: Cleanup
- [ ] Remove old files
- [ ] Full functionality test
- [ ] Git commit and merge

---

## 7. Time Estimates

| Phase | Estimated Time | Complexity |
|-------|---------------|------------|
| Phase 1: Directory Structure | 30 min | Low |
| Phase 2: CSS Extraction | 1-2 hours | Medium |
| Phase 3: JS Extraction | 2-3 hours | High |
| Phase 4: HTML Updates | 1 hour | Medium |
| Phase 5: Workflow Updates | 30 min | Low |
| Phase 6: Cleanup & Testing | 30 min | Low |
| **Total** | **6-8 hours** | - |

**Recommended Approach:** 
- Session 1: Phases 1-2 (Directory + CSS)
- Session 2: Phase 3 (JavaScript - most complex)
- Session 3: Phases 4-6 (HTML + Cleanup)

---

*Document created: January 3, 2026*  
*Status: Ready for implementation*  
*Next: Review plan, then execute Phase 1*
