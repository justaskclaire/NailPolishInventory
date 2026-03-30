# How to Use the Mirror Images Scripts

> **Before running a data import, note which machine you're on:**
> - **Mac** → use `mirror_images.py` (Python)
> - **PC / Windows** → use `mirror_images.rb` (Ruby)
>
> If starting a data import in a new chat session, tell your assistant which machine you're using so the correct script is selected.

## Purpose
Downloads product images from URLs in your CSV and saves them locally to the `images/` folder. Updates the `LocalImage` column in `data/polishes.csv`.

---

## Which Script to Use?

| Machine | Script | Run with |
|---------|--------|----------|
| **Mac** | `scripts/mirror_images.py` | `python3 scripts/mirror_images.py` |
| **PC / Windows** | `scripts/mirror_images.rb` | `ruby scripts/mirror_images.rb` |

Both scripts do the same thing — they just use different runtimes available on each platform.

---

## Step-by-Step Instructions

### 1. Update Your CSV
Add your new polish(es) to `data/polishes.csv` with these columns:
- **Number** - Polish number (e.g., "67", "243")
- **Name** - Polish name (e.g., "Fire Engine Red")
- **Link** - Product page URL
- **Image Address** - Direct image URL from the product page

### 2. Run the Script

**On Mac** (in Terminal):
```bash
python3 scripts/mirror_images.py
```

**On PC** (in PowerShell or Command Prompt):
```powershell
ruby scripts/mirror_images.rb
```

### 3. What It Does
- Reads `polishes.csv`
- Downloads each image from the "Image Address" column
- Saves images to `images/` folder as `{Number}-{Name}.{ext}`
- Skips images that already exist (won't re-download)
- Creates `DND Inventory - with_local_images.csv` with a new "LocalImage" column

### 4. Output
You'll see progress like:
```
[1/33] Downloaded: 67-Fire_Engine_Red.jpg
[2/33] Skipped (already exists): 39-Fire_Brick.jpg
...
Done.
Downloaded: 2, Skipped: 31, Failed: 0
```

### 5. What to Check
- ✅ New images appear in `images/` folder
- ✅ `DND Inventory - with_local_images.csv` has the "LocalImage" column filled in
- ⚠️ If any downloads fail, check the image URL is valid

## Notes
- Script automatically skips already-downloaded images (efficient for adding new polishes)
- Filenames are sanitized to be Windows-safe
- Retries failed downloads up to 3 times
- Default timeout: 25 seconds per image
