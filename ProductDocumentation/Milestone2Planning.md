# Milestone 2: Personalization Features - Planning Document

**Status:** ✅ COMPLETE  
**Target Duration:** Weeks 4-6  
**Actual Duration:** ~3.5 hours (same day implementation)  
**Estimated Effort:** 4 story points (simplified from original 42)  
**Last Updated:** January 3, 2026  
**Completion Date:** January 3, 2026

---

## 0. User Context & Use Case

### Who Uses This Site?
**Primary Users:** Nail salon clients  
**Site Owner:** Nail artist (Studio Claire)

### The Scenario
- The nail artist owns all 60+ polishes shown on this site
- Clients browse the collection to see what colors are available
- Clients use their personal phones to browse (mobile-first)
- When clients find colors they love, they can save them for reference
- Before appointments, clients can mark which colors they want to try

### Key Insight
**Clients don't own these polishes** - they're selecting from the artist's collection. This is more like "picking from a menu" than "tracking personal inventory."

### Personalization Features Needed
1. **Favorites:** General "I love this color" - polishes they find beautiful
   - Icon: Heart ♡/♥
   - Filter label: "My Favorites"
   
2. **Next Appt:** Specific "Use this on my next visit" - appointment planning
   - Icon: Calendar 📅
   - Filter label: "My Next Appt"

---

## 1. Executive Summary

### 1.1 Goal
Enable clients to personalize their browsing experience by marking favorite colors and selecting polishes for their next appointment—all without requiring login or external services.

### 1.2 Key Decision: SIMPLE Approach
We're using **localStorage** for all personalization data. This means:
- ✅ Zero backend infrastructure
- ✅ No authentication system
- ✅ Works offline
- ✅ Instant implementation
- ⚠️ Data is device/browser-specific (no cross-device sync)
- ⚠️ Data can be lost if user clears browser data

### 1.3 Success Criteria
- [ ] Client can favorite polishes with a single click (heart icon)
- [ ] Client can mark polishes for next appointment (calendar icon)
- [ ] Client can filter gallery by "My Favorites" and "My Next Appt"
- [ ] All personalization persists across browser sessions
- [ ] UI is intuitive and doesn't clutter the existing design
- [ ] Works perfectly on mobile (primary use case)
- [ ] Performance remains snappy (no perceptible lag)

---

## 2. Business Context

### 2.1 User Stories

**As a client, I want to...**

1. **Save favorites** so I can remember polishes I love
   - Click a heart icon to toggle favorite status
   - See at a glance which polishes are my favorites
   - Filter to show only favorites
   - Build a collection of colors I generally love

2. **Mark polishes for my next appointment** so I remember what to request
   - Mark specific polishes I want to try next visit
   - See which ones I've selected for next time
   - Filter to see just my "next appointment" picks
   - Show my nail artist what I'm thinking

3. **Keep my selections** so I don't lose my choices
   - Data persists when I close the browser
   - Data persists when I return days/weeks later
   - Data survives page refreshes
   - Works on my phone

### 2.2 Non-Goals (Out of Scope)
- Cross-device synchronization (each client uses their own phone)
- Client accounts/profiles
- Sharing selections with other clients
- Import/export functionality (could be future enhancement)
- Predefined seasonal collections (deferred - adds CSV complexity)
- Tracking which polishes client has actually used in past appointments (future feature)

---

## 3. Technical Architecture

### 3.1 Storage Strategy: localStorage

```javascript
// Data Structure
{
  "nailpolish_favorites": ["781-Air of Mint", "769-Ruby Ritz", "920-Cashmere"],     // Array of composite IDs (number-name)
  "nailpolish_nextappt": ["427-Beach Babe", "729-Aloha", "112-Pink Smoothie"]       // Array of composite IDs for next visit
  // TODO: Rename "nextappt" key once we decide on better feature name
}
```

