# Implementation Guide: NPI-005

## Ticket Information
**ID:** NPI-005  
**Title:** Add basic color filter  
**Points:** 3  
**Priority:** ⬆️ High  
**Tags:** `filter` `ui`

---

## Overview
Create a dropdown or chip-based color family filter that allows users to filter nail polishes by color family (reds, pinks, blues, neutrals, etc.).

---

## Acceptance Criteria
- [ ] User can see a color filter UI element on the main gallery page
- [ ] Filter includes major color families: Reds, Pinks, Oranges, Yellows, Greens, Blues, Purples, Browns, Neutrals, Blacks/Whites
- [ ] Selecting a color filters the displayed polishes in real-time
- [ ] Filter has a clear visual state (selected vs unselected)
- [ ] "All Colors" or reset option returns to showing all polishes
- [ ] Mobile-responsive design

---

## Prerequisites
- ✅ NPI-002: Mobile-first responsive grid layout exists
- ✅ NPI-003: CSV data is loaded into the gallery

---

## Technical Approach

### Data Requirements
1. Add a `color` or `colorFamily` field to the polish data structure
2. Categorize each polish into a color family

### UI Components
1. Filter control (dropdown or horizontal chip buttons)
2. Active filter indicator
3. Filtered results display

---

## Implementation Steps

### Step 1: Analyze Current Data Structure
**File:** `polishes.csv` or data source  
**Action:** Review current polish data to determine how to categorize by color

**Decision Point:** Do we need to add a new `ColorFamily` column to the CSV?
- If yes → Update CSV with color categories
- If no → Infer from polish names (less reliable)

### Step 2: Add Color Family Data
**File:** `polishes.csv`  
**Action:** Add a new column `ColorFamily` with values from this list:
- Red
- Pink
- Orange
- Yellow
- Green
- Blue
- Purple
- Brown
- Neutral
- Black
- White
- Multi

**Example:**
```csv
Number,Name,Link,Image Address,ColorFamily
19,Mood Change - Bridal Pink To Brighter Pink,https://...,https://...,Pink
67,Fire Engine Red,https://...,https://...,Red
```

### Step 3: Update HTML with Filter UI
**File:** `index.html`  
**Location:** After the `<h1>` and hint, before the grid

**Add Filter HTML:**
```html
<div class="filter-bar">
  <label for="color-filter" class="filter-label">Filter by Color:</label>
  <select id="color-filter" class="color-filter">
    <option value="">All Colors</option>
    <option value="Red">Reds</option>
    <option value="Pink">Pinks</option>
    <option value="Orange">Oranges</option>
    <option value="Yellow">Yellows</option>
    <option value="Green">Greens</option>
    <option value="Blue">Blues</option>
    <option value="Purple">Purples</option>
    <option value="Brown">Browns</option>
    <option value="Neutral">Neutrals</option>
    <option value="Black">Blacks</option>
    <option value="White">Whites</option>
  </select>
</div>
```

### Step 4: Add Filter Styling
**File:** `index.html`  
**Location:** Inside `<style>` section

**Add CSS:**
```css
.filter-bar {
  margin: 0 0 24px 0;
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}

.filter-label {
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.color-filter {
  padding: 8px 12px;
  font-size: 14px;
  border: 1px solid var(--border);
  border-radius: 8px;
  background: white;
  cursor: pointer;
  min-width: 150px;
}

.color-filter:focus {
  outline: 2px solid #4a90e2;
  outline-offset: 2px;
}

@media (max-width: 600px) {
  .filter-bar {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .color-filter {
    width: 100%;
  }
}
```

### Step 5: Add Color Family Attribute to Cards
**File:** `index.html`  
**Location:** Each `<a class="card">` element

**Modification:** Add a `data-color` attribute to each card:
```html
<a class="card" data-color="Pink" href="...">
```

**Implementation:** Update all 33 polish cards with appropriate color family values based on their actual colors.

### Step 6: Implement Filter JavaScript
**File:** `index.html`  
**Location:** Add `<script>` section before closing `</body>` tag

**Add JavaScript:**
```javascript
<script>
  // Get references to DOM elements
  const colorFilter = document.getElementById('color-filter');
  const cards = document.querySelectorAll('.card');
  
  // Add event listener to filter
  colorFilter.addEventListener('change', function() {
    const selectedColor = this.value;
    
    cards.forEach(card => {
      const cardColor = card.getAttribute('data-color');
      
      if (selectedColor === '' || cardColor === selectedColor) {
        // Show card
        card.style.display = 'block';
      } else {
        // Hide card
        card.style.display = 'none';
      }
    });
  });
</script>
```

### Step 7: Map Polishes to Color Families
**Manual Task:** Review each polish and assign color family

**Reference Guide:**
- **Red:** Fire Engine Red, Fire Brick, Cherry On Top
- **Pink:** Mood Change Pink, Little Piggy, Baby Girl
- **Orange:** Marigold, Apple Cider
- **Yellow:** Banana Crepe
- **Green:** Imperial Jade, Army Green, Air Of Mint
- **Blue:** Blue Violet, Blue De France, Blue Lake, Blossom Orchid (if blue-ish)
- **Purple:** Blossom Orchid (if purple-ish), Dream World
- **Brown:** Chestnut Cassette, Cedar Brown
- **Neutral:** With GRAYce, Clean Pallet, Biscuits N' Honey, California Grace, Dark Salmon
- **Other:** Ambrosia, Chartreux Cat, Chubby Himalayan, etc.

---

## Testing Checklist

### Functional Testing
- [ ] Filter dropdown appears on page
- [ ] Selecting "All Colors" shows all 33 polishes
- [ ] Selecting "Red" shows only red polishes
- [ ] Selecting each color family filters correctly
- [ ] Changing filter updates display immediately
- [ ] No console errors

### Visual Testing
- [ ] Filter looks good on desktop (1920px+)
- [ ] Filter looks good on tablet (768px)
- [ ] Filter looks good on mobile (375px)
- [ ] Filter is keyboard accessible (tab + enter/space)
- [ ] Filter has clear focus states

### Edge Cases
- [ ] Works with empty filter selection
- [ ] Works when rapidly changing filters
- [ ] Cards maintain layout after filtering
- [ ] Grid adjusts properly with fewer items

---

## Files Modified
1. `index.html` - Add filter UI, styling, JavaScript, and data attributes

---

## Files Created
None (all changes in existing file)

---

## Dependencies
- None (uses vanilla HTML/CSS/JS)

---

## Rollback Plan
If issues occur:
1. Remove `<div class="filter-bar">` section
2. Remove filter-related CSS
3. Remove `<script>` section
4. Remove `data-color` attributes from cards

---

## Follow-up Tickets
- **NPI-006:** Add brand filter (can reuse same pattern)
- **NPI-016:** Implement multi-filter selection (color + brand + finish)
- **NPI-017:** Add filter reset and active indicators

---

## Notes for Implementation
- Keep it simple for MVP - dropdown is faster than chips
- Color categorization is subjective - use best judgment
- Consider adding data-color to CSV for future automation
- This implementation uses display: none which maintains DOM but hides elements
- Alternative: Could use CSS classes for better animation support

---

## Estimated Time
- Data categorization: 15 minutes
- HTML/CSS changes: 20 minutes
- JavaScript implementation: 15 minutes
- Testing: 20 minutes
- **Total: ~70 minutes**
