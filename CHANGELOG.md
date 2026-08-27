# Changelog - Nail Polish Inventory

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Content pages for Charms, Stickers, and Accessories
- Mobile-first layout system refinements
- Accessibility improvements (ARIA labels, keyboard navigation)
- Performance optimizations
- Services/pricing page and contact/inquiry form (booking flow)
- Pre-appointment reminder nudging clients to review the Inspo Gallery

## [1.3.0] - 2026-08-26

### Added
- **"Book Appointment" booking flow**
  - Live CTA button in the nav (both Polishes and Inspo pages), linking to a Google Calendar Appointment Schedule
  - Documented workaround for Google's fixed-slot-duration limitation (short Duration + a Buffer time after decouples slot spacing from real appointment length)
- **Nail Inspo Gallery** (`/inspo/`) — new page mirroring 216 photos from Claire's Pinterest inspo board locally (`scripts/download_nails.py` → `public/inspo/`), sidestepping the still-pending Pinterest API approval entirely
  - Every photo tagged by **Color** (primary/dominant only, 13 categories including Black), **Season** (Spring/Summer/Fall/Winter), **Occasion** (Christmas/Valentine's Day/Halloween/Easter/New Year's/4th of July/Birthday/Everyday), and **Vibe** (14 style categories: Minimalist, Detailed, Floral, Geometric, Glam, French Tip, Ombré, Polka Dot, Stripes, Marble, Abstract, Animal Print, Whimsical, Elegant) — Season/Occasion/Vibe are all multi-label, since one design can span several
  - Four independent filter groups matching the Polishes page's filter UX and color-swatch styling; any tag with zero photos simply doesn't render as a filter option
  - `#floral #spring`-style hashtag overlay on each photo, plus a click-to-enlarge lightbox
  - Emoji icons on every Occasion and Vibe filter label
  - Data lives in `data/inspo.csv`; low-confidence tagging calls (142/216, mostly fuzzy season/vibe reads) logged in `docs/inspo-tagging-review.md` for manual spot-checking
- `.claude/launch.json` and `.vscode/tasks.json` for one-click local server preview (Ctrl+Shift+B in VS Code)

### Changed
- Inspo page moved from `inspo.html` to `inspo/index.html` for a clean URL (`/inspo/`, no `.html`) — matches how the site root already worked
- Home page nav now shows a live "Polishes" link (it had been left inside the commented-out placeholder block alongside the still-unbuilt Charms/Stickers/Accessories), matching the Inspo page's nav

### Fixed
- `dev` branch had drifted ~40 commits behind `main` (missing the 135-polish inventory refresh and the "Send colors to Claire" feature) — fast-forwarded to resync
- Inspo Gallery was completely broken on the live site: a GitHub Copilot Autofix commit added a `response.ok` check to the CSV fetch but accidentally deleted the line that parsed the response, leaving every page load throw and silently fail
- Inspo page had no `@media (max-width: 768px)` responsive rules at all (never carried over from the Polishes page when built from scratch), so "Book Appointment" overflowed off-screen on phones
- Moving `inspo.html` broke the old URL outright (404) for anyone with it bookmarked — added a redirect stub
- Two filter bugs in the Inspo page's own code, both caught in testing before shipping: a delimiter mismatch (CSV used `, ` for multi-value fields, the page's JS split on `;`) that silently dropped Yellow/Brown/Gold and 11 of 12 Vibe tags from the filters; and apostrophe values ("New Year's", "Valentine's Day") being HTML-escaped before storage in a way that never decoded back, so those two filters matched zero photos

## [1.2.0] - 2026-03-29

### Added
- **Ruby inventory workflow** for Mac-based updates
  - `helpers/merge_csv.rb` — merges a new raw inventory export into `data/polishes.csv`, matching on Number+Name (falls back to Number-only for unique numbers), preserving Brand and LocalImage, updating Links, Image Addresses, Colors, and Finishes; currently hard-codes the March 2026 export path/filename, so update those values in the script before each run
  - `scripts/mirror_images.rb` — Ruby port of the Python image mirror script; downloads images from Image Address URLs to `public/images/` and updates the LocalImage column in-place
- **March 2026 inventory export** — `POLISHES-03-2026 - polishes.csv` (107 polishes, raw)

### Changed
- **Expanded collection** from 60 to 135 polishes in `data/polishes.csv`
  - All 135 polishes have local images (LocalImage column fully populated)
- **Nav links hidden** — commented out `<ul class="nav-links">` block in `index.html`
  - Charms, Stickers, and Accessories were non-functional placeholders; "Polishes" alone as the sole item added no navigational value; code preserved in comments

## [1.1.0] - 2026-01-03

### Added
- **Glitter finish filter** with animated sparkle effect
  - Light-catching animation with pulsing opacity and rotation
  - Radial gradient sparkle particles for realistic glitter appearance
- **Local image storage** system
  - All 60 polish images downloaded to `/images/` folder
  - LocalImage column in CSV for offline-friendly browsing
  - mirror_images.py script for incremental image downloads
