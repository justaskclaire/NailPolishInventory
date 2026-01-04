# Milestone 3: Pinterest Integration & Visual Inspiration - Planning Document

**Status:** 🛑 ON HOLD - Creating Privacy Policy for Pinterest API Application  
**Target Duration:** TBD (pending Pinterest API approval)  
**Estimated Effort:** 2-3 weeks (after API access granted)  
**Created:** January 3, 2026  
**Approach:** Pinterest API Integration (not manual/static)

**TODO:**
- [ ] Complete privacy policy document (privacy-policy.html)
- [ ] Deploy privacy policy to publicly accessible URL
- [ ] Submit Pinterest API Trial access application with privacy policy link
- [ ] Wait for approval (1-3 business days)
- [ ] Resume implementation at Phase 0 after approval

---

## 0. Core Vision: Pinterest-Powered Nail Design Flow

### The Client Experience
1. **Browse Inspiration** - Scroll through Pinterest nail designs (your board or search term)
2. **Select Designs** - Pick one or multiple designs that inspire them
3. **Get Polish Suggestions** - System analyzes design colors and suggests your polishes
4. **Lock or Customize** - Accept suggestions or pick different colors

### Why This Matters
- **For Clients:** Visual-first discovery (they know what they want to see, not polish names)
- **For Artist:** Streamlines consultation, reduces "I don't know what I want" appointments
- **For Business:** Unique differentiator, professional tool, time-saver

### Technical Requirements
- Pinterest API integration (boards or search)
- Color extraction from Pinterest images
- Color matching algorithm (design colors → your polish inventory)
- UI for browsing, selecting, and managing suggestions
- Mobile-first design (clients use phones)

---

## 1. Pinterest API Integration: What's Required

### Application Process (Before We Can Start)
**Step 1: Trial Access (~1-3 business days)**
- Create Pinterest Business account
- Submit app registration with:
  - App name & description
  - Use case explanation
  - Privacy policy (required)
  - Verified email
- Await approval (reviewed daily)

**Step 2: OAuth Setup**
- Configure redirect URI (localhost for testing)
- Get App ID and App Secret
- Build OAuth 2.0 authentication flow
- Request scopes: `boards:read`, `pins:read`

**Step 3: Testing with Trial Access**
- Trial access has daily rate limits
- Pins/boards created are sandbox-only (not public)
- Read access to boards/pins works for testing
- Good for development/POC

**Step 4: Upgrade to Standard Access (when ready for production)**
- Submit video demo of OAuth flow
- Show live Pinterest integration
- Higher rate limits (per minute, not per day)
- Full production access

### Pinterest API Capabilities
**What We Can Do:**
- ✅ Read user's boards
- ✅ List pins from specific board
- ✅ Search pins by keyword
- ✅ Get pin details (image URL, description, colors)
- ✅ Access pin images

**What We Cannot Do:**
- ❌ Access any user's private boards without their OAuth consent
- ❌ Bypass rate limits
- ❌ Use Pinterest content without proper attribution

### Rate Limits & Constraints
- **Trial Access:** Daily limits per app (suitable for development)
- **Standard Access:** Per minute/per user limits (suitable for production)
- **Best Practice:** Cache Pinterest data locally, don't fetch on every page load
- **Attribution:** Must link back to Pinterest, show Pinterest logo

---

## 2. M3 Implementation Phases (After API Access)

### Phase 0: Pinterest API Setup (Week 1)
**Before coding anything**
- [ ] Create Pinterest Business account
- [ ] Submit Trial access application
- [ ] Wait for approval email
- [ ] Set up OAuth credentials
- [ ] Test API connection with quickstart script

**Deliverables:**
- Working Pinterest API authentication
- Ability to fetch boards from your account
- Test script that lists pins from a board

**Timeline:** 1-3 business days (waiting for approval) + 2-3 hours setup

---

### Phase 1: Board Selection UI (3-4 hours)
**Goal:** Let you choose which Pinterest board to display

**Implementation:**
- New inspiration.html page (separate from polish gallery)
- OAuth flow for your Pinterest account (one-time setup)
- Fetch your boards via API
- UI to select which board to use (admin setting)
- Store selected board ID in localStorage or config

**UI Flow:**
```
[First-time setup screen]
→ Connect to Pinterest
→ Choose a board: [Dropdown of your boards]
→ Save selection
```

**API Endpoints Used:**
- `GET /v5/boards` - List your boards
- `GET /v5/boards/{board_id}/pins` - Get pins from selected board

