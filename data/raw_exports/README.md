# Raw Exports

This folder stores raw inventory export CSVs before they are merged into `data/polishes.csv`.

## Naming Convention
`YYYY-MM-polishes.csv` — e.g., `2026-03-polishes.csv`

## Workflow
1. Export raw inventory CSV (6 columns: Number, Name, Link, Image Address, Color, Finish)
2. Place it here with the correct date-based filename
3. Run `helpers/merge_csv.rb` to merge it into `data/polishes.csv`
4. Run the appropriate mirror images script to download new images (see `scripts/README-mirror-images.md`)

## Files
| File | Date | Status |
|------|------|--------|
| [2026-03-polishes.csv](2026-03-polishes.csv) | March 2026 | Merged ✅ |
