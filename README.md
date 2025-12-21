# Nail Polish Inventory

A simple, static web gallery for browsing my DND gel polish collection with color filtering.

## 🎨 Features
- Browse 33 polishes with images and product links
- Filter by color (11 categories: Red, Pink, Orange, Yellow, Green, Blue, Purple, Brown, Neutral, Black, White)
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
1. Add new row(s) to `polishes.csv` with Number, Name, Link, and Image Address
2. Run `python helpers/mirror_images.py` to download images
3. Update `index.html` with new card entries
4. Verify color categorization from product page (never guess from name!)

## 📚 Documentation
- **[ProductDocumentation/TICKETS.md](ProductDocumentation/TICKETS.md)** - Full backlog (75 tickets)
- **[ProductDocumentation/ROADMAP.md](ProductDocumentation/ROADMAP.md)** - Roadmap and milestones
- **[helpers/README-mirror-images.md](helpers/README-mirror-images.md)** - How to use mirror_images.py

