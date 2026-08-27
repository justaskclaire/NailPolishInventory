# Nail Polish Inventory

A simple, static web experience for Studio Claire's nail business: a browsable gel polish gallery, a Pinterest-sourced inspiration gallery, and a live appointment-booking link — no backend, no build step, no login.

## 🎨 Features

### Polishes (`/`)
- Browse 135 polishes with images and product links
- Filter by color (color-coded buttons) and finish (with animated effects: Cream, Shimmer, Cat Eye, Mood Change, Sheer, Glitter)
- Multi-select checkbox filters with OR logic within categories, AND between categories
- Favorites (❤️) and "Next Appointment" (📅) marking, persisted in `localStorage` — no login required
- "📋 Send colors to Claire" — copies picked polishes to the clipboard to hand off before an appointment
- Lazy-loaded local images, cache-busting CSV loading for instant updates

### Inspo (`/inspo/`)
- 216 nail-art inspiration photos mirrored locally from Claire's Pinterest board
- Filter by **Color** (primary/dominant color only), **Season** (Spring/Summer/Fall/Winter), **Occasion** (Christmas/Valentine's Day/Halloween/Easter/New Year's/4th of July/Birthday/Everyday), and **Vibe** (Minimalist, Detailed, Floral, Geometric, Glam, French Tip, Ombré, Polka Dot, Stripes, Marble, Abstract, Animal Print, Whimsical, Elegant) — Season/Occasion/Vibe are multi-label, since one design can span several
- Hashtag overlay on each photo, click-to-enlarge lightbox

### Booking
- "Book Appointment" nav CTA links directly to a Google Calendar Appointment Schedule (no custom booking backend)

## 🚀 Quick Start
1. Run `python -m http.server 8000` from the project directory (or, in VS Code, press **Ctrl+Shift+B** — see `.vscode/tasks.json`)
2. Open http://localhost:8000 for the Polishes gallery, or http://localhost:8000/inspo/ for the Inspo gallery

## 📁 Project Structure
```
├── index.html                    # Polishes gallery (home page)
├── inspo/index.html              # Inspo gallery (served at /inspo/)
├── inspo.html                    # Redirect stub → inspo/ (keeps old bookmarks/links working)
├── privacy-policy.html           # GDPR/CCPA privacy policy (for the Pinterest API application)
├── data/
│   ├── polishes.csv              # Master polish data (site reads this)
│   ├── inspo.csv                 # Inspo photo tags (Filename,Colors,Seasons,Occasions,Vibes,Confidence)
│   └── raw_exports/              # Raw inventory export CSVs before merging
├── public/
│   ├── images/                   # Local polish product images
│   └── inspo/                    # Local Inspo gallery photos (nail-001.jpg ... nail-216.jpg)
├── scripts/
│   ├── download_nails.py         # Downloads Inspo photos from Pinterest pin URLs
│   ├── mirror_images.py          # Downloads polish images from CSV URLs (Windows/PC)
│   └── mirror_images.rb          # Same, for Mac (Ruby)
├── helpers/
│   └── merge_csv.rb              # Merges a new raw inventory export into data/polishes.csv
└── docs/                         # Tickets, roadmap, planning docs, tagging review
```

## 🛠️ Adding New Polishes
1. Add new row(s) to `data/polishes.csv` with Brand, Number, Name, Link, Image Address
2. Run `scripts/mirror_images.py` (PC) or `scripts/mirror_images.rb` (Mac) to download images and add LocalImage paths
3. Research each polish's Color and Finish from official product page descriptions (never guess from name!)
4. For polishes with multiple colors, use comma-separated values in quotes: `"Purple, Pink"`
5. Cards are dynamically generated from the CSV — no manual HTML updates needed

## 🖼️ Adding New Inspo Photos
1. Add new Pinterest pin image URLs to `scripts/download_nails.py`, run it to download into `public/inspo/`
2. Tag each new photo's Colors/Seasons/Occasions/Vibes in `data/inspo.csv` (see the existing rows for the format and vocabulary)
3. The Inspo page's filters and hashtag overlays are generated automatically from the CSV

## 📚 Documentation
- **[docs/TICKETS.md](docs/TICKETS.md)** — Full backlog, current status, and what shipped vs. what's still open
- **[docs/ROADMAP.md](docs/ROADMAP.md)** — Milestone roadmap
- **[docs/inspo-tagging-review.md](docs/inspo-tagging-review.md)** — Low-confidence Inspo photo tags flagged for a manual spot-check
- **[CHANGELOG.md](CHANGELOG.md)** — Version history
- **[.copilot/STANDUP.md](.copilot/STANDUP.md)** — Running day-to-day change log
