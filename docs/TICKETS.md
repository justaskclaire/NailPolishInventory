# Project Tickets - Nail Polish Inventory

## 📊 Executive Summary

### 🎯 Current Status
- **Completed:** 30/91 tickets (33%) | 59/224 points (26%) | **Skipped/Descoped:** 13 tickets (37pts)
- **Current Phase:** 🖼️ Inspo Gallery shipped (Aug 26, 2026) - a full color/season/occasion/vibe-filterable photo gallery, "save this look" + unified Send-to-Claire, a branded 404, favicon/social preview tags, plus the Book Appointment booking flow
- **Previous Milestone:** Milestone 2 - Personalization Basics ✅ COMPLETE (Jan 3, 2026, via a simplified localStorage approach - see note in that section)
- **Velocity:** 33 points (Sprint 1) + 20 points (Aug 26, 2026 session: booking CTA + Inspo Gallery)

### 🔥 Top 5 Priorities (Next Sprint)
1. **NPI-014** - Mobile-first layout system [5pt] - Design consistency (Polishes page; Inspo page's equivalent shipped as NPI-066)
2. **NPI-060** - Pre-appointment inspo/color-pick reminder [2pt] - Inspo Gallery now gives clients somewhere to browse; the actual reminder/nudge mechanism is still unbuilt
3. **NPI-018** - Mobile usability testing [2pt] - Quality assurance
4. **NPI-019** - Add basic accessibility checks [2pt] - Accessibility compliance
5. **NPI-057/059** - Contact/inquiry form + services/pricing page [4pt] - Rounds out the booking flow

### 📦 Functional Categories
| Category | Tickets | Points | Done | Priority |
|---|:---:|:---:|:---:|:---:|
| 🎨 **Filtering & Search** | 12 | 31 | 6 ✅ | 🔥 High |
| 🗺️ **Navigation & Layout** | 8 | 20 | 3 ✅ | 🔥 Critical |
| 📄 **Content Pages** | 7 | 14 | 0 | ➡️ Medium |
| 💾 **Data & Infrastructure** | 11 | 28 | 4 ✅ | ⬆️ High |
| 👤 **User & Personalization** | 15 | 42 | 2 ✅ | ✅ Complete |
| 🎯 **Discovery & Recommendations** | 11 | 33 | 0 | ⬇️ Low |
| 🧪 **Testing & Quality** | 11 | 21 | 0 | ⬆️ High |

_This table's a cross-cutting view by function, separate from the milestone-based tracking above/below - it predates tonight's Inspo Gallery work and wasn't recategorized into it. The Milestone Overview and Project Summary sections are the accurate, current source of truth._

### ⚠️ Blockers & Dependencies
- **5 tickets blocked:** NPI-006 (brand filter), NPI-009/010/011 (content pages), NPI-015 (detail modal)
- **NPI-017** ready to start - all filter prerequisites complete (NPI-005 ✅, NPI-007 ✅, NPI-008 ✅)
- **NPI-012** (navigation) ready to start - no blockers

### 🎯 Milestone Overview
- **M1: MVP Gallery (Weeks 1-3)** → ✅ COMPLETE (Jan 3, 2026) - 29 pts delivered
- **M2: Personalization (Weeks 4-6)** → ✅ COMPLETE (Jan 3, 2026) - delivered via localStorage (favorites + next-appt + "Send colors to Claire"), not the originally-scoped auth/backend approach - see note in that section
- **M3: Enhanced Browsing (Weeks 7-9)** → Polish-specific recommendation/lookbook tickets still not started, but the **Inspo Gallery** (new, Aug 26 2026) delivers the "enhanced browsing" spirit of this milestone for inspiration photos - see the new section below
- **🖼️ Inspo Gallery (Aug 26, 2026)** → ✅ SHIPPED - 216 photos mirrored from Pinterest, tagged and filterable by Color/Season/Occasion/Vibe, hashtag overlays, clean URLs, mobile-responsive
- **M4: Booking (Future)** → 🔵 IN PROGRESS - live Google Calendar booking flow shipped (NPI-058); pricing/contact-form/payment tickets still open

---

## Quick Reference Guide
- **ID:** NPI-### (unique identifier)
- **Points:** 1-13 (Fibonacci complexity scale)
- **Status:** 🟢 Done | 🔵 In Progress | 🟡 Not Started | 🔴 Blocked | ⏭️ Skipped/Descoped (superseded by a simpler shipped solution)
- **Priority:** 🔥 Critical | ⬆️ High | ➡️ Medium | ⬇️ Low

💡 **Tip:** Click ▶ to expand ticket details | **Executive view above** for high-level status

---

## ✅ Milestone 1: MVP Gallery & Inventory (Weeks 1-3) - COMPLETED

**Final Status:** 13/21 tickets ✅ | 29/50 points (58%) | Completed January 3, 2026
**Note:** Content page tickets (NPI-009, NPI-010, NPI-011) deferred - not blocking M1 success criteria

| ID | Title | Category | Pts | Status | Priority |
|---|---|---|:---:|:---:|:---:|
| [NPI-001](#npi-001) | Set up project repository and hosting | 💾 Infrastructure | 1 | 🟢 | 🔥 |
| [NPI-002](#npi-002) | Create mobile-first responsive grid layout | 🗺️ Layout | 2 | 🟢 | 🔥 |
| [NPI-003](#npi-003) | Import existing CSV inventory data | 💾 Data | 1 | 🟢 | 🔥 |
| [NPI-004](#npi-004) | Implement image optimization and lazy loading | 💾 Performance | 2 | 🟢 | ⬆️ |
| [NPI-005](#npi-005) | Add basic color filter | 🎨 Filtering | 3 | 🟢 | ⬆️ |
| [NPI-006](#npi-006) | Add brand filter functionality | 🎨 Filtering | 2 | 🔴 | ⬆️ |
| [NPI-007](#npi-007) | Add finish filter | 🎨 Filtering | 2 | 🟢 | ⬆️ |
| [NPI-008](#npi-008) | Build search bar with name/number filtering | 🎨 Search | 3 | 🟢 | ⬆️ |
| [NPI-009](#npi-009) | Create "Charms" static page | 📄 Content | 1 | 🔴 | ➡️ |
| [NPI-010](#npi-010) | Create "Stickers" static page | 📄 Content | 1 | 🔴 | ➡️ |
| [NPI-011](#npi-011) | Create "Accessories" static page | 📄 Content | 1 | 🔴 | ➡️ |
| [NPI-012](#npi-012) | Add navigation between pages | 🗺️ Navigation | 2 | 🟢 | 🔥 |
| [NPI-013](#npi-013) | Deploy MVP to production | 💾 Infrastructure | 1 | 🟢 | 🔥 |
| [NPI-014](#npi-014) | Design and implement mobile-first layout system | 🗺️ Layout | 5 | 🟡 | 🔥 |
| [NPI-015](#npi-015) | Create polish detail modal/page | 🗺️ UI | 3 | 🔴 | ⬆️ |
| [NPI-016](#npi-016) | Implement multi-filter selection | 🎨 Filtering | 3 | 🟢 | ⬆️ |
| [NPI-017](#npi-017) | Add filter reset and active indicators | 🎨 Filtering | 3 | 🟢 | ➡️ |
| [NPI-018](#npi-018) | Run mobile usability testing | 🧪 Testing | 2 | 🟡 | ⬆️ |
| [NPI-019](#npi-019) | Add basic accessibility checks | 🧪 Quality | 2 | 🟡 | ⬆️ |
| [NPI-020](#npi-020) | Optimize page load performance | 💾 Performance | 1 | 🟡 | ⬆️ |
| [NPI-021](#npi-021) | Set up analytics tracking | 💾 Infrastructure | 1 | 🟡 | ➡️ |

<details>
<summary><b>📋 View All Ticket Details</b> (click to expand)</summary>

### Ticket Details

<details id="npi-001">
<summary><b>NPI-001</b> | Set up project repository and hosting [1pt] 🟢 🔥</summary>

### 🏷️ Tags
`infrastructure` `setup`

### 📋 Description
Initialize Git repo and configure hosting on Vercel or Netlify

### ✅ Status Notes
✅ Git initialized, GitHub remote configured (justaskclaire/NailPolishInventory)
✅ Deployed to GitHub Pages (see NPI-013)
</details>

<details id="npi-002">
<summary><b>NPI-002</b> | Create mobile-first responsive grid layout [2pt] 🟢 🔥</summary>

### 🏷️ Tags
`frontend` `layout` `mobile`

### 📋 Description
Build responsive CSS grid for polish card display

### ✅ Status Notes
✅ Implemented with `repeat(auto-fill, minmax(160px, 1fr))` in index.html
</details>

<details id="npi-003">
<summary><b>NPI-003</b> | Import existing CSV inventory data [1pt] 🟢 🔥</summary>

### 🏷️ Tags
`data` `import`

### 📋 Description
Parse polishes.csv and load into gallery view

### ✅ Status Notes
✅ 60 polish cards displayed with data from polishes.csv
✅ Enhanced CSV parser to handle quoted fields with commas (multi-color support)
✅ Added cache-busting (?v=timestamp) to prevent browser caching issues
✅ CSV includes Brand, Number, Name, Link, Image Address, LocalImage, Color, Finish columns
✅ All Color and Finish data researched from official product descriptions
</details>

<details id="npi-004">
<summary><b>NPI-004</b> | Implement image optimization and lazy loading [2pt] 🟢 ⬆️</summary>

### 🏷️ Tags
`performance` `images`

### 📋 Description
Add lazy loading for polish swatches and optimize image delivery

### ✅ Status Notes
✅ All images use `loading="lazy"` attribute, local images in /images folder
</details>

<details id="npi-005">
<summary><b>NPI-005</b> | Add basic color filter [3pt] 🟢 ⬆️</summary>

### 🏷️ Tags
`filter` `ui`

### 📋 Description
Create dropdown or chip-based color family filter that allows users to filter nail polishes by color family (reds, pinks, blues, neutrals, etc.)

### 🔗 Prerequisites
NPI-002, NPI-003

### ✅ Status Notes
✅ Implemented dropdown color filter with 11 color families (Red, Pink, Orange, Yellow, Green, Blue, Purple, Brown, Neutral, Black, White). All 33 polishes categorized with data-color attributes verified from official product pages. Real-time filtering with JavaScript. Mobile-responsive design.
✅ Multi-color support added (Dec 21) - 8 polishes have comma-separated colors (e.g., "Purple, Pink"). Filter logic updated to show polishes when ANY of their colors match selected filter.
</details>

<details id="npi-006">
<summary><b>NPI-006</b> | Add brand filter functionality [2pt] 🔴 ⬆️</summary>

### 🏷️ Tags
`filter` `ui`

### 📋 Description
Filter polishes by brand (DND, etc.)

### 🔗 Prerequisites
NPI-002, NPI-003
</details>

<details id="npi-007">
<summary><b>NPI-007</b> | Add finish filter [2pt] � ⬆️</summary>

### 🏷️ Tags
`filter` `ui`

### 📋 Description
Filter by finish type (shimmer, matte, glitter, cream, etc.)

### 🔗 Prerequisites
NPI-002, NPI-003

### ✅ Status Notes
✅ Implemented dropdown finish filter with 5 categories: Cream (16), Shimmer (14), Cat Eye (3), Mood Change (1), Sheer (1). All 33 polishes categorized in polishes.csv. Multi-filter support with AND logic (works with color filter). Implemented on feature/npi-007-finish-filter branch.
</details>

<details id="npi-008">
<summary><b>NPI-008</b> | Build search bar with name/number filtering [3pt] � ⬆️</summary>

### 🏷️ Tags
`search` `ui`

### 📋 Description
Implement real-time search for polish names and numbers

### 🔗 Prerequisites
NPI-002, NPI-003

### ✅ Status Notes
✅ Search input field added to filter bar with clean UI and focus states
✅ Real-time filtering as user types (case-insensitive)
✅ Searches both polish names and numbers simultaneously
✅ Integrates with existing color/finish filters using AND logic
✅ Data attributes (data-number, data-name) added to all cards for efficient filtering⚠️ **Currently disabled:** Search functionality commented out with TODO markers - most users don't know polish names/numbers, and if they do, they already know the polish exists. May revisit with alternative discovery approaches in future.</details>

<details id="npi-009">
<summary><b>NPI-009</b> | Create "Charms" static page [1pt] 🔴 ➡️</summary>

### 🏷️ Tags
`content` `static-pages`

### 📋 Description
Display current charm inventory with photos

### 🔴 Blocker
On hold - needs content
</details>

<details id="npi-010">
<summary><b>NPI-010</b> | Create "Stickers" static page [1pt] 🔴 ➡️</summary>

### 🏷️ Tags
`content` `static-pages`

### 📋 Description
Display current sticker inventory with photos

### 🔴 Blocker
On hold - needs content
</details>

<details id="npi-011">
<summary><b>NPI-011</b> | Create "Accessories" static page [1pt] 🔴 ➡️</summary>

### 🏷️ Tags
`content` `static-pages`

### 📋 Description
Display other accessories (tools, files, etc.)

### 🔴 Blocker
On hold - needs content
</details>

<details id="npi-012">
<summary><b>NPI-012</b> | Add navigation between pages [2pt] � 🔥</summary>

### 🏷️ Tags
`navigation` `ui`

### 📋 Description
Create header/menu navigation for gallery and extras pages

### ✅ Status Notes
✅ Navigation header component with brand logo and page links
✅ Active state highlighting for current page (Polishes)
✅ Placeholder links for future pages (Charms, Stickers, Accessories) with disabled state
✅ Fully responsive design with mobile-first breakpoints
✅ Clean visual design matching existing design system
</details>

<details id="npi-013">
<summary><b>NPI-013</b> | Deploy MVP to production [1pt] 🟢 🔥</summary>

### 🏷️ Tags
`deployment` `infrastructure`

### 📋 Description
Push live to production hosting

### 🔗 Prerequisites
NPI-001 (hosting configured)

### ✅ Status Notes
✅ Deployed via GitHub Pages
</details>

<details id="npi-014">
<summary><b>NPI-014</b> | Design and implement mobile-first layout system [5pt] 🟡 🔥</summary>

### 🏷️ Tags
`design-system` `layout` `mobile`

### 📋 Description
Create consistent spacing, breakpoints, and responsive patterns
</details>

<details id="npi-015">
<summary><b>NPI-015</b> | Create polish detail modal/page [3pt] 🔴 ⬆️</summary>

### 🏷️ Tags
`ui` `modal` `detail-view`

### 📋 Description
Show enlarged swatch and polish details when clicked

### 🔴 Blocker
Uncertain if needed - links to product page may be sufficient
</details>

<details id="npi-016">
<summary><b>NPI-016</b> | Implement multi-filter selection [3pt] � ⬆️</summary>

### 🏷️ Tags
`filter` `ui`

### 📋 Description
Allow combining color + brand + finish filters simultaneously

### 🔗 Prerequisites
NPI-005, NPI-006, NPI-007

### ✅ Status Notes
✅ Multi-select checkbox filters implemented
✅ OR logic within categories (select Red + Pink shows both)
✅ AND logic between categories (color + finish)
✅ Visual selection state with gradient backgrounds
</details>

<details id="npi-017">
<summary><b>NPI-017</b> | Add filter reset and active indicators [3pt] � ➡️</summary>

### 🏷️ Tags
`filter` `ux`

### 📋 Description
Show active filters and provide clear all button

### 🔗 Prerequisites
NPI-005, NPI-006, NPI-007

### ✅ Status Notes
✅ Clear All Filters button with enabled/disabled states
✅ Clears all filter types: colors and finishes
✅ Updates in real-time as filters change
✅ UI Refinements: Removed filter count display (not useful), simplified to just clear button
✅ Visual feedback: Selected filters now show saturated/vibrant versions of their colors
✅ Subtle gray focus indicators (no more bright red)
</details>

<details id="npi-018">
<summary><b>NPI-018</b> | Run mobile usability testing [2pt] 🟡 ⬆️</summary>

### 🏷️ Tags
`testing` `mobile` `ux`

### 📋 Description
Test on 3+ different mobile devices and browsers
</details>

<details id="npi-019">
<summary><b>NPI-019</b> | Add basic accessibility checks [2pt] 🟡 ⬆️</summary>

### 🏷️ Tags
`accessibility` `a11y`

### 📋 Description
Add ARIA labels, keyboard navigation, and screen reader support
</details>

<details id="npi-020">
<summary><b>NPI-020</b> | Optimize page load performance [1pt] 🟡 ⬆️</summary>

### 🏷️ Tags
`performance` `optimization`

### 📋 Description
Run Lighthouse audit and fix critical issues
</details>

<details id="npi-021">
<summary><b>NPI-021</b> | Set up analytics tracking [1pt] 🟡 ➡️</summary>

### 🏷️ Tags
`analytics` `tracking`

### 📋 Description
Track page views, filter usage, and user behavior
</details>

</details>

---

## 💎 Milestone 2: Personalization Basics (Weeks 4-6) - COMPLETE (simplified scope)

**Progress:** 2/15 tickets done | 13/15 skipped/descoped | 5/42 points done (37pts descoped)

> ⚠️ **Reality check (added Aug 26, 2026):** This milestone was originally scoped around full auth + a backend (NPI-022/023/025 etc.), but shipped instead via a much simpler no-login, no-backend approach: a heart-icon "favorites" toggle and a calendar-icon "next appointment" toggle, both persisted in `localStorage` with a composite `number-name` ID, plus a "📋 Send colors to Claire" clipboard-copy button so clients can hand off their picks without any account system. ROADMAP.md already reflected this; this ticket list didn't. Tickets below are marked ⏭️ Skipped where the simpler approach made them unnecessary, not because the underlying need wasn't met.

| ID | Title | Category | Pts | Status | Priority |
|---|---|---|:---:|:---:|:---:|
| [NPI-022](#npi-022) | Set up authentication system | 👤 Auth | 5 | ⏭️ | 🔥 |
| [NPI-023](#npi-023) | Create login/signup UI flow | 👤 Auth | 3 | ⏭️ | 🔥 |
| [NPI-024](#npi-024) | Design user data schema | 💾 Data | 2 | 🟢 | 🔥 |
| [NPI-025](#npi-025) | Implement backend data persistence | 💾 Backend | 5 | ⏭️ | 🔥 |
| [NPI-026](#npi-026) | Add "Favorite" button to polish cards | 👤 Favorites | 3 | 🟢 | ⬆️ |
| [NPI-027](#npi-027) | Create "My Favorites" page | 👤 Favorites | 3 | ⏭️ | ⬆️ |
| [NPI-028](#npi-028) | Build "On-Hand" vs "Wishlist" toggle | 👤 Collection | 5 | ⏭️ | ⬆️ |
| [NPI-029](#npi-029) | Create "My Collection" page | 👤 Collection | 3 | ⏭️ | ⬆️ |
| [NPI-030](#npi-030) | Add collection counters | 👤 Collection | 2 | ⏭️ | ➡️ |
| [NPI-031](#npi-031) | Create seasonal collection tags | 📄 Content | 3 | ⏭️ | ➡️ |
| [NPI-032](#npi-032) | Build "Seasonal Collections" browsing page | 📄 Content | 3 | ⏭️ | ➡️ |
| [NPI-033](#npi-033) | Add custom collections/boards feature | 👤 Collection | 2 | ⏭️ | ⬇️ |
| [NPI-034](#npi-034) | Implement cross-device data sync | 💾 Backend | 2 | ⏭️ | ⬆️ |
| [NPI-035](#npi-035) | Add collection export functionality | 💾 Data | 2 | ⏭️ | ⬇️ |
| [NPI-036](#npi-036) | Create user profile/settings page | 👤 Profile | 1 | ⏭️ | ➡️ |

<details>
<summary><b>📋 View All Ticket Details</b> (click to expand)</summary>

### Ticket Details

<details id="npi-022">
<summary><b>NPI-022</b> | Set up authentication system [5pt] ⏭️ 🔥</summary>

### 🏷️ Tags
`auth` `backend` `firebase` `supabase`

### 📋 Description
Implement Firebase or Supabase authentication

### ⏭️ Skipped
Not needed - shipped with localStorage instead, no login required (see M2 note above)
</details>

<details id="npi-023">
<summary><b>NPI-023</b> | Create login/signup UI flow [3pt] ⏭️ 🔥</summary>

### 🏷️ Tags
`auth` `ui` `forms`

### 📋 Description
Build user-friendly authentication forms and flows

### 🔗 Prerequisites
NPI-022

### ⏭️ Skipped
No auth system built - not needed
</details>

<details id="npi-024">
<summary><b>NPI-024</b> | Design user data schema [2pt] 🟢 🔥</summary>

### 🏷️ Tags
`database` `schema` `planning`

### 📋 Description
Define data structure for favorites, on-hand, wishlist

### ✅ Status Notes
✅ Shipped as a composite `number-name` ID scheme in localStorage (`nailpolish_favorites`, `nailpolish_nextappt` keys) - simpler than the originally-planned backend schema, but fulfills the same need
</details>

<details id="npi-025">
<summary><b>NPI-025</b> | Implement backend data persistence [5pt] ⏭️ 🔥</summary>

### 🏷️ Tags
`backend` `database` `api`

### 📋 Description
Build data layer for storing user preferences and collections

### 🔗 Prerequisites
NPI-022, NPI-024

### ⏭️ Skipped
No backend - localStorage is sufficient for a single-device, no-login use case
</details>

<details id="npi-026">
<summary><b>NPI-026</b> | Add "Favorite" button to polish cards [3pt] 🟢 ⬆️</summary>

### 🏷️ Tags
`ui` `favorites` `interaction`

### 📋 Description
Heart icon toggle to save favorite polishes

### 🔗 Prerequisites
NPI-022, NPI-025 (skipped - not actually needed, see below)

### ✅ Status Notes
✅ ❤️/🤍 heart icon toggle on each card, persisted in localStorage - no auth/backend required
</details>

<details id="npi-027">
<summary><b>NPI-027</b> | Create "My Favorites" page [3pt] ⏭️ ⬆️</summary>

### 🏷️ Tags
`ui` `page` `favorites`

### 📋 Description
View all saved favorite polishes

### 🔗 Prerequisites
NPI-026

### ⏭️ Skipped
Delivered differently - "My Favorites" is a filter checkbox on the main gallery (My Picks filter group) rather than a separate page
</details>

<details id="npi-028">
<summary><b>NPI-028</b> | Build "On-Hand" vs "Wishlist" toggle [5pt] ⏭️ ⬆️</summary>

### 🏷️ Tags
`ui` `collection` `tracking`

### 📋 Description
Allow users to mark polishes as owned or wanted

### 🔗 Prerequisites
NPI-022, NPI-025

### ⏭️ Skipped
Not applicable to this business model (Claire owns the inventory, clients don't) - superseded by the simpler "Next Appointment" marking concept instead
</details>

<details id="npi-029">
<summary><b>NPI-029</b> | Create "My Collection" page [3pt] ⏭️ ⬆️</summary>

### 🏷️ Tags
`ui` `page` `collection`

### 📋 Description
Display on-hand and wishlist tabs

### 🔗 Prerequisites
NPI-028

### ⏭️ Skipped
Depended on NPI-028, which was skipped
</details>

<details id="npi-030">
<summary><b>NPI-030</b> | Add collection counters [2pt] ⏭️ ➡️</summary>

### 🏷️ Tags
`ui` `stats`

### 📋 Description
Show totals for favorites/on-hand/wishlist items

### 🔗 Prerequisites
NPI-026, NPI-028

### ⏭️ Skipped
Not built - low value without the collection pages above
</details>

<details id="npi-031">
<summary><b>NPI-031</b> | Create seasonal collection tags [3pt] ⏭️ ➡️</summary>

### 🏷️ Tags
`content` `tags` `collections`

### 📋 Description
Tag polishes with Spring, Summer, Fall, Winter

### ⏭️ Skipped
Not built for polishes - but the equivalent WAS built for the Inspo Gallery (Season field: Spring/Summer/Fall/Winter, multi-label) - see NPI-062
</details>

<details id="npi-032">
<summary><b>NPI-032</b> | Build "Seasonal Collections" browsing page [3pt] ⏭️ ➡️</summary>

### 🏷️ Tags
`ui` `page` `collections`

### 📋 Description
Browse polishes by season

### 🔗 Prerequisites
NPI-031

### ⏭️ Skipped
Depended on NPI-031 (not built for polishes) - see NPI-063 for the Inspo Gallery's season filter, which serves the same purpose for inspiration photos
</details>

<details id="npi-033">
<summary><b>NPI-033</b> | Add custom collections/boards feature [2pt] ⏭️ ⬇️</summary>

### 🏷️ Tags
`ui` `collections` `customization`

### 📋 Description
Let users create named collections (e.g., "Date Night")

### 🔗 Prerequisites
NPI-025

### ⏭️ Skipped
Depended on backend persistence, which was skipped
</details>

<details id="npi-034">
<summary><b>NPI-034</b> | Implement cross-device data sync [2pt] ⏭️ ⬆️</summary>

### 🏷️ Tags
`sync` `backend`

### 📋 Description
Sync user data across logged-in devices

### 🔗 Prerequisites
NPI-022, NPI-025

### ⏭️ Skipped
No auth/backend to sync - the "Send colors to Claire" clipboard button covers the actual need (handing picks off to Claire) without needing sync
</details>

<details id="npi-035">
<summary><b>NPI-035</b> | Add collection export functionality [2pt] ⏭️ ⬇️</summary>

### 🏷️ Tags
`export` `csv` `data`

### 📋 Description
Download user's collection as CSV file

### 🔗 Prerequisites
NPI-028

### ⏭️ Skipped
Depended on NPI-028 - "Send colors to Claire" (clipboard copy) covers the practical need instead
</details>

<details id="npi-036">
<summary><b>NPI-036</b> | Create user profile/settings page [1pt] ⏭️ ➡️</summary>

### 🏷️ Tags
`ui` `profile` `settings`

### 📋 Description
Basic user profile and preferences

### 🔗 Prerequisites
NPI-022

### ⏭️ Skipped
No auth system - nothing to attach a profile to
</details>

</details>

---

## ✨ Milestone 3: Recommendations & Enhanced Browsing (Weeks 7-9)

**Progress:** 0/15 tickets | 0/46 points (0%)

> 💡 **Note (Aug 26, 2026):** None of the tickets below (recommendation engine, similar shades, lookbooks, etc. - all scoped to the *Polishes* dataset) have been built. Separately, a new **Inspo Gallery** shipped this session that delivers the "enhanced browsing/discovery" spirit of this milestone for a different dataset (216 Pinterest-sourced inspiration photos, not the polish inventory) - see the new section after Milestone 4 below for those tickets (NPI-061 onward).

| ID | Title | Category | Pts | Status | Priority |
|---|---|---|:---:|:---:|:---:|
| [NPI-037](#npi-037) | Build recommendation engine | 🎯 Recommendations | 5 | 🟡 | ⬆️ |
| [NPI-038](#npi-038) | Create "Recommended for You" section | 🎯 Recommendations | 3 | 🟡 | ⬆️ |
| [NPI-039](#npi-039) | Add "Similar Shades" feature | 🎯 Recommendations | 3 | 🟡 | ➡️ |
| [NPI-040](#npi-040) | Implement "Trending" polish highlighting | 🎯 Discovery | 3 | 🟡 | ⬇️ |
| [NPI-041](#npi-041) | Create curated lookbooks | 📄 Content | 5 | 🟡 | ➡️ |
| [NPI-042](#npi-042) | Add color family quick filters | 🎨 Filtering | 3 | 🟡 | ⬆️ |
| [NPI-043](#npi-043) | Implement advanced filter panel | 🎨 Filtering | 3 | 🟡 | ⬆️ |
| [NPI-044](#npi-044) | Add sort options | 🎨 Sorting | 2 | 🟡 | ➡️ |
| [NPI-045](#npi-045) | Add "clear all filters" button | 🎨 Filtering | 2 | 🟡 | ⬇️ |
| [NPI-046](#npi-046) | Implement filter URL params | 🎨 Filtering | 3 | 🟡 | ➡️ |
| [NPI-047](#npi-047) | Support multiple photos per polish | 💾 Data | 3 | 🟡 | ⬆️ |
| [NPI-048](#npi-048) | Add finish descriptions | 📄 Content | 2 | 🟡 | ➡️ |
| [NPI-049](#npi-049) | Add "dupes" field | 📄 Content | 2 | 🟡 | ⬇️ |
| [NPI-050](#npi-050) | Create image gallery/carousel | 🗺️ UI | 3 | 🟡 | ⬆️ |
| [NPI-051](#npi-051) | Add "recently viewed" history | 🎯 Discovery | 2 | 🟡 | ⬇️ |

💡 _Detailed ticket specs available in collapsed sections above_

---

## 📅 Milestone 4: Future Booking Foundation (Placeholder)

**Progress:** 2/9 tickets | 3/16 points (19%)

💡 _Detailed specs pending - focusing on M1-M3 first_

| ID | Title | Category | Pts | Status | Priority |
|---|---|---|:---:|:---:|:---:|
| NPI-052 | Create booking interest form | 📋 Research | 2 | 🟡 | ⬇️ |
| NPI-053 | Draft booking flow wireframes | 🎨 Design | 3 | 🟡 | ⬇️ |
| NPI-054 | Research calendar/scheduling tools | 📋 Research | 1 | 🟢 | ⬇️ |
| NPI-055 | Document pricing structure requirements | 📋 Planning | 1 | 🟡 | ⬇️ |
| NPI-056 | Plan payment integration approach | 📋 Planning | 2 | 🟡 | ⬇️ |
| NPI-057 | Build simple contact/inquiry form | 🗺️ UI | 3 | 🟡 | ➡️ |
| NPI-058 | Add "Book Appointment" CTA button | 🗺️ UI | 2 | 🟢 | ➡️ |
| NPI-059 | Create services/pricing static page | 📄 Content | 1 | 🟡 | ➡️ |
| NPI-060 | Add pre-appointment inspo/color-pick reminder | 📅 Booking | 2 | 🟡 | ➡️ |

#### NPI-054: Research calendar/scheduling tools ✅ DONE (Aug 26, 2026)
Chose **Google Calendar Appointment Schedules** (the native booking-page feature, not the full Calendar API) - zero code, zero backend, matches the static-site philosophy. Found and documented a workaround for Google's fixed-duration-slot limitation (decouple slot spacing from real appointment length using a shorter Duration + a Buffer time after, e.g. 60min duration + 120min buffer = hourly start times but 3 real hours blocked). Booking notifications go through Google's own "Appointment schedules" notification setting plus the per-calendar "New events" setting.

#### NPI-058: Add "Book Appointment" CTA button ✅ DONE (Aug 26, 2026)
Added as a styled solid-rose CTA in the nav on both the Polishes and Inspo pages, linking to the Google Calendar appointment schedule (opens in a new tab). Placed as its own live nav item, kept separate from the still-commented-out Charms/Stickers/Accessories placeholder links.

#### NPI-060: Add pre-appointment inspo/color-pick reminder

**Requested by:** Friend (client), via Claire, 2026-08-26

**Problem:** Clients book via the Google Calendar appointment schedule, whose event description links to the Pinterest inspo board and the polish gallery site — but nothing prompts clients to actually go review inspo and pick colors *before* they show up.

**Possible approaches (unresearched):**
- Google Calendar's own event reminder/notification settings (e.g. an extra reminder on the booking event, or a custom email a day before)
- A follow-up automation (e.g. Zapier/Apps Script) triggered off new calendar bookings
- Text in the booking form itself asking clients to pre-select colors

**Status:** 🟡 Not started, but partially addressed as a side effect — the **Inspo Gallery** (NPI-061-068, below) now gives clients an actual page to browse and filter inspiration photos by before their appointment, which is half of what this ticket wanted. The *active reminder/nudge* mechanism itself (a calendar notification tweak, or an automation that fires when someone books) still isn't built.

---

## 🖼️ Inspo Gallery (Aug 26, 2026) - SHIPPED

**Progress:** 14/15 tickets done | 28/33 points (85%)

Not part of the original milestone plan — delivers the "Pinterest-powered inspiration browsing" vision from `docs/Milestone3Planning.md` via a local photo mirror instead of the live Pinterest API, sidestepping the still-pending Pinterest API trial approval entirely. Also functions as the practical half of NPI-060.

| ID | Title | Category | Pts | Status | Priority |
|---|---|---|:---:|:---:|:---:|
| NPI-061 | Mirror Pinterest inspo board photos locally | 💾 Data | 2 | 🟢 | 🔥 |
| NPI-062 | Tag all photos by Color/Season/Occasion/Vibe | 🎯 Discovery | 5 | 🟢 | 🔥 |
| NPI-063 | Build Inspo Gallery filter UI | 🎨 Filtering | 3 | 🟢 | 🔥 |
| NPI-064 | Add hashtag overlay + click-to-enlarge lightbox | 🗺️ UI | 2 | 🟢 | ➡️ |
| NPI-065 | Clean URLs for Inspo page (`/inspo/`, no `.html`) | 💾 Infrastructure | 1 | 🟢 | ➡️ |
| NPI-066 | Fix Inspo page mobile-responsive layout | 🗺️ Layout | 2 | 🟢 | 🔥 |
| NPI-067 | Fix nav consistency between Polishes and Inspo pages | 🗺️ Navigation | 1 | 🟢 | ➡️ |
| NPI-068 | Add emoji icons to Occasion/Vibe filter labels | 🎨 Design System | 1 | 🟢 | ⬇️ |
| NPI-069 | Add branded 404 page | 🗺️ UI | 1 | 🟢 | ➡️ |
| NPI-070 | Add favicon + Open Graph/social preview tags | 🎨 Design System | 1 | 🟢 | ➡️ |
| NPI-071 | My Favorites + My Next Appt on Inspo photos, unified Send-to-Claire | 👤 Favorites | 4 | 🟢 | ⬆️ |
| NPI-072 | Auto-suggest matching polishes from a photo's colors ("dream world" feature) | 🎯 Recommendations | 5 | 🟡 | ⬇️ |
| NPI-073 | Fix Inspo page header to match Polishes page structure | 🗺️ Navigation | 1 | 🟢 | ➡️ |
| NPI-074 | Sort color filters in rainbow order (both pages) | 🎨 Design System | 1 | 🟢 | ⬇️ |
| NPI-075 | Instagram-style mobile grid + randomized photo order | 🗺️ Layout | 3 | 🟢 | ➡️ |

<details>
<summary><b>📋 View All Ticket Details</b> (click to expand)</summary>

<details id="npi-061">
<summary><b>NPI-061</b> | Mirror Pinterest inspo board photos locally [2pt] 🟢 🔥</summary>

### 🏷️ Tags
`data` `images` `pinterest`

### 📋 Description
Download the photos from Claire's Pinterest "nail-inspo" board to `public/inspo/` so they can be browsed without the Pinterest API

### ✅ Status Notes
✅ `scripts/download_nails.py` downloads all 216 pins via direct `i.pinimg.com` URLs to `public/inspo/nail-001.jpg` through `nail-216.jpg`
</details>

<details id="npi-062">
<summary><b>NPI-062</b> | Tag all photos by Color/Season/Occasion/Vibe [5pt] 🟢 🔥</summary>

### 🏷️ Tags
`data` `tagging` `ai`

### 📋 Description
Visually tag each of the 216 photos so they can be filtered like the polish gallery

### ✅ Status Notes
✅ Two full tagging passes (216 photos each, via parallel sub-agents actually viewing every image). First pass: Color (any visible) + single Occasion. Second pass, after Claire's feedback: Color restricted to primary/dominant only + added Black to the vocabulary; Occasion split into independent multi-label **Season** (Spring/Summer/Fall/Winter) and **Occasion** (Christmas/Valentine's Day/Halloween/Easter/New Year's/4th of July/Birthday/Everyday) fields, since designs often span several; New Year's broadened to catch any glitter/sparkle/metallic shine regardless of color (8→37 photos); added a 4th **Vibe** field (Minimalist/Detailed/Floral/Geometric/Glam/French Tip/Ombre/Polka Dot/Stripes/Marble/Abstract/Animal Print/Whimsical/Elegant).
✅ Data lives in `data/inspo.csv` (`Filename,Colors,Seasons,Occasions,Vibes,Confidence`)
✅ 142/216 photos flagged low-confidence on the occasion/season/vibe judgment calls - logged in `docs/inspo-tagging-review.md` for Claire to spot-check; colors are generally reliable
</details>

<details id="npi-063">
<summary><b>NPI-063</b> | Build Inspo Gallery filter UI [3pt] 🟢 🔥</summary>

### 🏷️ Tags
`filter` `ui`

### 📋 Description
Filter the 216 photos by Color, Season, Occasion, and Vibe, matching the Polishes page's filter UX

### ✅ Status Notes
✅ Four independent filter groups, each populated only from tags that actually exist in the data (a tag with zero photos never renders as an option - verified Marble/Animal Print correctly don't show up)
✅ Same OR-within-category / AND-across-categories logic as the Polishes page, same color-swatch CSS classes (plus added Black, which the Polishes page's filter didn't have either)
✅ Live count, Clear All Filters, empty-state message
</details>

<details id="npi-064">
<summary><b>NPI-064</b> | Add hashtag overlay + click-to-enlarge lightbox [2pt] 🟢 ➡️</summary>

### 🏷️ Tags
`ui` `interaction`

### 📋 Description
Show each photo's tags directly on the thumbnail, and let users tap a photo to see it larger

### ✅ Status Notes
✅ `#floral #spring`-style hashtag overlay (dark gradient scrim + light text) built from Season+Occasion+Vibe, visible while scrolling
✅ Vanilla-JS lightbox on click, closes on backdrop click, close button, or Escape
</details>

<details id="npi-065">
<summary><b>NPI-065</b> | Clean URLs for Inspo page [1pt] 🟢 ➡️</summary>

### 🏷️ Tags
`infrastructure` `urls`

### 📋 Description
Serve the Inspo page at `/inspo/` instead of `/inspo.html`, matching how the site root already works

### ✅ Status Notes
✅ Moved to `inspo/index.html` (GitHub Pages serves `index.html` for directory requests natively, no server config needed)
✅ Left a meta-refresh redirect stub at the old `inspo.html` path after the move broke existing bookmarks/links - lesson: should have shipped the redirect in the same commit as the move, not after
</details>

<details id="npi-066">
<summary><b>NPI-066</b> | Fix Inspo page mobile-responsive layout [2pt] 🟢 🔥</summary>

### 🏷️ Tags
`mobile` `responsive` `bug`

### 📋 Description
Fix the nav ("Book Appointment" overflowing off-screen) and grid layout on small viewports

### ✅ Status Notes
✅ Root cause: the Inspo page was built from scratch and never got the `@media (max-width: 768px)` responsive overrides the Polishes page already had, so the nav never switched to a stacked mobile layout. Ported that breakpoint over, plus dropped the masonry grid to a single column below 768px.
✅ Verified at a 375px mobile viewport: no horizontal overflow, nav stacks cleanly
</details>

<details id="npi-067">
<summary><b>NPI-067</b> | Fix nav consistency between Polishes and Inspo pages [1pt] 🟢 ➡️</summary>

### 🏷️ Tags
`navigation` `consistency` `bug`

### 📋 Description
Both pages should show the same nav links

### ✅ Status Notes
✅ "Polishes" had been left inside the commented-out placeholder block (grouped with the still-unbuilt Charms/Stickers/Accessories) on the home page, so it only appeared as a link on the Inspo page. Split it out as a live link on both pages.
</details>

<details id="npi-068">
<summary><b>NPI-068</b> | Add emoji icons to Occasion/Vibe filter labels [1pt] 🟢 ⬇️</summary>

### 🏷️ Tags
`design-system` `polish`

### 📋 Description
Give every Occasion and Vibe filter option a small emoji, matching the existing Season icons

### ✅ Status Notes
✅ 💅 Everyday, plus a unique emoji for each of the 14 Vibe tags (🎨 Abstract, 🔬 Detailed, 💎 Elegant, 🌼 Floral, 🤍 French Tip, 🔷 Geometric, ✨ Glam, ⚪ Minimalist, 🌈 Ombre, ⚫ Polka Dot, 〰️ Stripes, 🦄 Whimsical, plus Marble/Animal Print icons defined and waiting for a photo to use them)
</details>

<details id="npi-069">
<summary><b>NPI-069</b> | Add branded 404 page [1pt] 🟢 ➡️</summary>

### 🏷️ Tags
`ui` `error-handling` `polish`

### 📋 Description
Replace GitHub's generic 404 with something on-brand that helps people recover

### ✅ Status Notes
✅ `404.html` at repo root (GitHub Pages convention - served automatically for any unmatched path). Studio Claire branding, absolute URLs (a 404 can fire at any path depth, so relative links aren't reliable) back to Polishes, Inspo, and Book Appointment.
</details>

<details id="npi-070">
<summary><b>NPI-070</b> | Add favicon + Open Graph/social preview tags [1pt] 🟢 ➡️</summary>

### 🏷️ Tags
`design-system` `seo` `polish`

### 📋 Description
The site had no favicon and no social-share preview metadata at all

### ✅ Status Notes
✅ Favicon (`public/favicon.svg`, shared by both pages) - started as a hand-drawn nail polish bottle, swapped to a simple 💅 emoji per Claire's preference
✅ `og:title`/`og:description`/`og:image`/`og:url` + `twitter:card` on both pages, using an existing Inspo photo (`nail-079.jpg`) as the shared preview image
</details>

<details id="npi-071">
<summary><b>NPI-071</b> | My Favorites + My Next Appt on Inspo photos, unified Send-to-Claire [4pt] 🟢 ⬆️</summary>

### 🏷️ Tags
`ui` `favorites` `interaction`

### 📋 Description
Let clients save Inspo photos they like and hand off their Next Appt picks to Claire, same two-list pattern as the Polishes page - requested as "someone picks an inspo pic ... and can easily share it with me in some way," then corrected to actually match the Polishes page's Favorites/Next-Appt split rather than a single combined heart

### ✅ Status Notes
✅ First pass shipped a single ❤️/🤍 "save this look" heart whose list also drove the send button - not what was asked for. Corrected same evening.
✅ **Final version:** two icon buttons per photo (❤️/🤍 favorite-btn + 📅/🗓️ nextappt-btn), identical `card-icons`/`icon-btn` CSS and active-state behavior to the Polishes page, including the mobile always-visible/44px-touch-target override
✅ "My Picks" filter group (My Favorites / My Next Appt checkboxes) as the *first* filter group, before Color - filters the grid by either list
✅ **Favorites is a personal bookmark/filter only - it is never sent.** Only **My Next Appt** drives "📋 Send my picks to Claire", exactly matching the Polishes page's semantics
✅ Send button moved into the My Picks filter group as a full-width button with the Polishes page's exact blue "next appt" gradient - was previously a small button tucked into the filter-controls corner, which didn't match
✅ Deep links (`/inspo/#nail-042`) with each photo's Season/Occasion/Vibe tags copy to the clipboard; visiting one auto-opens that photo in the lightbox
✅ Contextual empty-state messages when a personal filter alone yields zero results, matching the Polishes page's tone
✅ **Unified across both pages** (same-origin localStorage, key `nailinspo_nextappt`): the Polishes page's "Send my picks to Claire" now also includes a "Nail inspo for my next appointment" section if any Inspo photos are marked, and shows itself if *either* list has items
</details>

<details id="npi-072">
<summary><b>NPI-072</b> | Auto-suggest matching polishes from a photo's colors [5pt] 🟡 ⬇️</summary>

### 🏷️ Tags
`recommendations` `data` `dream-feature`

### 📋 Description
Claire's "true dream world" version of NPI-071: each Inspo photo shows which polishes from the actual inventory match its colors, so a client picking a look also gets a ready answer for "which polish is that?"

### 💡 Why this is closer than it sounds
Both datasets already use a compatible color vocabulary - `data/inspo.csv`'s Colors column and `data/polishes.csv`'s Color column both draw from the same category names (Red, Pink, Blue, etc., NPI-062's primary-color tagging). A first version could be pure client-side JS with no new tagging work: for a given Inspo photo, look up its Colors, filter `polishes.csv` for matches, show 2-3 as "Try: #123 Ruby Red" in the lightbox.

**Status:** Not started - logged as a follow-up idea, not scoped for a single evening.
</details>

<details id="npi-073">
<summary><b>NPI-073</b> | Fix Inspo page header to match Polishes page structure [1pt] 🟢 ➡️</summary>

### 🏷️ Tags
`ui` `consistency` `bug`

### 📋 Description
Claire flagged the two pages' headers didn't look/feel the same

### ✅ Status Notes
✅ Root cause: Inspo had an entire extra section (large "Nail Inspo" title + tagline + hint paragraph) between the nav and the filter bar that the Polishes page never had - Polishes goes straight from nav-header into the filter-bar. Removed that block entirely and folded its description into the filter-controls hint row, matching the Polishes page's exact structure (count + hint text + Clear All Filters, nothing else above the filter-bar). Removed the now-dead `.header`/`h1` CSS.
</details>

<details id="npi-074">
<summary><b>NPI-074</b> | Sort color filters in rainbow order (both pages) [1pt] 🟢 ⬇️</summary>

### 🏷️ Tags
`ui` `design-system` `polish`

### 📋 Description
Color filter buttons were sorted alphabetically; Claire asked for rainbow order instead

### ✅ Status Notes
✅ New order on both pages: Red, Orange, Yellow, Green, Blue, Purple, Pink, then neutrals (Brown, Gold, Neutral, White, Grey, Black - Inspo only, since Polishes has no Black-tagged polish yet)
</details>

<details id="npi-075">
<summary><b>NPI-075</b> | Instagram-style mobile grid + randomized photo order [3pt] 🟢 ➡️</summary>

### 🏷️ Tags
`ui` `mobile` `layout`

### 📋 Description
Two asks: (a) show photos smaller on mobile, "think insta grid"; (b) randomize photo order so visitors don't always land on the same ones first

### ✅ Status Notes
✅ Mobile (<768px) switched from single-column masonry to a tight 3-column square grid (~112px cells, 3px gaps, `object-fit: cover` crop) - tablet/desktop masonry unchanged
✅ 44px touch-target icons don't fit on a 112px thumbnail, so the per-photo favorite/next-appt icons and hashtag overlay are hidden on the mobile grid. Added matching action buttons + a tag summary directly in the lightbox instead - tap the photo, then act on it, same interaction model Instagram itself uses. Toggling from the lightbox stays in sync with the grid's icon state via a shared `setIconButtonState`/`syncGridIcons` helper
✅ Photos render in a random order each page load (Fisher-Yates shuffle on the parsed CSV data before rendering) - filtering, counts, and deep links are all order-independent so nothing else was affected
</details>

</details>

---

## 🎨 Ongoing & Infrastructure

**Progress:** 0/16 tickets | 0/37 points (0%)

| Category | Tickets | Points |
|---|:---:|:---:|
| Design System | 4 | 12 |
| Content & Data Management | 4 | 10 |
| Quality & Performance | 5 | 10 |
| Testing | 3 | 10 |

_Full ticket list available - expand sections as needed_

---

## 🚀 Recommended Sprint Plan

### Sprint 1: Foundation Setup (13 points) ✅ DONE
- ✅ **NPI-001** - Set up project repository (1pt)
- ✅ **NPI-002** - Create mobile-first grid (2pt)
- ✅ **NPI-003** - Import CSV inventory (1pt)
- ✅ **NPI-004** - Image optimization (2pt)
- ⬜ **NPI-005** - Add color filter (3pt)
- ⬜ **NPI-006** - Add brand filter (2pt)
- ⬜ **NPI-012** - Add navigation (2pt)

### Sprint 2: Core Features (13 points)
- **NPI-008** - Build search bar (3pt)
- **NPI-015** - Create polish detail modal (3pt)
- **NPI-007** - Add finish filter (2pt)
- **NPI-009** - Charms page (1pt)
- **NPI-010** - Stickers page (1pt)
- **NPI-011** - Accessories page (1pt)
- **NPI-018** - Mobile usability testing (2pt)

### Sprint 3: Polish & Deploy (13 points)
- **NPI-013** - Deploy MVP (1pt)
- **NPI-014** - Mobile-first layout system (5pt)
- **NPI-016** - Multi-filter selection (3pt)
- **NPI-019** - Accessibility checks (2pt)
- **NPI-020** - Performance optimization (1pt)
- **NPI-021** - Analytics setup (1pt)

---

## 📊 Project Summary

**Total:** 91 tickets | 224 story points  
**Completed:** 30 tickets (33%) | 59 points (26%)  
**Skipped/Descoped:** 13 tickets (14%) | 37 points (17%) - all in M2, superseded by the simpler localStorage approach that actually shipped  
**In Progress:** 0 tickets  
**Not Started:** 48 tickets | 128 points  

### By Milestone
| Milestone | Tickets | Points | Done | Skipped | Remaining |
|---|:---:|:---:|:---:|:---:|:---:|
| 🚀 M1: MVP Gallery | 21 | 50 | 11 ✅ (23pts) | 0 | 10 (27pts) |
| 💎 M2: Personalization | 15 | 42 | 2 ✅ (5pts) | 13 (37pts) | 0 |
| ✨ M3: Enhanced Browsing | 15 | 46 | 0 | 0 | 15 (46pts) |
| 📅 M4: Booking | 9 | 16 | 2 ✅ (3pts) | 0 | 7 (13pts) |
| 🎨 Infrastructure | 16 | 37 | 0 | 0 | 16 (37pts) |
| 🖼️ Inspo Gallery | 15 | 33 | 14 ✅ (28pts) | 0 | 1 (5pts) |

### By Priority
_(Individually-itemized tickets only - the 16 Infrastructure tickets are tracked as a category rollup, not itemized, so aren't counted here)_
- 🔥 **Critical:** 14 tickets - 10 done, 3 skipped, 1 not started
- ⬆️ **High:** 22 tickets - 7 done, 4 skipped, 2 blocked, 9 not started
- ➡️ **Medium:** 25 tickets - 9 done, 4 skipped, 3 blocked, 9 not started
- ⬇️ **Low:** 14 tickets - 3 done, 2 skipped, 9 not started

### Quick Stats
- Average ticket: 2.5 points
- Milestone 1 velocity: 23 points completed
- Aug 26, 2026 session velocity: 20 points (Book Appointment + calendar research + full Inspo Gallery)
- Estimated M1 completion: 27 points remaining (~2 more sprints)

---

## 📝 Usage Guide

**For executive overview:** See the [Executive Summary](#-executive-summary) at the top for key priorities and status  
**For high-level planning:** Use the summary tables with categories to see all tickets at a glance  
**For detailed work:** Expand the collapsible "View All Ticket Details" sections  
**For navigation:** Click ticket IDs in tables to jump to detailed sections  
**For tracking:** Update status emojis and notes in ticket details  

**Need implementation details?** Check the `guides/` folder for step-by-step instructions

---

## 🔄 Quick Access

- [📊 Executive Summary](#executive-summary) - Current status, priorities, and category breakdown
- [🚀 Milestone 1: MVP Gallery](#milestone-1-mvp-gallery--inventory-weeks-1-3) - 52% complete (11/21)
- [💎 Milestone 2: Personalization](#milestone-2-personalization-basics-weeks-4-6) - Complete via simplified scope (2 done, 13 skipped)
- [✨ Milestone 3: Enhanced Browsing](#milestone-3-recommendations--enhanced-browsing-weeks-7-9) - Not started (polish-specific tickets; see Inspo Gallery below for the delivered equivalent)
- [📅 Milestone 4: Booking](#milestone-4-future-booking-foundation-placeholder) - In progress (2/9 done)
- [🖼️ Inspo Gallery](#-inspo-gallery-aug-26-2026---shipped) - 100% complete (8/8)
- [🚀 Sprint Plan](#recommended-sprint-plan) - Recommended sprint breakdown
