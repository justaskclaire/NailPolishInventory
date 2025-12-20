# Implementation Guide: NPI-001

## Ticket Information
**ID:** NPI-001  
**Title:** Set up project repository and hosting  
**Points:** 1  
**Priority:** 🔥 Critical  
**Tags:** `infrastructure` `setup`

---

## Overview
Initialize a Git repository for the nail polish inventory project and configure hosting on Vercel or Netlify for easy deployment and continuous delivery.

---

## Acceptance Criteria
- [ ] Git repository is initialized in the project directory
- [ ] `.gitignore` file is created with appropriate exclusions
- [ ] Initial commit includes all current project files
- [ ] Remote repository is set up (GitHub/GitLab/Bitbucket)
- [ ] Hosting platform account is created (Vercel or Netlify)
- [ ] Project is connected to hosting platform
- [ ] Site deploys successfully and is accessible via public URL
- [ ] Automatic deployments are configured (commits trigger rebuilds)

---

## Prerequisites
None - This is the foundation task

---

## Technical Approach

### Repository Strategy
- Use Git for version control
- Host on GitHub (preferred for Vercel integration)
- Use main/master branch for production
- Set up .gitignore to exclude unnecessary files

### Hosting Platform Choice
**Recommended: Vercel**
- Free tier suitable for static sites
- Automatic deployments from Git
- Zero configuration for static HTML
- Fast global CDN
- Custom domain support

**Alternative: Netlify**
- Similar features to Vercel
- Also free for static sites
- Drag-and-drop deployment option

---

## Implementation Steps

### Step 1: Verify Current Project Structure
**Location:** `C:\PersonalProjects\NailPolishInventory`  
**Action:** Confirm these files exist:
```
NailPolishInventory/
├── index.html
├── polishes.csv
├── mirror_images.py
├── images/
│   └── [33 polish images]
├── ProductDocumentation/
│   ├── ROADMAP.md
│   ├── TICKETS.md
│   └── guides/
└── README.md
```

### Step 2: Create .gitignore File
**File:** `.gitignore` (create at project root)  
**Action:** Add these exclusions:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# OS files
.DS_Store
Thumbs.db
desktop.ini

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Temporary files
*.tmp
*.log

# Environment variables
.env
.env.local

# Build outputs (if adding build tools later)
dist/
build/
```

### Step 3: Initialize Git Repository
**Location:** Project root directory  
**Commands:**
```bash
cd C:\PersonalProjects\NailPolishInventory
git init
git add .
git commit -m "Initial commit: Nail Polish Inventory MVP"
```

**Verification:**
```bash
git status
git log
```

### Step 4: Create GitHub Repository
**Action:** Via GitHub website or CLI

**Option A: GitHub Website**
1. Go to https://github.com/new
2. Repository name: `NailPolishInventory` (or your preferred name)
3. Description: "Personal nail polish inventory and gallery"
4. Visibility: Private (or Public if you want to share)
5. **Do NOT** initialize with README, .gitignore, or license (we have these)
6. Click "Create repository"

**Option B: GitHub CLI** (if installed)
```bash
gh repo create NailPolishInventory --private --source=. --remote=origin
```

### Step 5: Connect Local to Remote Repository
**Commands:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/NailPolishInventory.git
git branch -M main
git push -u origin main
```

**Replace:** `YOUR_USERNAME` with your GitHub username

**Verification:**
```bash
git remote -v
```

### Step 6: Set Up Vercel Hosting
**Action:** Create account and connect repository

**Steps:**
1. Go to https://vercel.com/signup
2. Sign up with GitHub account (easiest integration)
3. Click "Add New..." → "Project"
4. Import your `NailPolishInventory` repository
5. Configure project:
   - **Framework Preset:** Other
   - **Root Directory:** `./`
   - **Build Command:** Leave empty (static site)
   - **Output Directory:** `./`
6. Click "Deploy"

**Expected Result:** Vercel will deploy your site and provide a URL like:
`https://nail-polish-inventory.vercel.app`

### Step 7: Test Deployment
**Action:** Verify the site is live

**Checks:**
- [ ] Visit the Vercel URL
- [ ] index.html loads correctly
- [ ] All polish images display
- [ ] CSS styling is applied
- [ ] Links work properly
- [ ] Mobile responsive layout works

### Step 8: Configure Custom Domain (Optional)
**Action:** If you have a custom domain

**Steps:**
1. In Vercel project settings → Domains
2. Add your domain
3. Follow DNS configuration instructions
4. Wait for DNS propagation (up to 48 hours)

---

## Testing Checklist

### Repository Testing
- [ ] `.git` directory exists in project root
- [ ] `git status` shows "nothing to commit, working tree clean"
- [ ] `git log` shows initial commit
- [ ] GitHub repository contains all files
- [ ] `images/` folder is tracked in Git

### Deployment Testing
- [ ] Vercel dashboard shows successful deployment
- [ ] Public URL is accessible
- [ ] All images load (check network tab)
- [ ] No 404 errors in console
- [ ] Site works on mobile devices
- [ ] HTTPS is enabled

### Continuous Deployment Testing
- [ ] Make a small change (e.g., edit README.md)
- [ ] Commit and push to GitHub
- [ ] Vercel automatically triggers new deployment
- [ ] Changes appear on live site within 1-2 minutes

---

## Files Created
1. `.gitignore` - Git exclusion rules
2. `.git/` - Git repository metadata (created by git init)

---

## Files Modified
None (unless you want to update README.md with the live URL)

---

## Dependencies
- Git installed on local machine
- GitHub account
- Vercel account
- Internet connection

---

## Rollback Plan
If issues occur:
- **Repository:** Delete `.git` folder to remove Git tracking
- **Hosting:** Delete project from Vercel dashboard
- **Remote:** Delete GitHub repository

Local files remain unchanged - you can always re-initialize.

---

## Follow-up Tickets
- **NPI-002:** Create mobile-first responsive grid layout
- **NPI-003:** Import existing CSV inventory data into gallery
- **NPI-013:** Deploy MVP to production (continuous deployment now set up!)

---

## Notes for Implementation
- Keep repository private initially until ready to share
- Vercel free tier includes:
  - Unlimited deployments
  - Automatic HTTPS
  - Global CDN
  - Analytics (basic)
- Consider adding a `.gitattributes` file for line ending consistency
- Document the live URL in README.md for easy reference

---

## Post-Setup Configuration

### Optional: Add Deployment Badge to README
**File:** `README.md`  
**Add at top:**
```markdown
# Nail Polish Inventory

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/NailPolishInventory)

🌐 **Live Site:** https://your-project.vercel.app
```

### Optional: Set Up Branch Protection
**Location:** GitHub repository settings → Branches

**Recommended rules:**
- Require pull request reviews before merging
- Require status checks to pass
- Enable "Do not allow bypassing the above settings"

---

## Estimated Time
- Git setup and initial commit: 5 minutes
- GitHub repository creation: 3 minutes
- Vercel account and deployment: 7 minutes
- Testing and verification: 5 minutes
- **Total: ~20 minutes**

---

## Success Criteria
✅ **DONE** when:
1. You can run `git log` and see commits
2. You can visit your GitHub repository and see all files
3. You can visit your Vercel URL and see the site live
4. Making a change and pushing triggers automatic redeployment
