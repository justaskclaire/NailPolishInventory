# Project Tickets - Nail Polish Inventory

## Ticket Format Guide
- **ID:** Unique identifier (NPI-###)
- **Points:** Fibonacci scale - 1 (trivial), 2 (simple), 3 (moderate), 5 (complex), 8 (very complex), 13 (epic)
- **Status:** 🟡 Not Started | 🔵 In Progress | 🟢 Done | 🔴 Blocked
- **Priority:** 🔥 Critical | ⬆️ High | ➡️ Medium | ⬇️ Low

---

## 🚀 Milestone 1: MVP Gallery & Inventory (Weeks 1-3)

### Quick Wins

**NPI-001** | Set up project repository and hosting  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `infrastructure` `setup`  
**Description:** Initialize Git repo and configure hosting on Vercel or Netlify

**NPI-002** | Create mobile-first responsive grid layout  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `frontend` `layout` `mobile`  
**Description:** Build responsive CSS grid for polish card display

**NPI-003** | Import existing CSV inventory data  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `data` `import`  
**Description:** Parse polishes.csv and load into gallery view

**NPI-004** | Implement image optimization and lazy loading  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `performance` `images`  
**Description:** Add lazy loading for polish swatches and optimize image delivery

**NPI-005** | Add basic color filter  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `filter` `ui`  
**Description:** Create dropdown or chip-based color family filter

**NPI-006** | Add brand filter functionality  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `filter` `ui`  
**Description:** Filter polishes by brand (DND, etc.)

**NPI-007** | Add finish filter  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `filter` `ui`  
**Description:** Filter by finish type (shimmer, matte, glitter, cream, etc.)

**NPI-008** | Build search bar with name/number filtering  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `search` `ui`  
**Description:** Implement real-time search for polish names and numbers

**NPI-009** | Create "Charms" static page  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `static-pages`  
**Description:** Display current charm inventory with photos

**NPI-010** | Create "Stickers" static page  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `static-pages`  
**Description:** Display current sticker inventory with photos

**NPI-011** | Create "Accessories" static page  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `static-pages`  
**Description:** Display other accessories (tools, files, etc.)

**NPI-012** | Add navigation between pages  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `navigation` `ui`  
**Description:** Create header/menu navigation for gallery and extras pages

**NPI-013** | Deploy MVP to production  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `deployment` `infrastructure`  
**Description:** Push live to production hosting

### Medium Complexity

**NPI-014** | Design and implement mobile-first layout system  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `design-system` `layout` `mobile`  
**Description:** Create consistent spacing, breakpoints, and responsive patterns

**NPI-015** | Create polish detail modal/page  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `modal` `detail-view`  
**Description:** Show enlarged swatch and polish details when clicked

**NPI-016** | Implement multi-filter selection  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `filter` `ui`  
**Description:** Allow combining color + brand + finish filters simultaneously

**NPI-017** | Add filter reset and active indicators  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `filter` `ux`  
**Description:** Show active filters and provide clear all button

### Validation & Polish

**NPI-018** | Run mobile usability testing  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `testing` `mobile` `ux`  
**Description:** Test on 3+ different mobile devices and browsers

**NPI-019** | Add basic accessibility checks  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `accessibility` `a11y`  
**Description:** Add ARIA labels, keyboard navigation, and screen reader support

**NPI-020** | Optimize page load performance  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `performance` `optimization`  
**Description:** Run Lighthouse audit and fix critical issues

**NPI-021** | Set up analytics tracking  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `analytics` `tracking`  
**Description:** Track page views, filter usage, and user behavior

---

## 💎 Milestone 2: Personalization Basics (Weeks 4-6)

### Authentication & Data

**NPI-022** | Set up authentication system  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `auth` `backend` `firebase` `supabase`  
**Description:** Implement Firebase or Supabase authentication

**NPI-023** | Create login/signup UI flow  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `auth` `ui` `forms`  
**Description:** Build user-friendly authentication forms and flows

**NPI-024** | Design user data schema  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `database` `schema` `planning`  
**Description:** Define data structure for favorites, on-hand, wishlist

**NPI-025** | Implement backend data persistence  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `backend` `database` `api`  
**Description:** Build data layer for storing user preferences and collections

### User Features

**NPI-026** | Add "Favorite" button to polish cards  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `favorites` `interaction`  
**Description:** Heart icon toggle to save favorite polishes

**NPI-027** | Create "My Favorites" page  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `page` `favorites`  
**Description:** View all saved favorite polishes

**NPI-028** | Build "On-Hand" vs "Wishlist" toggle  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `collection` `tracking`  
**Description:** Allow users to mark polishes as owned or wanted

**NPI-029** | Create "My Collection" page  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `page` `collection`  
**Description:** Display on-hand and wishlist tabs

**NPI-030** | Add collection counters  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `ui` `stats`  
**Description:** Show totals for favorites/on-hand/wishlist items

**NPI-031** | Create seasonal collection tags  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `tags` `collections`  
**Description:** Tag polishes with Spring, Summer, Fall, Winter

**NPI-032** | Build "Seasonal Collections" browsing page  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `ui` `page` `collections`  
**Description:** Browse polishes by season

**NPI-033** | Add custom collections/boards feature  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `ui` `collections` `customization`  
**Description:** Let users create named collections (e.g., "Date Night")

### Data Management

**NPI-034** | Implement cross-device data sync  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `sync` `backend`  
**Description:** Sync user data across logged-in devices

**NPI-035** | Add collection export functionality  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `export` `csv` `data`  
**Description:** Download user's collection as CSV file

**NPI-036** | Create user profile/settings page  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `ui` `profile` `settings`  
**Description:** Basic user profile and preferences

---

## ✨ Milestone 3: Recommendations & Enhanced Browsing (Weeks 7-9)

### Discovery Features

**NPI-037** | Build recommendation engine  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `algorithm` `recommendations` `backend`  
**Description:** Generate polish suggestions based on favorites and season

**NPI-038** | Create "Recommended for You" section  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `recommendations` `homepage`  
**Description:** Display personalized recommendations on homepage

**NPI-039** | Add "Similar Shades" feature  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `recommendations` `detail-view`  
**Description:** Show similar polishes on detail pages

**NPI-040** | Implement "Trending" polish highlighting  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `analytics` `ui` `trending`  
**Description:** Highlight popular polishes based on views/favorites

**NPI-041** | Create curated lookbooks  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `collections` `curation`  
**Description:** Build sets like "Date Night", "Beach Vibes", etc.

### Filter & Browse Enhancements

**NPI-042** | Add color family quick filters  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `filter` `ui` `color`  
**Description:** Quick-select buttons for reds, pinks, blues, etc.

**NPI-043** | Implement advanced filter panel  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `filter` `ui` `chips`  
**Description:** Multi-select chip-based filtering interface

**NPI-044** | Add sort options  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `sorting` `ui`  
**Description:** Sort by name, number, recently added, popularity

**NPI-045** | Add "clear all filters" button  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `filter` `ux`  
**Description:** One-click to reset all filters

**NPI-046** | Implement filter URL params  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `filter` `routing` `sharing`  
**Description:** Enable shareable links with active filters

### Polish Details

**NPI-047** | Support multiple photos per polish  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `images` `detail-view`  
**Description:** Show bottle, swatch, and on-hand photos

**NPI-048** | Add finish descriptions  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `detail-view`  
**Description:** Include finish type and application notes

**NPI-049** | Add "dupes" field  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `content` `detail-view` `comparison`  
**Description:** Show similar polishes from other brands

**NPI-050** | Create image gallery/carousel  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `ui` `images` `carousel`  
**Description:** Swipeable photo gallery for polish details

**NPI-051** | Add "recently viewed" history  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `tracking` `ui` `history`  
**Description:** Track and display recently viewed polishes

---

## 📅 Milestone 4: Future Booking Foundation (Placeholder)

### Research & Planning

**NPI-052** | Create booking interest form  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `research` `forms` `booking`  
**Description:** Survey form to gauge booking feature needs

**NPI-053** | Draft booking flow wireframes  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `design` `wireframes` `booking`  
**Description:** Design user journey for appointment scheduling

**NPI-054** | Research calendar/scheduling tools  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `research` `tools` `booking`  
**Description:** Evaluate Calendly, Acuity, custom solutions

**NPI-055** | Document pricing structure requirements  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `planning` `pricing` `booking`  
**Description:** Define service pricing and time estimates

**NPI-056** | Plan payment integration approach  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬇️ Low  
**Tags:** `planning` `payments` `stripe` `square`  
**Description:** Design payment flow with Stripe or Square

### Light Implementation

**NPI-057** | Build simple contact/inquiry form  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `forms` `contact` `ui`  
**Description:** Basic form for appointment inquiries

**NPI-058** | Add "Book Appointment" CTA button  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `ui` `cta` `booking`  
**Description:** Prominent button linking to contact form

**NPI-059** | Create services/pricing static page  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `content` `static-pages` `pricing`  
**Description:** Display service menu and pricing

---

## 🎨 Ongoing & Infrastructure

### Design System

**NPI-060** | Build reusable component library  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** 🔥 Critical  
**Tags:** `design-system` `components` `ui`  
**Description:** Create buttons, cards, modals, and other UI components

**NPI-061** | Define brand color palette  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `design-system` `branding` `colors`  
**Description:** Establish primary, secondary, and accent colors

**NPI-062** | Create typography system  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `design-system` `typography` `spacing`  
**Description:** Define font scales, weights, and spacing units

**NPI-063** | Design loading states and skeletons  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `design-system` `ui` `loading`  
**Description:** Create skeleton screens and loading indicators

### Content & Data Management

**NPI-064** | Create admin interface  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `admin` `cms` `backend`  
**Description:** UI for adding/editing polish entries

**NPI-065** | Build image upload pipeline  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `images` `upload` `optimization`  
**Description:** Automated image optimization on upload

**NPI-066** | Set up automated data backup  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `backup` `infrastructure` `database`  
**Description:** Scheduled backups of user data and inventory

**NPI-067** | Implement bulk CSV import/update  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `import` `csv` `admin`  
**Description:** Mass update inventory from CSV files

### Quality & Performance

**NPI-068** | Set up error tracking  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `monitoring` `errors` `sentry`  
**Description:** Implement Sentry or similar error tracking

**NPI-069** | Comprehensive accessibility audit  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `accessibility` `a11y` `audit`  
**Description:** Full WCAG compliance check and fixes

**NPI-070** | Add PWA features  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `pwa` `offline` `mobile`  
**Description:** Offline support and install prompt

**NPI-071** | Optimize images with WebP/AVIF  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `performance` `images` `optimization`  
**Description:** Convert to modern image formats

**NPI-072** | Add SEO meta tags  
📊 **Points:** 1 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `seo` `meta-tags` `og-image`  
**Description:** Implement proper meta tags and OpenGraph images

### Testing

**NPI-073** | Write unit tests for critical functions  
📊 **Points:** 5 | **Status:** 🟡 Not Started | **Priority:** ⬆️ High  
**Tags:** `testing` `unit-tests` `quality`  
**Description:** Test filters, search, and data operations

**NPI-074** | Set up E2E testing  
📊 **Points:** 3 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `testing` `e2e` `playwright` `cypress`  
**Description:** Automate main user flow testing

**NPI-075** | Create QA checklist  
📊 **Points:** 2 | **Status:** 🟡 Not Started | **Priority:** ➡️ Medium  
**Tags:** `testing` `qa` `checklist`  
**Description:** Release readiness checklist

---

## 🚀 Recommended Sprint Plan

### Sprint 1: Foundation Setup (13 points)
- **NPI-001** - Set up project repository (1pt)
- **NPI-002** - Create mobile-first grid (2pt)
- **NPI-003** - Import CSV inventory (1pt)
- **NPI-004** - Image optimization (2pt)
- **NPI-005** - Add color filter (3pt)
- **NPI-006** - Add brand filter (2pt)
- **NPI-012** - Add navigation (2pt)

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

### Sprint 4+: Personalization
Start Milestone 2 with authentication and user features

---

## 📊 Project Summary

**Total Tickets:** 75  
**Total Story Points:** ~189

### By Milestone:
- **Milestone 1 (MVP):** 21 tickets, ~50 points (~4-5 sprints)
- **Milestone 2 (Personalization):** 15 tickets, ~42 points (~3-4 sprints)
- **Milestone 3 (Enhanced Browsing):** 15 tickets, ~46 points (~3-4 sprints)
- **Milestone 4 (Booking):** 8 tickets, ~14 points (~1-2 sprints)
- **Ongoing/Infrastructure:** 16 tickets, ~37 points (continuous)

### By Priority:
- 🔥 **Critical:** 11 tickets
- ⬆️ **High:** 28 tickets
- ➡️ **Medium:** 23 tickets
- ⬇️ **Low:** 13 tickets

---

## 📝 How to Update Tickets

When working on a ticket:
1. Change status from 🟡 to 🔵 when starting
2. Add notes in the Description field as needed
3. Update to 🟢 when complete
4. Mark 🔴 if blocked with blocker details

Example:
```
**NPI-001** | Set up project repository
📊 **Points:** 1 | **Status:** 🟢 Done | **Priority:** 🔥 Critical
**Tags:** `infrastructure` `setup`
**Description:** Initialize Git repo and configure hosting on Vercel
**Notes:** Deployed to nailpolish.vercel.app - using Vercel free tier
```
