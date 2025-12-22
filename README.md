# Nail Polish Inventory

A simple, static web gallery for browsing my DND gel polish collection with color filtering.

## 🎨 Features
- Browse 33 polishes with images and product links
- Filter by color (11 categories: Red, Pink, Orange, Yellow, Green, Blue, Purple, Brown, Neutral, Black, White)
- Multi-color polish support - polishes with multiple color families appear in all relevant filters
- Filter by finish (5 categories: Cream, Shimmer, Cat Eye, Mood Change, Sheer)
- Multi-filter selection with AND logic (combine color + finish filters)
- Responsive grid layout
- Lazy-loaded images for performance
- Offline-friendly with local images

## 🚀 Quick Start
1. Open `index.html` in a web browser
2. Use the color filter dropdown to browse by color
3. Click any card to view the product page on dndgel.com

## 📁 Project Structure
```
├── index.html              # Main gallery page
├── polishes.csv            # Source data (Number, Name, Link, Image Address)
├── images/                 # Local product images
├── helpers/
│   ├── mirror_images.py    # Script to download images from CSV URLs
│   └── README-mirror-images.md
├── ProductDocumentation/   # Tickets, roadmap, implementation guides
└── reference/              # Original order PDFs
```

## 🛠️ Adding New Polishes
1. Add new row(s) to `polishes.csv` with Number, Name, Link, Image Address, Color, and Finish
2. For polishes with multiple colors, use comma-separated values in quotes: `"Purple, Pink"`
3. Run `python helpers/mirror_images.py` to download images
4. Cards are dynamically generated from CSV - no manual HTML updates needed
5. Verify color categorization from product page (never guess from name!)

## 📚 Documentation
- **[ProductDocumentation/TICKETS.md](ProductDocumentation/TICKETS.md)** - Full backlog (75 tickets)
- **[ProductDocumentation/ROADMAP.md](ProductDocumentation/ROADMAP.md)** - Roadmap and milestones
- **[helpers/README-mirror-images.md](helpers/README-mirror-images.md)** - How to use mirror_images.py

