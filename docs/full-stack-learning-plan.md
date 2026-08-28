# Full-Stack Learning Plan (Nail Polish Inventory as the sandbox)

**Status:** Idea captured 2026-08-27, not started. This is a *separate learning track*, not part of the live site's roadmap (`docs/TICKETS.md`) - the goal is to practice backend + frontend + CI/CD + testing, using this project's real data as low-stakes practice material, without touching the live client-facing site.

## Why this project works for it
- Small, already-understood domain (no time spent learning "the business," all energy goes to "the how")
- Real data already exists (`data/polishes.csv`, `data/inspo.csv`) - no fake seed data needed
- A real, already-felt pain point that CI/CD directly fixes: the manual `git checkout main && merge dev && push` dance done by hand all night
- A natural vertical slice already exists to rebuild: favorites / next-appt / "send to Claire" currently lives in browser localStorage only - moving it to a real backend is a genuine (not contrived) reason for a database and an API

## Ground rule
**Build this as a separate branch or fork, never directly on `main`.** The live site serves real clients booking real appointments - don't let a learning experiment risk breaking it.

## High-level phases

1. **Pick one small vertical slice, not the whole site.**
   Rebuild favorites/next-appt/send-to-Claire with a real backend instead of localStorage. Everything else (galleries, filters, booking link) stays static as-is.

2. **Backend**
   - Simple stack: Python + FastAPI, or Node + Express - whichever language you'd rather practice
   - SQLite to start (zero ops, one file, easy to reason about) - Postgres later if you want that experience too
   - A small REST API: create/read/delete favorite, create/read/delete next-appt pick

3. **Frontend**
   - Keep the existing HTML/CSS/JS - swap the storage layer (`localStorage.getItem/setItem`) for `fetch()` calls to the new API. Minimal UI rewrite, since the UI already exists and works.

4. **Unit tests**
   - Start with pure-function logic: the color-matching/filter logic, CSV or DB row parsing - these are the easiest, highest-value tests
   - Then test the API endpoints (a favorite you add shows up when you list favorites, etc.)
   - pytest (Python) or Jest (Node)

5. **Deployment automation (CI/CD)**
   - GitHub Actions: run tests on every push
   - Auto-deploy on green: backend needs real hosting now (GitHub Pages is static-only) - Render, Railway, or Fly.io all have simple free tiers for a small service + SQLite/Postgres
   - Frontend can stay on GitHub Pages, or move alongside the backend - either is fine to start

6. **Iterate from there**
   Once that one slice works end-to-end with tests and auto-deploy, there's a real menu of next steps: add auth (so Claire has an admin view distinct from client view), migrate more features, add the color-matching "dream feature" (NPI-072) as a real backend endpoint instead of client-side JS, etc.

## Not decided yet (pick these when you actually start)
- Language/framework (Python+FastAPI vs Node+Express)
- Hosting provider for the backend
- Whether the DB is SQLite the whole way or migrates to Postgres