**Edge Cases:**
- No boards exist
- Board is empty
- API rate limit reached
- OAuth token expired

---

### Phase 2: Pinterest Feed Display (4-5 hours)
**Goal:** Show Pinterest pins in a gallery view

**Implementation:**
- Grid layout for pins (similar to polish gallery)
- Fetch pins from selected board
- Display: pin image, title/description
- Infinite scroll or pagination
- Cache images locally (reduce API calls)
- Mobile-responsive masonry layout

**Data Flow:**
```
inspiration.html loads
→ Check localStorage for cached pins (< 1 hour old)
→ If stale, fetch from Pinterest API
→ Display pins in grid
→ User scrolls → load more pins
```

**Performance:**
- Cache pin data for 1 hour (reduce API calls)
- Lazy load images
- Compress/resize Pinterest images if too large

**Attribution:**
- Link each pin to Pinterest source
- Show "Pinned from Pinterest" with logo
- Comply with Pinterest branding guidelines

---

### Phase 3: Color Extraction (5-6 hours)
**Goal:** Extract dominant colors from Pinterest images

**Technical Approach:**
Use client-side JavaScript library (no backend needed):
- **Option A:** [Vibrant.js](https://github.com/jariz/vibrant.js/) - extracts vibrant colors
- **Option B:** [Color Thief](https://lokeshdhakar.com/projects/color-thief/) - gets dominant palette
- **Option C:** Canvas API - manual pixel sampling

**Implementation:**
- When pin is selected, run color extraction
- Get 3-5 dominant colors from image
- Convert to HSL color space (better for matching)
- Display color swatches to user
- Show "Extracting colors..." loading state

**Algorithm:**
```javascript
async function extractColors(imageUrl) {
  const img = new Image();
  img.crossOrigin = "Anonymous";
  img.src = imageUrl;
  await img.decode();
  
  const vibrant = new Vibrant(img);
  const palette = await vibrant.getPalette();
  
  return [
    palette.Vibrant,
    palette.Muted,
    palette.DarkVibrant,
    // ... etc
  ];
}
```

**Challenges:**
- CORS issues (Pinterest images on different domain)
- May need proxy or Pinterest's processed images
- Color accuracy depends on image quality

---

### Phase 4: Polish Matching Algorithm (6-8 hours)
**Goal:** Match extracted colors to your polish inventory

**Matching Logic:**
```
For each extracted color from design:
  For each polish in inventory:
    Calculate color distance (ΔE or HSL distance)
    Assign similarity score (0-100)
  Sort polishes by similarity
  Return top 3-5 matches
```

**Color Distance Formula (HSL):**
```javascript
function colorDistance(hsl1, hsl2) {
  const hDiff = Math.abs(hsl1.h - hsl2.h);
  const sDiff = Math.abs(hsl1.s - hsl2.s);
  const lDiff = Math.abs(hsl1.l - hsl2.l);
  
  // Weighted distance (hue matters most)
  return Math.sqrt(
    (hDiff * 2) ** 2 +
    (sDiff * 1) ** 2 +
    (lDiff * 1) ** 2
  );
}
```

**Enhancements:**
- Filter by finish type (if design needs shimmer, prioritize shimmer polishes)
- Consider color family tags from polishes.csv
- Let user manually override suggestions

**UI:**
```
[Pinterest Design Image]

Extracted Colors:
[🟥] [🟦] [🟨]

Suggested Polishes:
For Red: [Polish 67 - Ruby Ritz] [Polish 39 - Red Carpet]
For Blue: [Polish 530 - Ocean Blue] [Polish 3 - Blue Me A Kiss]
For Yellow: [...]

[Accept Suggestions] [Choose My Own]
```

---

### Phase 5: Polish Selection & Next Appointment (3-4 hours)
**Goal:** Let clients lock in their choices

**Integration with M2:**
- Use existing "Next Appointment" feature
- Selected design + polishes → saved to localStorage
- Show in "My Next Appt" filter

**Workflow:**
```
1. Client browses Pinterest inspiration
2. Clicks a design they like
3. System suggests polishes
4. Client reviews/adjusts suggestions
5. Clicks "Save for My Next Appointment"
6. Data saved: {designImage, designUrl, polishIds: [...]}
7. Client can view in main gallery with "My Next Appt" filter
```

**Data Structure:**
```javascript
localStorage.setItem('nailpolish_nextappt', JSON.stringify({
  designs: [
    {
      pinterestUrl: "https://...",
      imageUrl: "https://...",
      polishes: ["427-Air Of Mint", "781-Apple Cider"],
      timestamp: "2026-01-03T..."
    }
  ]
}));
```

**UI Enhancements:**
- Show design thumbnail on polish gallery when "My Next Appt" filter is active
- Link back to inspiration page to view full design

---

### Phase 6: Polish & Testing (2-3 hours)
**Goal:** Edge cases, mobile optimization, performance

**Testing Checklist:**
- [ ] Pinterest OAuth works on mobile
- [ ] Images load on slow connection
- [ ] Color extraction handles various image types
- [ ] Matching algorithm finds reasonable suggestions
- [ ] Rate limits don't break the experience
- [ ] Cached data refreshes appropriately
- [ ] Attribution to Pinterest is visible
- [ ] Touch targets are 44x44px minimum
- [ ] Works in Safari (iOS) and Chrome (Android)

**Edge Cases:**
- Pinterest API is down
- Rate limit exceeded
- No polishes match extracted colors (too niche)
- User has no Pinterest account
- Board is deleted or made private

**Performance:**
- Cache aggressively (API calls are slow)
- Compress images
- Lazy load Pinterest feed
- Debounce color extraction

---

## 3. Alternative: Search Instead of Boards

**If you'd prefer search over a specific board:**

### Search-Based Flow
Instead of selecting one of your boards, allow searching Pinterest:

**UI:**
```
[Search Pinterest for nail designs...]
[Search button]

Results:
[Grid of nail design pins from Pinterest search]
```

**API:**
- `GET /v5/search/pins?query=nail+art+designs`
- Returns pins matching search term

**Pros:**
- More variety, not limited to your board
- Clients can search for what they want
- Don't need to curate a board

**Cons:**
- Less control over content quality
- Random designs from other users
- May not represent your style
- Still subject to rate limits

**Recommendation:** Start with your curated board (Phase 1), add search later (Phase 7)

---

## 4. Data Structure: No CSV Needed!

**Good news:** Since we're pulling from Pinterest API, we don't need a static CSV.

**Pinterest API Response (simplified):**
```json
{
  "items": [
    {
      "id": "pin123",
      "title": "Gorgeous nail art",
      "description": "Sunset ombre nails",
      "image": {
        "url": "https://i.pinimg.com/..."
      },
      "link": "https://pinterest.com/pin/...",
      "dominant_color": "#ff6b6b"
    }
  ]
}
```

**What We Store Locally:**
```javascript
// Cache in localStorage (refresh every hour)
{
  boardPins: [...], // Raw Pinterest data
  lastFetched: timestamp,
  selectedDesigns: [...], // User's saved designs for next appt
  extractedColors: {
    "pin123": ["#ff6b6b", "#4ecdc4", ...]
  }
}
```

**No manual data entry needed** - Pinterest is the source of truth!

---

## 5. Timeline Estimate (After API Access Granted)

## 5. Timeline Estimate (After API Access Granted)

| Phase | Task | Estimate | Dependencies |
|-------|------|----------|--------------|
| 0 | Pinterest API setup & approval | 1-3 business days + 3 hours | Pinterest approval |
| 1 | Board selection UI | 3-4 hours | Phase 0 complete |
| 2 | Pinterest feed display | 4-5 hours | Phase 1 |
| 3 | Color extraction | 5-6 hours | Phase 2 |
| 4 | Polish matching algorithm | 6-8 hours | Phase 3 |
| 5 | Next appointment integration | 3-4 hours | Phase 4, M2 complete |
| 6 | Polish & testing | 2-3 hours | Phase 5 |
| - | **Total Development** | **~26-33 hours** | - |

**Sprint Planning:**
- **Week 1:** Pinterest API application + approval wait + setup
- **Week 2:** Phases 1-3 (Board selection, display, color extraction)
- **Week 3:** Phases 4-6 (Matching, integration, testing)

**Critical Path:** Pinterest API approval is the blocker. Can't start development until Trial access granted.

---

## 6. Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Pinterest denies API access | Cannot proceed with M3 | Medium | Strong application, clear use case, privacy policy |
| Rate limits too restrictive | Slow/broken experience | Medium | Aggressive caching, Trial → Standard upgrade |
| Color extraction inaccurate | Bad polish suggestions | Medium | Manual override option, algorithm tuning |
| CORS blocks Pinterest images | Can't analyze colors | High | Use Pinterest's CDN URLs, implement proxy if needed |
| API costs money later | Budget concern | Low | Free for Trial/Standard, only paid for ads |
| Client doesn't have Pinterest | Can't use feature | Low | Make it optional, fallback to browse polishes |

**Biggest Risk:** Pinterest API approval. Without it, we need a different approach (manual gallery).

---

## 7. Open Questions & Decisions Needed

### Before Starting Phase 0
- [ ] **Do you have a Pinterest Business account?** (Required)
- [ ] **Do you have a privacy policy URL?** (Required for API application)
- [ ] **Which board(s) do you want to use?** Or should clients search?
- [ ] **Are you okay with Pinterest attribution?** (Required by API terms)

### Technical Decisions
- [ ] **Color extraction library:** Vibrant.js vs Color Thief vs custom?
- [ ] **Caching strategy:** How long to cache Pinterest data? (1 hour? 1 day?)
- [ ] **Number of suggestions:** Show top 3 or top 5 polish matches per color?
- [ ] **Manual override:** Should clients be able to pick different polishes than suggestions?

### Business/Legal Decisions
- [ ] **Privacy policy:** Does your business have one? Pinterest requires it.
- [ ] **Terms of service:** Do you need to add Pinterest-related terms?
- [ ] **Client consent:** Do clients need to agree to Pinterest API use?

---

## 8. Alternative Approaches (If Pinterest Doesn't Work)

### Plan B: Manual Gallery (Original M3 Plan)
If Pinterest API is denied or too complex:
- Curate 10-20 of your own nail design photos
- Manual CSV with designs, colors, polishes used
- Same UI flow, but static content
- **Effort:** ~10 hours (much simpler)
- **Trade-off:** Less variety, more manual work to add designs

### Plan C: Instagram Integration
If Pinterest doesn't work but you have Instagram:
- Instagram API (also requires approval)
- Pull from your Instagram feed or saved posts
- Similar color extraction approach
- **Complexity:** Similar to Pinterest

### Plan D: Local Image Upload
Simplest approach:
- Client uploads a photo from their device
- Color extraction on uploaded image
- Match to polishes
- No API needed, fully client-side
- **Trade-off:** No browsing inspiration, one-off analysis only

**Recommendation:** Try Pinterest API first (Plan A). Fall back to Plan B if needed.

---

## 9. Success Metrics (M3)

### Quantitative
- [ ] Pinterest API integration working (Trial access)
- [ ] Board with 20+ pins displaying correctly
- [ ] Color extraction accuracy >70% (manual validation)
- [ ] Polish suggestions match extracted colors (manual validation)
- [ ] <3 second load time for inspiration page
- [ ] Mobile-responsive on iOS and Android

### Qualitative
- [ ] Clients say "this helps me pick designs"
- [ ] Color suggestions are reasonable/close
- [ ] UI feels natural (Pinterest → polishes → save)
- [ ] Attribution to Pinterest is clear but not intrusive

### Technical
- [ ] OAuth flow works on mobile
- [ ] Caching reduces API calls by 80%+
- [ ] No breaking changes to M1/M2 features
- [ ] Rate limits don't impact user experience

---

## 10. Implementation Checklist (Phase 0)

Before writing code, complete these steps:

### Pinterest API Setup
- [ ] Create Pinterest Business account (if not already)
- [ ] Verify email address
- [ ] Accept Developer Terms of Service
- [ ] Go to My Apps → Submit Trial access request
- [ ] Provide:
  - App name: "[Your Business] Nail Polish Matcher"
  - Description: "Helps nail salon clients match Pinterest inspiration to artist's polish collection"
  - Privacy policy URL: [Your website privacy policy]
  - Use case: Content management (reading boards/pins)
- [ ] Wait for approval email (1-3 business days)

### After Approval
- [ ] Get App ID and App Secret from My Apps page
- [ ] Configure redirect URI (localhost:8000 for testing)
- [ ] Test OAuth flow with quickstart script
- [ ] Verify can read your boards via API
- [ ] Verify can read pins from a board via API

### Development Environment
- [ ] Create new branch: `feature/pinterest-integration`
- [ ] Create inspiration.html (separate page)
- [ ] Set up environment variables for API credentials (don't commit!)
- [ ] Install color extraction library (Vibrant.js or Color Thief)

**Ready to begin implementation:** ____________ (date)

---

## 11. Sample Code Snippets (Planning Reference)

### Pinterest OAuth Flow (Simplified)
```javascript
// Step 1: Redirect to Pinterest for authorization
const authUrl = `https://www.pinterest.com/oauth/?
  client_id=${APP_ID}&
  redirect_uri=${encodeURIComponent('http://localhost:8000/callback')}&
  response_type=code&
  scope=boards:read,pins:read`;

window.location.href = authUrl;

// Step 2: Handle callback with authorization code
const urlParams = new URLSearchParams(window.location.search);
const authCode = urlParams.get('code');

// Step 3: Exchange code for access token (needs backend or proxy)
const tokenResponse = await fetch('https://api.pinterest.com/v5/oauth/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code',
    code: authCode,
    redirect_uri: 'http://localhost:8000/callback'
  }),
  headers: {
    'Authorization': 'Basic ' + btoa(APP_ID + ':' + APP_SECRET)
  }
});

const { access_token } = await tokenResponse.json();
localStorage.setItem('pinterest_token', access_token);
```

### Fetch Boards
```javascript
const token = localStorage.getItem('pinterest_token');
const response = await fetch('https://api.pinterest.com/v5/boards', {
  headers: { 'Authorization': `Bearer ${token}` }
});
const { items: boards } = await response.json();
// boards = [{ id, name, description, pin_count, ... }]
```

### Fetch Pins from Board
```javascript
const boardId = '123456789';
const response = await fetch(`https://api.pinterest.com/v5/boards/${boardId}/pins`, {
  headers: { 'Authorization': `Bearer ${token}` }
});
const { items: pins } = await response.json();
// pins = [{ id, title, description, media: { images: {...} }, ... }]
```

### Color Extraction (Vibrant.js)
```javascript
import Vibrant from 'node-vibrant';

async function extractColors(imageUrl) {
  const palette = await Vibrant.from(imageUrl).getPalette();
  return [
    palette.Vibrant?.hex,
    palette.Muted?.hex,
    palette.DarkVibrant?.hex,
    palette.LightVibrant?.hex,
    palette.DarkMuted?.hex
  ].filter(Boolean);
}
```

### Polish Matching (Simple)
```javascript
function findMatchingPolishes(extractedColors, polishInventory) {
  const matches = [];
  
  extractedColors.forEach(hexColor => {
    const hsl = hexToHSL(hexColor);
    const sorted = polishInventory
      .map(polish => ({
        polish,
        distance: colorDistance(hsl, hexToHSL(polish.color))
      }))
      .sort((a, b) => a.distance - b.distance);
    
    matches.push({
      designColor: hexColor,
      suggestions: sorted.slice(0, 3) // Top 3 matches
    });
  });
  
  return matches;
}
```

---

## 12. FAQs

**Q: How much does Pinterest API cost?**  
A: Free for Trial and Standard access. Only paid features are advertising APIs.

**Q: Can we start without API approval?**  
A: No. Pinterest requires approval before you can use the API. This typically takes 1-3 business days.

**Q: What if Pinterest denies our application?**  
A: We can revise and resubmit, or fall back to manual gallery approach (Plan B).

**Q: Can clients see designs from any Pinterest user?**  
A: Only public pins. Private boards require that user's OAuth permission.

**Q: Does this work offline?**  
A: No, requires internet to fetch Pinterest data. But we cache aggressively.

**Q: What about copyright/image rights?**  
A: Pinterest API terms allow us to display pins with proper attribution. Always link back to original pin.

**Q: Can we use Pinterest images in marketing?**  
A: Only with Pinterest's permission and proper attribution. Check their brand guidelines.

**Q: How accurate is color extraction?**  
A: Depends on image quality. Expect 70-80% accuracy. Manual override option is important.

**Q: What if we exceed rate limits?**  
A: Upgrade from Trial to Standard access for higher limits. Also implement caching.

**Q: Can clients save multiple designs?**  
A: Yes, we'll extend the "Next Appointment" feature to support multiple saved designs.

---

## 13. Next Steps

### Immediate (Today/This Week)
1. **Review this plan** - Any questions or concerns?
2. **Make decisions** - Answer open questions in Section 7
3. **Check prerequisites:**
   - Pinterest Business account exists?
   - Privacy policy exists?
   - Ready to commit 2-3 weeks to this?

### Short-term (Week 1)
1. **Submit Pinterest API application**
2. **While waiting for approval:**
   - Research color extraction libraries
   - Design UI mockups for inspiration page
   - Plan OAuth flow for your setup
3. **Once approved:**
   - Configure API credentials
   - Test basic connectivity
   - Begin Phase 1 development

### Long-term (Weeks 2-3)
1. **Implement phases 1-6**
2. **Test with real clients**
3. **Iterate based on feedback**
4. **Consider Standard access upgrade if needed**

---

*Document created: January 3, 2026*  
*Status: Planning - Pinterest API integration approach*  
*Next: Apply for Pinterest API access*
