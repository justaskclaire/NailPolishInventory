# Nail Polish Inventory

A simple, static web gallery for browsing my DND gel polish collection with color and finish filtering.

## 🎨 Features
- Browse 60 polishes with images and product links
- Filter by color (11 categories with color-coded buttons: Red, Pink, Orange, Yellow, Green, Blue, Purple, Brown, Neutral, Grey, Gold)
- Multi-color polish support - polishes with multiple color families appear in all relevant filters
- Filter by finish with animated effects (6 categories: Cream, Shimmer, Cat Eye, Mood Change, Sheer, Glitter)
- Multi-select checkbox filters with OR logic within categories, AND between categories
- Professional design system with custom typography (Inter + Playfair Display)
- Responsive grid layout with enhanced hover effects
- Lazy-loaded images for performance
- Offline-friendly with local images
- Cache-busting CSV loading for instant updates

## 🚀 Quick Start
1. Run `python -m http.server 8000` from the project directory
2. Open http://localhost:8000 in a web browser
3. Use the color and finish filters to browse by attributes
4. Click any card to view the product page on dndgel.com

## 📁 Project Structure
```
├── index.html              # Main gallery page
├── polishes.csv            # Source data (Brand, Number, Name, Link, Image Address, LocalImage, Color, Finish)
├── images/                 # Local product images
├── helpers/
│   ├── mirror_images.py    # Script to download images from CSV URLs
│   ├── fix_colors_accurate.py  # Script to update Color/Finish from official product descriptions
│   └── README-mirror-images.md
├── ProductDocumentation/   # Tickets, roadmap, implementation guides
└── reference/              # Original order PDFs
```

## 🛠️ Adding New Polishes
1. Add new row(s) to `polishes.csv` with Brand, Number, Name, Link, Image Address
2. Run `python helpers/mirror_images.py` to download images and add LocalImage paths
3. Research each polish's Color and Finish from official product page descriptions (never guess from name!)
4. For polishes with multiple colors, use comma-separated values in quotes: `"Purple, Pink"`
5. Update Color and Finish columns in CSV
6. Cards are dynamically generated from CSV - no manual HTML updates needed

## 📚 Documentation
- **[ProductDocumentation/TICKETS.md](ProductDocumentation/TICKETS.md)** - Full backlog (75 tickets)
- **[ProductDocumentation/ROADMAP.md](ProductDocumentation/ROADMAP.md)** - Roadmap and milestones
- **[helpers/README-mirror-images.md](helpers/README-mirror-images.md)** - How to use mirror_images.py