**Why Composite Keys (number-name)?**
- **CRITICAL:** Polish numbers alone are NOT unique in the dataset
- Combining number + name creates a unique identifier
- Both values are stable (won't change)
- Human-readable for debugging
- No need to generate/maintain arbitrary IDs
- Format: `"number-name"` (e.g., "781-Air of Mint")

**Key Naming Convention:** Prefix with `nailpolish_` to avoid conflicts with other localStorage data.

### 3.2 Core Functions Needed

```javascript
// ============ STORAGE LAYER ============

/**
 * Create composite key from polish data
 * @param {string} number - Polish number (e.g., "781")
 * @param {string} name - Polish name (e.g., "Air of Mint")
 * @returns {string} Composite key (e.g., "781-Air of Mint")
 */
function getPolishId(number, name) {
  return `${number}-${name}`;
}

/**
 * Get array from localStorage
 * @param {string} key - Storage key (favorites|nextappt)
 * @returns {string[]} Array of polish composite IDs (number-name)
 */
function getStoredList(key) {
  const data = localStorage.getItem(`nailpolish_${key}`);
  return data ? JSON.parse(data) : [];
}

/**
 * Save array to localStorage
 * @param {string} key - Storage key
 * @param {string[]} list - Array of polish composite IDs
 */
function saveStoredList(key, list) {
  localStorage.setItem(`nailpolish_${key}`, JSON.stringify(list));
}

/**
 * Toggle item in stored list
 * @param {string} key - Storage key
 * @param {string} polishId - Polish composite ID (number-name)
 * @returns {boolean} New state (true = in list, false = removed)
 */
function toggleInList(key, polishId) {
  const list = getStoredList(key);
  const index = list.indexOf(polishId);
  
  if (index > -1) {
    list.splice(index, 1);
    saveStoredList(key, list);
    return false;
  } else {
    list.push(polishId);
    saveStoredList(key, list);
    return true;
  }
}

/**
 * Check if item is in stored list
 * @param {string} key - Storage key
 * @param {string} polishId - Polish composite ID to check
 * @returns {boolean}
 */
function isInList(key, polishId) {
  return getStoredList(key).includes(polishId);
}
```

### 3.3 UI Components Needed

#### 3.3.1 Card Overlay Icons
Each polish card needs interactive icons:

```
┌─────────────────────┐
│  [♡]            [📅] │  ← Top right: Heart (favorite), Calendar (next appt)
│                     │
│      [IMAGE]        │
│                     │
│  427                │
│  Air of Mint        │
└─────────────────────┘
```

**Icon Layout: Heart + Calendar**
- Heart icon (left): Toggle favorite
- Calendar icon (right): Toggle "next appt" status
- Both icons visible on hover, always visible if active

#### 3.3.2 Filter Section Addition
Add new filter group for personalization:

```
┌─ Color Family ────────────────────────────┐
│ [Red] [Pink] [Orange] [Yellow] [Green]... │
└───────────────────────────────────────────┘

┌─ Finish Type ─────────────────────────────┐
│ [Cream] [Shimmer] [Cat Eye] [Glitter]...  │
└───────────────────────────────────────────┘

┌─ My Picks ────────────────────────────────┐  ← NEW
│ [♡ My Favorites] [📅 My Next Appt]        │
└───────────────────────────────────────────┘
```

### 3.4 Filter Logic Integration

Current filter logic: `(matchesColor OR noColorSelected) AND (matchesFinish OR noFinishSelected)`

New logic: `... AND (matchesPersonal OR noPersonalSelected)`

```javascript
// Pseudocode for combined filtering
function shouldShowCard(card) {
  const matchesColor = selectedColors.size === 0 || 
    cardColors.some(c => selectedColors.has(c));
  
  const matchesFinish = selectedFinishes.size === 0 || 
    selectedFinishes.has(cardFinish);
  
  // Create composite ID from card data
  const polishId = getPolishId(card.number, card.name);
  
  const matchesPersonal = selectedPersonal.size === 0 ||
    (selectedPersonal.has('favorites') && isInList('favorites', polishId)) ||
    (selectedPersonal.has('nextappt') && isInList('nextappt', polishId));
  
  return matchesColor && matchesFinish && matchesPersonal;
}
```

---

## 4. Implementation Plan

### Phase 1: Storage Foundation (30 min)
**Goal:** Create localStorage utility functions

- [ ] Add storage functions to index.html (getStoredList, saveStoredList, toggleInList, isInList)
- [ ] Add initialization on page load to read stored data
- [ ] Test in browser console: manually add/remove items
- [ ] Verify data persists after page refresh

**Acceptance Test:**
```javascript
// In browser console:
const testId = getPolishId('781', 'Air of Mint');
toggleInList('favorites', testId);  // Should return true
isInList('favorites', testId);      // Should return true
// Refresh page
isInList('favorites', testId);      // Should still return true
```

### Phase 2: Favorite Hearts (1 hour)
**Goal:** Add clickable heart icons to cards

- [ ] Add heart icon HTML to createCard() function
- [ ] Style heart icon (positioned top-right, subtle until hover)
- [ ] Add click handler to toggle favorite (use getPolishId to create composite key)
- [ ] Visual feedback: filled heart when favorited, outline when not
- [ ] Initialize heart state on card creation (check localStorage with composite ID)
- [ ] Prevent heart click from triggering card link

**CSS States:**
```css
.favorite-btn { /* default: outline heart */ }
.favorite-btn.active { /* filled heart, maybe red/pink */ }
.favorite-btn:hover { /* highlight effect */ }
```

**Key Considerations:**
- Heart should be visible on hover, always visible if favorited
- Click should not navigate to product page
- Animation on toggle (subtle scale or color transition)

### Phase 3: Next Appointment Picks (45 min)
**Goal:** Add calendar icon to cards for "Next Appt" feature

- [ ] Add calendar icon HTML to createCard() (positioned near heart)
- [ ] Style calendar icon (visible on hover, always visible if active)
- [ ] Add click handler to toggle next appointment status (use getPolishId for composite key)
- [ ] Visual states: default (outline calendar), active (filled/colored calendar)
- [ ] Initialize icon state on card creation (check localStorage with composite ID)
- [ ] Prevent icon click from triggering card link
- [ ] Polish can be both favorite AND next appt pick (both icons can be active)

### Phase 4: Personal Filters (45 min)
**Goal:** Add filter buttons for Favorites and Next Appointment picks

- [ ] Add new filter group HTML ("My Picks" or similar)
- [ ] Style filter buttons (consistent with existing filters)
- [ ] Add filter state tracking (selectedPersonal Set)
- [ ] Integrate with applyFilters() function
- [ ] Update handleFilterChange for personal filters
- [ ] Ensure "Clear All Filters" resets personal filters too

**Filter Button Design:**
- Should visually match color/finish filter style
- Two filters: ♡ My Favorites + 📅 My Next Appt
- Badge showing count (e.g., "My Favorites (5)") - helpful for clients
- Placed BEFORE color filters (most personal/important) for mobile users

### Phase 5: Polish & Mobile Testing (30 min)
**Goal:** Handle edge cases and ensure mobile works perfectly

- [ ] Empty state messages for each filter ("No favorites yet - tap ♡ on polishes you love!", "No polishes selected yet - tap 📅 to pick for your next visit!")
- [ ] Hover states and transitions for all interactive elements
- [ ] Mobile touch targets (minimum 44x44px - CRITICAL)
- [ ] Test on actual mobile phone (primary use case)
- [ ] Test touch interactions: tap heart, tap next appt icon
- [ ] Ensure icons don't accidentally trigger card navigation
- [ ] Performance check: ensure no lag with 60 polishes
- [ ] Keyboard accessibility for desktop users (Tab to reach icons)

---

## 5. UI/UX Design Details

### 5.1 Heart Icon Design

**Placement:** Top-right corner of card, overlaid on image

**States:**
| State | Icon | Color | Visibility |
|-------|------|-------|------------|
| Default | ♡ (outline) | Gray/transparent | On hover only |
| Hovered | ♡ (outline) | Pink | Visible |
| Favorited | ♥ (filled) | Pink/Red | Always visible |
| Favorited + Hovered | ♥ (filled) | Darker pink | Always visible |

**Animation:** 
- Subtle scale (1.0 → 1.2 → 1.0) on toggle
- Color transition (0.2s ease)

### 5.2 Calendar Icon Design (Next Appt)

**Layout: Two Icons Top-Right**
```
┌─────────────────────┐
│ [♡]  [📅]           │  ← Heart (favorite) + Calendar (next appt)
│      [IMAGE]        │
│                     │
│  427                │
│  Air of Mint        │
└─────────────────────┘
```

**States:**
| State | Icon | Color | Visibility |
|-------|------|-------|------------|
| Default | 📅 (outline) | Gray/transparent | On hover only |
| Hovered | 📅 (outline) | Blue/accent | Visible |
| Active | 📅 (filled) | Blue/accent | Always visible |
| Active + Hovered | 📅 (filled) | Darker blue | Always visible |

**Icon Spacing:**
- 8-12px gap between heart and calendar icon
- Each icon ~32x32px minimum for mobile touch targets
- Icons fade in on hover (desktop) or always visible (mobile)

### 5.3 Filter Section Design

```
┌─ My Picks ─────────────────────────────────────────────┐
│                                                        │
│  [♡ My Favorites (3)]  [📅 My Next Appt (2)]          │
│                                                        │
└────────────────────────────────────────────────────────┘
```

- Show count in parentheses (helpful for clients to see how many they've picked)
- Same visual style as existing filters
- Placed BEFORE color filters (most important for mobile users)
- Section title: "My Picks"
- Two filters: "My Favorites" + "My Next Appt"

---

## 6. Data Considerations

### 6.1 localStorage Limits
- localStorage limit: ~5-10MB per origin
- Our data: ~2-3KB maximum (60 composite IDs × ~30 chars each × 2 lists)
- **Verdict:** No concerns

### 6.2 Data Integrity
```javascript
// Defensive loading - handle corrupted data
function getStoredList(key) {
  try {
    const data = localStorage.getItem(`nailpolish_${key}`);
    if (!data) return [];
    const parsed = JSON.parse(data);
    // Validate it's an array of strings
    if (!Array.isArray(parsed)) return [];
    return parsed.filter(item => typeof item === 'string');
  } catch (e) {
    console.warn(`Failed to load ${key} from localStorage:`, e);
    return [];
  }
}
```

### 6.3 Future: Export/Import (Out of Scope)
If we ever want cross-device support without a backend:
```javascript
// Future enhancement - not for M2
function exportData() {
  return JSON.stringify({
    favorites: getStoredList('favorites'),
    nextappt: getStoredList('nextappt'),
    exportedAt: new Date().toISOString()
  });
}

function importData(jsonString) {
  const data = JSON.parse(jsonString);
  saveStoredList('favorites', data.favorites || []);
  saveStoredList('nextappt', data.nextappt || []);
}
```

---

## 7. Testing Plan

### 7.1 Manual Test Cases

#### Storage Tests
- [ ] Add item to favorites → verify in localStorage
- [ ] Remove item from favorites → verify removed from localStorage
- [ ] Refresh page → favorites persist
- [ ] Close browser, reopen → favorites persist
- [ ] Clear localStorage → favorites cleared (expected)

#### UI Tests
- [ ] Click heart → heart fills
- [ ] Click filled heart → heart empties
- [ ] Favorited polish shows filled heart on page load
- [ ] Click next appt icon → icon activates
- [ ] Click active next appt icon → icon deactivates
- [ ] Selected next appt polish shows active icon on page load
- [ ] Icon clicks don't navigate to product page
- [ ] Both icons work on mobile (44x44px touch targets)
- [ ] Icons visible on hover (desktop) or always visible if active (mobile)

#### Filter Tests
- [ ] Click "Favorites" filter → only favorites show
- [ ] Click "Next Appt" filter → only next appointment picks show
- [ ] Combine: "Favorites" + "Red" → red favorites only
- [ ] Combine: "Next Appt" + "Shimmer" → shimmer polishes for next appt
- [ ] "Clear All Filters" clears personal filters too
- [ ] Filter buttons show counts that match stored data
- [ ] Counts update immediately when icons are clicked

#### Edge Cases
- [ ] No favorites yet → filter shows "No favorites yet - tap the heart on polishes you love!" message
- [ ] No next appt picks → filter shows appropriate empty state
- [ ] Add favorite while filtered → card appears/updates
- [ ] Remove favorite while "Favorites" filter active → card hides
- [ ] Polish in both favorites AND next appt → shows in both filter views
- [ ] Rapidly clicking icons doesn't cause UI glitches
- [ ] Works offline (localStorage doesn't require network)

### 7.2 Browser Testing
- [ ] Chrome (primary)
- [ ] Firefox
- [ ] Safari (if available)
- [ ] Mobile Chrome
- [ ] Mobile Safari

---

## 8. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| User clears browser data | Loses all personalization | Low | Consider future export feature |
| localStorage disabled | Feature won't work | Very Low | Detect and show warning |
| Performance with many favorites | Slow filtering | Low | Current 60 polishes is fine; optimize if >500 |
| UI clutter with icons | Harder to browse | Medium | Keep icons subtle, only prominent when active |
| Mobile tap targets too small | Frustrating UX | Medium | Enforce 44x44px minimum |

---

## 9. Timeline

| Phase | Task | Estimate | Dependencies |
|-------|------|----------|--------------|
| 1 | Storage Foundation | 30 min | None |
| 2 | Favorite Hearts | 1 hour | Phase 1 |
| 3 | Next Appointment Icon | 45 min | Phase 1, naming decision |
| 4 | Personal Filters | 45 min | Phases 2, 3 |
| 5 | Polish & Mobile Testing | 30 min | Phase 4 |
| - | **Total** | **~3.5 hours** | - |
- After Phase 5: Ready for production

---

## 10. Open Questions / TODOs

### Design Decisions (RESOLVED)
- [x] **Feature Name:** "Next Appt" (calendar icon 📅)
- [x] **Filter Labels:** "My Favorites" and "My Next Appt"
- [x] **Filter Section Title:** "My Picks"
- [x] **Can a polish be both?** YES - polish can be favorited AND marked for next appt

### Implementation Details To Confirm
- [ ] **Icon Visibility:** Always visible on mobile, or only on hover? (Suggest: hover on desktop, always if active)
- [ ] **Empty State Messages:** Finalize exact wording during Phase 5

### Research Tasks
- [ ] Check existing CSS for icon styling patterns
- [ ] Review mobile card layout for icon placement space
- [ ] Test touch target sizes on actual mobile device

### Future Considerations (Not M2)
- [ ] Export/import for cross-device
- [ ] Seasonal collections (would need CSV column)
- [ ] "Recently viewed" list
- [ ] Polish comparison feature

---

## 11. File Changes Summary

### index.html
- Add storage utility functions (JavaScript) including getPolishId() helper
- Modify createCard() to add heart icon and next appointment controls
- Add new filter group HTML for "My Picks"
- Add CSS for new UI elements
- Modify applyFilters() to include personal filters
- Use composite keys (number-name) for all storage operations

### No other files needed
- polishes.csv: No changes (we use Number + Name as composite key)
- No new files required
- No backend/API changes

---

## 12. Approval Checklist

Before starting implementation:
- [x] Review this document together
- [x] **DECIDED:** "Next Appt" with calendar icon 📅
- [x] **DECIDED:** Filter labels "My Favorites" and "My Next Appt"
- [x] **DECIDED:** Filter section title "My Picks"
- [x] Confirm mobile-first approach and touch target sizes (44x44px minimum)
- [x] Any questions or concerns addressed

**Ready to begin:** January 3, 2026

---

## 14. Implementation Summary

### ✅ All Phases Complete

**Phase 1: Storage Foundation (30 min)** ✅
- Added localStorage utility functions with error handling
- Composite ID system (number-name) for unique identification
- Functions: getPolishId, getStoredList, saveStoredList, toggleInList, isInList

**Phase 2: Favorite Hearts (1 hour)** ✅  
- Heart icon overlay on every card (❤️ filled / 🤍 outline)
- Click to toggle favorite status
- Persists to localStorage
- Icons visible on hover, always visible when active
- Prevents navigation when clicked

**Phase 3: Next Appointment Calendar Icon (45 min)** ✅  
- Calendar icon next to heart (📅 filled / 🗓️ outline)
- Click to toggle "next appointment" status
- Blue accent color differentiation
- Both icons can be active simultaneously

**Phase 4: Personal Filters (45 min)** ✅  
- "My Picks" filter group with matching visual style
- "❤️ My Favorites" filter button
- "📅 My Next Appt" filter button
- Works with AND logic alongside color/finish filters
- "Clear All Filters" includes personal filters

**Phase 5: Polish & Mobile Testing (30 min)** ✅  
- Empty state messages for each scenario
- Mobile-optimized touch targets (44x44px)
- Icon visibility rules (hover on desktop, visible when active)
- Smooth transitions and animations

### Final Implementation Details
- **Total Time:** ~3.5 hours (as estimated)
- **Files Modified:** index.html only
- **Lines Added:** ~200 lines (JS + CSS)
- **Storage Keys:** nailpolish_favorites, nailpolish_nextappt
- **Browser Compatibility:** All modern browsers with localStorage support

### What Was Simplified
- **Removed:** Authentication, backend, cross-device sync, ownership tracking
- **Kept:** Core personalization (favorites + next appointment)
- **Result:** Faster implementation, simpler maintenance, perfect for use case

---

*Document created: January 3, 2026*  
*Implementation completed: January 3, 2026*  
*Total duration: Same day*

### Key Changes from Initial Draft
- Removed all "ownership tracking" functionality (clients don't own polishes)
- Simplified to 2 features instead of 3: Favorites + Next Appointment picks
- Added user context section explaining nail salon use case
- Emphasized mobile-first approach (clients primarily use phones)
- Reduced timeline from 4 hours to 3.5 hours
- Added TODO for better feature naming

### Remember
- This is for CLIENTS browsing the nail artist's collection
- All polishes belong to the artist (Studio Claire)
- Clients are selecting "from the menu" not tracking personal inventory
- Mobile experience is CRITICAL

---

*Document created: January 3, 2026*  
*Last reviewed: [pending]*
