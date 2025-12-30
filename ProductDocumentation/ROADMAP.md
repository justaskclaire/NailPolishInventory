# Nail Polish Inventory & Inspiration - Personal Roadmap

This roadmap translates the ProductQuestions responses into a simple, high-level plan for a personal side project. Milestones are organized to deliver a minimal but useful experience quickly, then iterate with richer capabilities over time.

## Vision
Create a mobile-first web experience that helps friends and clients browse available nail polish shades, view swatches, and discover on-hand charms and accessories, with room to grow into favorites, wishlists, recommendations, and eventual booking/support features.

## Milestones & Phasing

### Milestone 1: MVP gallery and inventory (Weeks 1-3)
- **Deliverable:** Live mobile-first web page showcasing available shades with photos/swatches in a clean grid.
- **Key work:**
  - ✅ Build responsive gallery/grid of available shades only, sourced from existing inventory data and images.
  - ✅ Include basic filters (color, finish) with multi-color support for polishes with multiple color families.
  - ✅ Add multi-filter selection with AND logic (color + finish simultaneously).
  - ✅ Add search functionality for polish names and numbers.
  - ✅ Add lightweight pages/sections for charms, stickers, and accessories on hand.
  - ✅ Keep the design minimal and functional; prioritize speed to launch.
- **Dependencies:** Current inventory CSVs and images; simple hosting (static site is fine).
- **Success criteria:** Friends/clients can quickly browse the current collection, filter by multiple attributes, and see on-hand extras.
- **Progress:** ~85% complete - Gallery ✅, Color filter ✅, Finish filter ✅, Multi-color support ✅, Multi-filter AND logic ✅, Search ✅, Navigation ✅, Filter reset ✅, Content pages pending

### Milestone 2: Personalization basics (Weeks 4-6)
- **Deliverable:** Logged-in experience with personal tracking.
- **Key work:**
  - Enable account creation/login for personal use.
  - Add favorites, “on-hand” vs. “wishlist” tracking, and simple seasonal/occasion collections.
  - Persist personalization data locally or via lightweight backend/service.
- **Dependencies:** Lightweight auth + data store (Supabase/Firebase or local-first storage); polish detail endpoints if needed.
- **Success criteria:** Users can save favorite looks and track what they own versus want, with curated seasonal groupings.

### Milestone 3: Recommendations & polish browsing enhancements (Weeks 7-9)
- **Deliverable:** Smarter browsing and discovery.
- **Key work:**
  - Surface seasonal recommendations and curated sets on the gallery page.
  - Improve filtering (multi-filter chips, quick color families, finishes).
  - Add richer polish detail views (multiple swatches/photos, finish notes).
- **Dependencies:** Personalization data from Milestone 2; tagging scheme for seasons/finishes/colors.
- **Success criteria:** Browsing feels personalized and inspiring, with quicker navigation to desired shades.

### Milestone 4: Future booking foundation (High-level placeholder)
- **Deliverable:** Very light planning for potential appointment support.
- **Key work:**
  - Draft simple intake/interest form to gauge booking needs.
  - Outline potential scheduling/booking flow for later implementation.
- **Dependencies:** None—keep as a discovery item; can run as a static form.
- **Success criteria:** Clear next steps if/when booking becomes a priority; no full scheduling build yet.

## Risks & Considerations
- Keep scope lean early—focus on gallery, filters, and showcasing available shades.
- Plan hosting/deployment for mobile performance (e.g., static hosting + CDN for images).
- Ensure image handling stays organized as the collection grows.
- Reserve time each milestone for accessibility and mobile usability checks.
- Track image/licensing constraints if adding new swatches or client photos.

## Success in 3 Months
A live, mobile-friendly gallery that friends and clients actively use as a meaningful resource, with personalization features in progress and clear options for future booking expansion.
