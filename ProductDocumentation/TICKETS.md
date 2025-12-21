# Project Tickets - Nail Polish Inventory

## Quick Reference Guide
- **ID:** NPI-### (unique identifier)
- **Points:** 1-13 (Fibonacci complexity scale)
- **Status:** 🟢 Done | 🔵 In Progress | 🟡 Not Started | 🔴 Blocked
- **Priority:** 🔥 Critical | ⬆️ High | ➡️ Medium | ⬇️ Low

💡 **Tip:** Click ▶ to expand ticket details

---

## 🚀 Milestone 1: MVP Gallery & Inventory (Weeks 1-3)

**Progress:** 4/21 tickets ✅ | 6/50 points (12%)

| ID | Title | Pts | Status | Priority |
|---|---|:---:|:---:|:---:|
| [NPI-001](#npi-001) | Set up project repository and hosting | 1 | 🟢 | 🔥 |
| [NPI-002](#npi-002) | Create mobile-first responsive grid layout | 2 | 🟢 | 🔥 |
| [NPI-003](#npi-003) | Import existing CSV inventory data | 1 | 🟢 | 🔥 |
| [NPI-004](#npi-004) | Implement image optimization and lazy loading | 2 | 🟢 | ⬆️ |
| [NPI-005](#npi-005) | Add basic color filter | 3 | 🟡 | ⬆️ |
| [NPI-006](#npi-006) | Add brand filter functionality | 2 | 🟡 | ⬆️ |
| [NPI-007](#npi-007) | Add finish filter | 2 | 🟡 | ➡️ |
| [NPI-008](#npi-008) | Build search bar with name/number filtering | 3 | 🟡 | ⬆️ |
| [NPI-009](#npi-009) | Create "Charms" static page | 1 | 🟡 | ➡️ |
| [NPI-010](#npi-010) | Create "Stickers" static page | 1 | 🟡 | ➡️ |
| [NPI-011](#npi-011) | Create "Accessories" static page | 1 | 🟡 | ➡️ |
| [NPI-012](#npi-012) | Add navigation between pages | 2 | 🟡 | 🔥 |
| [NPI-013](#npi-013) | Deploy MVP to production | 1 | 🟡 | 🔥 |
| [NPI-014](#npi-014) | Design and implement mobile-first layout system | 5 | 🟡 | 🔥 |
| [NPI-015](#npi-015) | Create polish detail modal/page | 3 | 🟡 | ⬆️ |
| [NPI-016](#npi-016) | Implement multi-filter selection | 3 | 🟡 | ⬆️ |
| [NPI-017](#npi-017) | Add filter reset and active indicators | 3 | 🟡 | ➡️ |
| [NPI-018](#npi-018) | Run mobile usability testing | 2 | 🟡 | ⬆️ |
| [NPI-019](#npi-019) | Add basic accessibility checks | 2 | 🟡 | ⬆️ |
| [NPI-020](#npi-020) | Optimize page load performance | 1 | 🟡 | ⬆️ |
| [NPI-021](#npi-021) | Set up analytics tracking | 1 | 🟡 | ➡️ |

### Ticket Details

<details id="npi-001">
<summary><b>NPI-001</b> | Set up project repository and hosting [1pt] 🟢 🔥</summary>

**Tags:** `infrastructure` `setup`

**Description:** Initialize Git repo and configure hosting on Vercel or Netlify

**Status Notes:** ✅ Git initialized, GitHub remote configured (justaskclaire/NailPolishInventory)

**Implementation Guide:** [NPI-001-implementation.md](guides/NPI-001-implementation.md)
</details>

<details id="npi-002">
<summary><b>NPI-002</b> | Create mobile-first responsive grid layout [2pt] 🟢 🔥</summary>

**Tags:** `frontend` `layout` `mobile`

**Description:** Build responsive CSS grid for polish card display

**Status Notes:** ✅ Implemented with `repeat(auto-fill, minmax(160px, 1fr))` in index.html
</details>

<details id="npi-003">
<summary><b>NPI-003</b> | Import existing CSV inventory data [1pt] 🟢 🔥</summary>

**Tags:** `data` `import`

**Description:** Parse polishes.csv and load into gallery view

**Status Notes:** ✅ 33 polish cards displayed with data from polishes.csv
</details>

<details id="npi-004">
<summary><b>NPI-004</b> | Implement image optimization and lazy loading [2pt] 🟢 ⬆️</summary>

**Tags:** `performance` `images`

**Description:** Add lazy loading for polish swatches and optimize image delivery

**Status Notes:** ✅ All images use `loading="lazy"` attribute, local images in /images folder
</details>

<details id="npi-005">
<summary><b>NPI-005</b> | Add basic color filter [3pt] 🟡 ⬆️</summary>

**Tags:** `filter` `ui`

**Description:** Create dropdown or chip-based color family filter that allows users to filter nail polishes by color family (reds, pinks, blues, neutrals, etc.)

**Prerequisites:** NPI-002, NPI-003

**Implementation Guide:** [NPI-005-implementation.md](guides/NPI-005-implementation.md)
</details>

<details id="npi-006">
<summary><b>NPI-006</b> | Add brand filter functionality [2pt] 🟡 ⬆️</summary>

**Tags:** `filter` `ui`

**Description:** Filter polishes by brand (DND, etc.)

**Prerequisites:** NPI-002, NPI-003
</details>

<details id="npi-007">
<summary><b>NPI-007</b> | Add finish filter [2pt] 🟡 ➡️</summary>

**Tags:** `filter` `ui`

**Description:** Filter by finish type (shimmer, matte, glitter, cream, etc.)

**Prerequisites:** NPI-002, NPI-003
</details>

<details id="npi-008">
<summary><b>NPI-008</b> | Build search bar with name/number filtering [3pt] 🟡 ⬆️</summary>

**Tags:** `search` `ui`

**Description:** Implement real-time search for polish names and numbers

**Prerequisites:** NPI-002, NPI-003
</details>

<details id="npi-009">
<summary><b>NPI-009</b> | Create "Charms" static page [1pt] 🟡 ➡️</summary>

**Tags:** `content` `static-pages`

**Description:** Display current charm inventory with photos
</details>

<details id="npi-010">
<summary><b>NPI-010</b> | Create "Stickers" static page [1pt] 🟡 ➡️</summary>

**Tags:** `content` `static-pages`

**Description:** Display current sticker inventory with photos
</details>

<details id="npi-011">
<summary><b>NPI-011</b> | Create "Accessories" static page [1pt] 🟡 ➡️</summary>

**Tags:** `content` `static-pages`

**Description:** Display other accessories (tools, files, etc.)
</details>

<details id="npi-012">
<summary><b>NPI-012</b> | Add navigation between pages [2pt] 🟡 🔥</summary>

**Tags:** `navigation` `ui`

**Description:** Create header/menu navigation for gallery and extras pages
</details>

<details id="npi-013">
<summary><b>NPI-013</b> | Deploy MVP to production [1pt] 🟡 🔥</summary>

**Tags:** `deployment` `infrastructure`

**Description:** Push live to production hosting

**Prerequisites:** NPI-001 (hosting configured)
</details>

<details id="npi-014">
<summary><b>NPI-014</b> | Design and implement mobile-first layout system [5pt] 🟡 🔥</summary>

**Tags:** `design-system` `layout` `mobile`

**Description:** Create consistent spacing, breakpoints, and responsive patterns
</details>

<details id="npi-015">
<summary><b>NPI-015</b> | Create polish detail modal/page [3pt] 🟡 ⬆️</summary>

**Tags:** `ui` `modal` `detail-view`

**Description:** Show enlarged swatch and polish details when clicked
</details>

<details id="npi-016">
<summary><b>NPI-016</b> | Implement multi-filter selection [3pt] 🟡 ⬆️</summary>

**Tags:** `filter` `ui`

**Description:** Allow combining color + brand + finish filters simultaneously

**Prerequisites:** NPI-005, NPI-006, NPI-007
</details>

<details id="npi-017">
<summary><b>NPI-017</b> | Add filter reset and active indicators [3pt] 🟡 ➡️</summary>

**Tags:** `filter` `ux`

**Description:** Show active filters and provide clear all button

**Prerequisites:** NPI-005, NPI-006, NPI-007
</details>

<details id="npi-018">
<summary><b>NPI-018</b> | Run mobile usability testing [2pt] 🟡 ⬆️</summary>

**Tags:** `testing` `mobile` `ux`

**Description:** Test on 3+ different mobile devices and browsers
</details>

<details id="npi-019">
<summary><b>NPI-019</b> | Add basic accessibility checks [2pt] 🟡 ⬆️</summary>

**Tags:** `accessibility` `a11y`

**Description:** Add ARIA labels, keyboard navigation, and screen reader support
</details>

<details id="npi-020">
<summary><b>NPI-020</b> | Optimize page load performance [1pt] 🟡 ⬆️</summary>

**Tags:** `performance` `optimization`

**Description:** Run Lighthouse audit and fix critical issues
</details>

<details id="npi-021">
<summary><b>NPI-021</b> | Set up analytics tracking [1pt] 🟡 ➡️</summary>

**Tags:** `analytics` `tracking`

**Description:** Track page views, filter usage, and user behavior
</details>

---

## 💎 Milestone 2: Personalization Basics (Weeks 4-6)

**Progress:** 0/15 tickets | 0/42 points (0%)

| ID | Title | Pts | Status | Priority |
|---|---|:---:|:---:|:---:|
| [NPI-022](#npi-022) | Set up authentication system | 5 | 🟡 | 🔥 |
| [NPI-023](#npi-023) | Create login/signup UI flow | 3 | 🟡 | 🔥 |
| [NPI-024](#npi-024) | Design user data schema | 2 | 🟡 | 🔥 |
| [NPI-025](#npi-025) | Implement backend data persistence | 5 | 🟡 | 🔥 |
| [NPI-026](#npi-026) | Add "Favorite" button to polish cards | 3 | 🟡 | ⬆️ |
| [NPI-027](#npi-027) | Create "My Favorites" page | 3 | 🟡 | ⬆️ |
| [NPI-028](#npi-028) | Build "On-Hand" vs "Wishlist" toggle | 5 | 🟡 | ⬆️ |
| [NPI-029](#npi-029) | Create "My Collection" page | 3 | 🟡 | ⬆️ |
| [NPI-030](#npi-030) | Add collection counters | 2 | 🟡 | ➡️ |
| [NPI-031](#npi-031) | Create seasonal collection tags | 3 | 🟡 | ➡️ |
| [NPI-032](#npi-032) | Build "Seasonal Collections" browsing page | 3 | 🟡 | ➡️ |
| [NPI-033](#npi-033) | Add custom collections/boards feature | 2 | 🟡 | ⬇️ |
| [NPI-034](#npi-034) | Implement cross-device data sync | 2 | 🟡 | ⬆️ |
| [NPI-035](#npi-035) | Add collection export functionality | 2 | 🟡 | ⬇️ |
| [NPI-036](#npi-036) | Create user profile/settings page | 1 | 🟡 | ➡️ |

### Ticket Details

<details id="npi-022">
<summary><b>NPI-022</b> | Set up authentication system [5pt] 🟡 🔥</summary>

**Tags:** `auth` `backend` `firebase` `supabase`

**Description:** Implement Firebase or Supabase authentication
</details>

<details id="npi-023">
<summary><b>NPI-023</b> | Create login/signup UI flow [3pt] 🟡 🔥</summary>

**Tags:** `auth` `ui` `forms`

**Description:** Build user-friendly authentication forms and flows

**Prerequisites:** NPI-022
</details>

<details id="npi-024">
<summary><b>NPI-024</b> | Design user data schema [2pt] 🟡 🔥</summary>

**Tags:** `database` `schema` `planning`

**Description:** Define data structure for favorites, on-hand, wishlist
</details>

<details id="npi-025">
<summary><b>NPI-025</b> | Implement backend data persistence [5pt] 🟡 🔥</summary>

**Tags:** `backend` `database` `api`

**Description:** Build data layer for storing user preferences and collections

**Prerequisites:** NPI-022, NPI-024
</details>

<details id="npi-026">
<summary><b>NPI-026</b> | Add "Favorite" button to polish cards [3pt] 🟡 ⬆️</summary>

**Tags:** `ui` `favorites` `interaction`

**Description:** Heart icon toggle to save favorite polishes

**Prerequisites:** NPI-022, NPI-025
</details>

<details id="npi-027">
<summary><b>NPI-027</b> | Create "My Favorites" page [3pt] 🟡 ⬆️</summary>

**Tags:** `ui` `page` `favorites`

**Description:** View all saved favorite polishes

**Prerequisites:** NPI-026
</details>

<details id="npi-028">
<summary><b>NPI-028</b> | Build "On-Hand" vs "Wishlist" toggle [5pt] 🟡 ⬆️</summary>

**Tags:** `ui` `collection` `tracking`

**Description:** Allow users to mark polishes as owned or wanted

**Prerequisites:** NPI-022, NPI-025
</details>

<details id="npi-029">
<summary><b>NPI-029</b> | Create "My Collection" page [3pt] 🟡 ⬆️</summary>

**Tags:** `ui` `page` `collection`

**Description:** Display on-hand and wishlist tabs

**Prerequisites:** NPI-028
</details>

<details id="npi-030">
<summary><b>NPI-030</b> | Add collection counters [2pt] 🟡 ➡️</summary>

**Tags:** `ui` `stats`

**Description:** Show totals for favorites/on-hand/wishlist items

**Prerequisites:** NPI-026, NPI-028
</details>

<details id="npi-031">
<summary><b>NPI-031</b> | Create seasonal collection tags [3pt] 🟡 ➡️</summary>

**Tags:** `content` `tags` `collections`

**Description:** Tag polishes with Spring, Summer, Fall, Winter
</details>

<details id="npi-032">
<summary><b>NPI-032</b> | Build "Seasonal Collections" browsing page [3pt] 🟡 ➡️</summary>

**Tags:** `ui` `page` `collections`

**Description:** Browse polishes by season

**Prerequisites:** NPI-031
</details>

<details id="npi-033">
<summary><b>NPI-033</b> | Add custom collections/boards feature [2pt] 🟡 ⬇️</summary>

**Tags:** `ui` `collections` `customization`

**Description:** Let users create named collections (e.g., "Date Night")

**Prerequisites:** NPI-025
</details>

<details id="npi-034">
<summary><b>NPI-034</b> | Implement cross-device data sync [2pt] 🟡 ⬆️</summary>

**Tags:** `sync` `backend`

**Description:** Sync user data across logged-in devices

**Prerequisites:** NPI-022, NPI-025
</details>

<details id="npi-035">
<summary><b>NPI-035</b> | Add collection export functionality [2pt] 🟡 ⬇️</summary>

**Tags:** `export` `csv` `data`

**Description:** Download user's collection as CSV file

**Prerequisites:** NPI-028
</details>

<details id="npi-036">
<summary><b>NPI-036</b> | Create user profile/settings page [1pt] 🟡 ➡️</summary>

**Tags:** `ui` `profile` `settings`

**Description:** Basic user profile and preferences

**Prerequisites:** NPI-022
</details>

---

## ✨ Milestone 3: Recommendations & Enhanced Browsing (Weeks 7-9)

**Progress:** 0/15 tickets | 0/46 points (0%)

| ID | Title | Pts | Status | Priority |
|---|---|:---:|:---:|:---:|
| [NPI-037](#npi-037) | Build recommendation engine | 5 | 🟡 | ⬆️ |
| [NPI-038](#npi-038) | Create "Recommended for You" section | 3 | 🟡 | ⬆️ |
| [NPI-039](#npi-039) | Add "Similar Shades" feature | 3 | 🟡 | ➡️ |
| [NPI-040](#npi-040) | Implement "Trending" polish highlighting | 3 | 🟡 | ⬇️ |
| [NPI-041](#npi-041) | Create curated lookbooks | 5 | 🟡 | ➡️ |
| [NPI-042](#npi-042) | Add color family quick filters | 3 | 🟡 | ⬆️ |
| [NPI-043](#npi-043) | Implement advanced filter panel | 3 | 🟡 | ⬆️ |
| [NPI-044](#npi-044) | Add sort options | 2 | 🟡 | ➡️ |
| [NPI-045](#npi-045) | Add "clear all filters" button | 2 | 🟡 | ⬇️ |
| [NPI-046](#npi-046) | Implement filter URL params | 3 | 🟡 | ➡️ |
| [NPI-047](#npi-047) | Support multiple photos per polish | 3 | 🟡 | ⬆️ |
| [NPI-048](#npi-048) | Add finish descriptions | 2 | 🟡 | ➡️ |
| [NPI-049](#npi-049) | Add "dupes" field | 2 | 🟡 | ⬇️ |
| [NPI-050](#npi-050) | Create image gallery/carousel | 3 | 🟡 | ⬆️ |
| [NPI-051](#npi-051) | Add "recently viewed" history | 2 | 🟡 | ⬇️ |

_Ticket details collapsed for brevity - expand milestones 2 & 4 and Infrastructure sections as needed_

---

## 📅 Milestone 4: Future Booking Foundation (Placeholder)

**Progress:** 0/8 tickets | 0/14 points (0%)

| ID | Title | Pts | Status | Priority |
|---|---|:---:|:---:|:---:|
| NPI-052 | Create booking interest form | 2 | 🟡 | ⬇️ |
| NPI-053 | Draft booking flow wireframes | 3 | 🟡 | ⬇️ |
| NPI-054 | Research calendar/scheduling tools | 1 | 🟡 | ⬇️ |
| NPI-055 | Document pricing structure requirements | 1 | 🟡 | ⬇️ |
| NPI-056 | Plan payment integration approach | 2 | 🟡 | ⬇️ |
| NPI-057 | Build simple contact/inquiry form | 3 | 🟡 | ➡️ |
| NPI-058 | Add "Book Appointment" CTA button | 2 | 🟡 | ➡️ |
| NPI-059 | Create services/pricing static page | 1 | 🟡 | ➡️ |

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

**Total:** 75 tickets | 189 story points  
**Completed:** 4 tickets (5.3%) | 6 points (3.2%)  
**In Progress:** 0 tickets  
**Not Started:** 71 tickets | 183 points  

### By Milestone
| Milestone | Tickets | Points | Done | Remaining |
|---|:---:|:---:|:---:|:---:|
| 🚀 M1: MVP Gallery | 21 | 50 | 4 ✅ | 17 (44pts) |
| 💎 M2: Personalization | 15 | 42 | 0 | 15 (42pts) |
| ✨ M3: Enhanced Browsing | 15 | 46 | 0 | 15 (46pts) |
| 📅 M4: Booking | 8 | 14 | 0 | 8 (14pts) |
| 🎨 Infrastructure | 16 | 37 | 0 | 16 (37pts) |

### By Priority
- 🔥 **Critical:** 11 tickets (4 done, 7 remaining)
- ⬆️ **High:** 28 tickets (0 done, 28 remaining)
- ➡️ **Medium:** 23 tickets
- ⬇️ **Low:** 13 tickets

### Quick Stats
- Average ticket: 2.5 points
- Milestone 1 velocity: 6 points completed
- Estimated M1 completion: 44 points remaining (~3-4 more sprints)

---

## 📝 Usage Guide

**For high-level planning:** Use the summary tables to see all tickets at a glance  
**For detailed work:** Expand the collapsible details for specific tickets  
**For navigation:** Click ticket IDs in tables to jump to detailed sections  
**For tracking:** Update status emojis and notes in ticket details  

**Need implementation details?** Check the `guides/` folder for step-by-step instructions
