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
| 1.1.0 | 2026-01-03 | Data accuracy + Glitter filter + Local images + Cache-busting |
| 1.0.0 | 2026-01-01 | Initial release with 33 polishes, color/finish filters |

---

## Notes

### Breaking Changes
- None yet - project is in active development phase

### Deprecations
- Search functionality commented out but preserved in code for potential future use

### Data Source
- All polish information from dndgel.com
- Color and Finish data researched from official product descriptions
- Images downloaded locally for offline browsing

### Known Issues
- Content pages (Charms, Stickers, Accessories) not yet implemented - pending inventory photos
- Mobile layout could benefit from dedicated mobile-first system (planned in NPI-014)
- No accessibility audit yet (planned in NPI-019)