- **Cache-busting** for CSV loading to ensure instant updates
  - Timestamp query parameter (?v=Date.now()) on fetch requests
- **Color and Finish metadata** for all 60 polishes
  - Researched from official dndgel.com product descriptions
  - Multi-color support (e.g., "Purple, Pink", "Orange, Red")
  - fix_colors_accurate.py script for automated updates

### Changed
- **Expanded collection** from 33 to 60 DND gel polishes
- **Enhanced CSV parser** to handle quoted fields with internal commas
  - Properly splits multi-color values like "Orange, Red"
  - Strips surrounding quotes while preserving internal content
- **CSV structure** now includes 8 columns:
  - Brand, Number, Name, Link, Image Address, LocalImage, Color, Finish

### Fixed
- **Browser caching issue** preventing CSV updates from displaying
- **Multi-color parsing errors** where commas inside quoted fields broke parser
- **Incorrect color categorizations** (e.g., Starry Night was "Blue, Purple", now "Yellow, Gold")
- **Card image paths** now use LocalImage column instead of constructing from Number/Name

### Data Quality
- ✅ All 60 polishes verified against official product descriptions
- ✅ No color assumptions based on polish names
- ✅ Manual image analysis for 2 Cat Eye polishes lacking descriptions (#10, #12)

## [1.0.0] - 2026-01-01

### Initial Release

#### Added
- **Responsive gallery** with CSS Grid layout
  - Auto-fill columns with min/max sizing
  - Enhanced hover effects with lift and shadow
- **Color filtering** with 11 categories
  - Red, Pink, Orange, Yellow, Green, Blue, Purple, Brown, Neutral, Black, White
  - Color-coded filter buttons
  - Multi-color polish support
- **Finish filtering** with animated effects
  - 5 categories: Cream, Shimmer, Cat Eye, Mood Change, Sheer
  - Visual animations for each finish type
- **Multi-select filters** with combined logic
  - OR logic within categories (any selected color matches)
  - AND logic between categories (must match selected color AND finish)
- **Search functionality** (disabled by default)
  - Real-time search by polish name or number
  - Case-insensitive matching
  - Commented out with TODO markers for potential future use
- **Filter reset and active indicators**
  - Clear All Filters button
  - Visual indicators for active filters
- **Navigation structure**
  - Header with Studio Claire branding
  - Navigation links for future content pages
- **Design system**
  - Custom CSS variables for colors, spacing, typography
  - Inter font for body text
  - Playfair Display for headers
  - Professional color palette with rose gold accents
- **Performance optimizations**
  - Lazy loading for all images (loading="lazy")
  - Minimal dependencies (vanilla HTML/CSS/JavaScript)
  - Static site architecture

#### Technical Details
- Client-side CSV parsing with dynamic card generation
- XSS protection with textContent and escapeHtml()
- Mobile-first responsive design
- Semantic HTML structure
- Accessible color contrast ratios

---

## Version History Summary

| Version | Date | Description |
|---------|------|-------------|
| 1.3.0 | 2026-08-26 | Book Appointment booking flow + Nail Inspo Gallery (216 photos, Color/Season/Occasion/Vibe filters) |
| 1.2.0 | 2026-03-29 | Inventory refresh to 135 polishes + Ruby workflow + nav links hidden |
| 1.1.0 | 2026-01-03 | Data accuracy + Glitter filter + Local images + Cache-busting |
| 1.0.0 | 2026-01-01 | Initial release with 33 polishes, color/finish filters |

---

## Notes

### Breaking Changes
- **1.3.0:** `inspo.html` moved to `inspo/index.html` (now `/inspo/`) - old direct links to `inspo.html` still work via a redirect stub, but anything hardcoding the old path outside the repo (e.g. a Calendar event description) should be updated

### Deprecations
- Search functionality commented out but preserved in code for potential future use

### Data Source
- All polish information from dndgel.com
- Color and Finish data researched from official product descriptions
- Images downloaded locally for offline browsing
- Inspo Gallery photos mirrored from Claire's own Pinterest "nail-inspo" board, tagged via visual review (Color/Season/Occasion/Vibe) - see `docs/inspo-tagging-review.md` for the 142 photos flagged low-confidence on that tagging

### Known Issues
- Content pages (Charms, Stickers, Accessories) not yet implemented - pending inventory photos
- Mobile layout could benefit from dedicated mobile-first system (planned in NPI-014) - the Inspo page's mobile layout was fixed in 1.3.0, but this ticket is about a proper shared design system, not a one-off fix
- No accessibility audit yet (planned in NPI-019)
- No pre-appointment reminder nudging clients to review the Inspo Gallery before booking (NPI-060, requested by a friend/client - the gallery itself now exists, but nothing actively prompts clients to visit it)
- 142/216 Inspo Gallery photos have a low-confidence tag on their Season/Occasion/Vibe calls - not yet spot-checked (see `docs/inspo-tagging-review.md`)
