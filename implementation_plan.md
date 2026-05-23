# Portfolio Redesign — Editorial, Card-Free Design System

## Core Philosophy

> The site should never feel like a portfolio template. Every section should feel like intentional, authored content — the way a research paper, a design agency's website, or an Apple product page feels. **No cards. No tiles. No dashboard grids. No boxed components.**

The design language has two pillars:
1. **Glass identity** — preserved. Soft translucency, smooth edges, and blur remain the material feel. But used as texture and surface — not as UI containers.
2. **Editorial rhythm** — spacing, typography scale, ruled lines, and visual weight replace the role that cards and boxes used to play.

---

## Files Changed

Only two files:
- **`index.html`** — Full structural rewrite of every section
- **`static/css/main.css`** — Full CSS rewrite applying the new design system

No new vendor dependencies. No build step. Remains statically deployable.

---

## Design Tokens

### Color Palette (refined, not replaced)
| Token | Old | New | Rationale |
|---|---|---|---|
| `--background-color` | `#ffffff` | `#f2f4f8` | Soft blue-grey — cohesive with glass |
| `--accent-color` | `#0563bb` | `#2563eb` | Slightly more vibrant, still professional |
| `--heading-color` | `#45505b` | `#1e293b` | Darker, sharper contrast |
| `--default-color` | `#272829` | `#374151` | Slightly softer body text |
| `--muted-color` | _(new)_ | `#94a3b8` | For labels, metadata, dividers |
| `--glass-surface` | _(new)_ | `rgba(255,255,255,0.55)` | Lighter than before — less card-like |
| `--glass-border` | _(new)_ | `rgba(255,255,255,0.5)` | Soft glass edge |

### Glass System (texture, not container)
The glass effect is applied as a **surface texture** on full-width or large elements, not as a card wrapper. When glass appears on a panel or content area, it should feel like frosted paper — integrated into the page, not floating above it.
```css
/* Lightweight glass surface — not a card */
backdrop-filter: blur(12px) saturate(140%);
background: rgba(255, 255, 255, 0.52);
border-bottom: 1px solid rgba(255, 255, 255, 0.5); /* edge only, not full border */
/* No box-shadow on editorial content areas */
```

### Typography Scale
- **Display (Hero name)**: Inter 700, `clamp(52px, 7vw, 80px)`
- **Section label**: Raleway 500, `11px`, `letter-spacing: 3px`, muted, uppercase
- **Section title**: Raleway 700, `clamp(28px, 3.5vw, 42px)`
- **Content title**: Raleway 700, `22–26px`
- **Body**: Roboto 400, `15–16px`, `line-height: 1.75`
- **Meta / date / label**: Roboto 400, `13px`, muted color

---

## Section-by-Section Design

---

### 1. Navigation (sidebar — minimal glass surface)
- Preserved vertical sidebar structure
- Glass surface: `backdrop-filter: blur(16px)`, `background: rgba(242,244,248,0.85)` — blends with page background
- Nav items: icon-only circles, expands on hover — same behavior as current
- Active state: accent fill — same as current
- No heavy borders or shadows on the sidebar itself

---

### 2. Hero Section

#### Layout
- Full viewport height
- Hero background image (preserved) with a soft overlay: `background: linear-gradient(135deg, rgba(242,244,248,0.82), rgba(215,225,255,0.65))`
- Centered content column, no bounding box around name/text
- Name, typed subtitle, social links remain focal point

#### Orbital Tech Ring
- Single CSS ring: `border-radius: 50%`, `border: 1px dashed rgba(37,99,235,0.18)` — the orbit track
- Dimensions: `clamp(360px, 44vw, 520px)` diameter, centered behind the text
- 15 tech logos (SVG from devicons CDN) at evenly-spaced degree positions on the ring
- Ring rotates: `animation: orbit 70s linear infinite` — slow, elegant
- Each logo counter-rotates to stay upright: `transform: rotate(Ndeg) translateX(R) rotate(-Ndeg)`
- Logo size: `32px`, subtle drop-shadow
- **Hidden below 992px** — clean mobile
- Logos: Python · Django · FastAPI · LangGraph · Git · SQL/PostgreSQL · Apache Spark · Azure · Heroku · Pandas · NumPy · TensorFlow · Neo4j · Raspberry Pi · Docker

---

### 3. About Section

#### Layout (no card wrapping the content)
- Two-column: profile image left, content right — same as current
- Profile image: `border-radius: 50%` with a soft glowing ring (`box-shadow: 0 0 0 4px rgba(37,99,235,0.12), 0 20px 60px rgba(37,99,235,0.15)`) — image as editorial anchor, not inside a card frame
- Content column: plain typographic layout — role title in large Raleway, italic intro, then personal details as a clean definition list
- No enclosing box, no background surface behind the content column
- Personal detail list: `display: grid; grid-template-columns: 1fr 1fr; gap: 12px 32px` with thin top rule per item (`border-top: 1px solid rgba(37,99,235,0.08)`) — structured but not card-like
- Resume download: styled as an inline text CTA with an arrow, not a button-in-a-card

---

### 4. Skills Section

#### Layout (no progress bar dashboard)
Two approaches considered. **Chosen approach: two-column typographic skill list with accent-line proficiency indicator.**

Each skill:
```
Python ············································ Expert
Django ··········································· Advanced
LangGraph ········································ Advanced
```
- Skill name: `font-weight: 600`, `font-size: 15px`
- Dotted connector: `border-bottom: 1px dotted rgba(37,99,235,0.25)`, flex grow
- Proficiency label: `font-size: 13px`, muted accent, `font-style: italic`
- No bar chart. No percentage numbers. No progress-bar tracks.
- Two columns on desktop, single column on mobile
- Section has a soft top rule and plenty of vertical breathing room between items

---

### 5. Resume Section

#### Layout (pure typographic timeline — no boxed items)
- Two-column: Education left, Experience right — same column structure as current
- **Section label**: small uppercase Raleway in muted accent, e.g. `EDUCATION`
- No `resume-item` glass boxes. Items are pure typographic blocks separated by whitespace.

Each experience item:
```
AI Engineer Intern · Auxo AI
Jan 2026 – Present  ·  Bangalore, India

Developing Generative AI solutions using LLMs…
Building and deploying autonomous AI agents…
Implementing RAG pipelines and FastAPI backends…
```
- Company + Role: `font-size: 18px`, `font-weight: 700`, heading color
- Date + Location: `font-size: 13px`, muted, `margin-bottom: 12px`
- Bullet points replaced with `·` prefixed lines or simple `<p>` blocks — no `<ul>` bullets
- Items separated by a thin ruled line: `border-top: 1px solid rgba(37,99,235,0.10)`, with `padding-top: 32px; margin-top: 32px`
- Timeline dot on left border: **kept** — a single 8px accent dot on a `border-left: 2px solid rgba(37,99,235,0.25)` vertical rule gives the timeline feel without the boxed item

---

### 6. Portfolio Section — Editorial Alternating Showcase

This is the most visually significant section. The full section feels like a magazine spread.

#### Project rows (filter-projects)
Each project is a **full-width editorial row**. No enclosing card or box.

**Row structure:**
```html
<article class="project-row portfolio-item isotope-item filter-projects" data-aos="fade-right">
  <div class="project-visual">
    <div class="project-circle">
      <img src="..." alt="..." loading="lazy">
    </div>
  </div>
  <div class="project-content">
    <span class="project-label">AI · Backend · Finance</span>
    <h3 class="project-title">QuantLab — Algorithmic Trading Engine</h3>
    <p class="project-desc">Django-based engine integrating ML models for accurate stock price prediction and portfolio management. Deployed live on Heroku.</p>
    <div class="project-tags">
      <span>Django</span><span>Python</span><span>ML</span><span>Heroku</span>
    </div>
    <p class="project-highlight">97% model accuracy · Live deployment</p>
    <a href="..." class="project-link" target="_blank" rel="noopener">View Project →</a>
  </div>
</article>
```

**Row layout:**
- `display: flex; align-items: center; gap: clamp(48px, 6vw, 96px); padding: 96px 0`
- `project-row--flip` (every other): `flex-direction: row-reverse`
- Separated by: `border-top: 1px solid rgba(37,99,235,0.08)` — hairline, not a card border
- No background surface on the row itself — it floats on the page background

**Circular visual:**
- `width: clamp(280px, 28vw, 380px); height: clamp(280px, 28vw, 380px)`
- `border-radius: 50%; overflow: hidden`
- `box-shadow: 0 24px 72px rgba(37,99,235,0.16)` — glowing shadow, not a border
- `border: 2px solid rgba(255,255,255,0.7)` — subtle glass rim
- Hover: `transform: scale(1.035)` over `0.6s ease` — barely perceptible, premium

**Content area (project-content):**
- `flex: 1`
- **No background. No blur. No border.** — pure typographic content block
- The glass identity comes from the page surface and the circular image shadow, not from wrapping the text in a glass box
- `project-label`: `font-size: 11px; letter-spacing: 3px; text-transform: uppercase; color: var(--accent-color); opacity: 0.7; margin-bottom: 12px`
- `project-title`: Raleway 700, `clamp(22px, 2.5vw, 30px)`, heading color
- `project-desc`: Roboto 400, `15px`, `line-height: 1.8`, body color, `max-width: 480px`
- `project-tags`: pill spans — `background: rgba(37,99,235,0.07); border: 1px solid rgba(37,99,235,0.18); border-radius: 50px; padding: 4px 14px; font-size: 12px; color: var(--accent-color)`
- `project-highlight`: `font-size: 13px; font-style: italic; color: var(--muted-color); margin-top: 8px`
- `project-link`: accent color, `font-size: 14px; font-weight: 600; letter-spacing: 0.5px`, underline grows on hover

#### Achievements (filter-achievements)
Large typographic layout. No card enclosure.

Each achievement:
```html
<article class="achievement-row portfolio-item isotope-item filter-achievements" data-aos="fade-up">
  <div class="achievement-year">2022</div>
  <div class="achievement-content">
    <h3 class="achievement-title">Panasonic Asia Scholarship Winner</h3>
    <p class="achievement-desc">One of 30 scholars selected across Asia Pacific for academic excellence and leadership potential.</p>
    <a href="..." class="achievement-link" target="_blank">View Certificate →</a>
  </div>
</article>
```
- `display: flex; gap: 48px; align-items: flex-start; padding: 40px 0`
- `border-top: 1px solid rgba(37,99,235,0.08)` — ruled separator only
- `achievement-year`: `font-size: clamp(36px, 4vw, 52px); font-weight: 700; color: rgba(37,99,235,0.15); font-family: Raleway; line-height: 1; flex-shrink: 0; width: 100px`
- `achievement-title`: Raleway 700, `22px`, heading color
- `achievement-desc`: Roboto, `14px`, muted, `line-height: 1.7`

#### Certifications (filter-certifications)
Minimal list. No tiles.

```html
<article class="cert-item portfolio-item isotope-item filter-certifications" data-aos="fade-up">
  <span class="cert-issuer">Google</span>
  <h3 class="cert-title">Advanced Data Analytics</h3>
  <a href="..." class="cert-link">Verify →</a>
</article>
```
- Each cert: `display: flex; align-items: baseline; gap: 24px; padding: 24px 0; border-bottom: 1px solid rgba(37,99,235,0.08)`
- `cert-issuer`: small muted label left-aligned, `width: 100px; flex-shrink: 0`
- `cert-title`: `font-size: 18px; font-weight: 600; flex: 1`
- `cert-link`: right-aligned, small accent text

#### Responsibilities (filter-responsibility)
Editorial timeline. No cards.

```html
<article class="resp-item portfolio-item isotope-item filter-responsibility" data-aos="fade-up">
  <div class="resp-timeline-dot"></div>
  <div class="resp-content">
    <span class="resp-period">2024 – Present</span>
    <h3 class="resp-title">Placement Coordinator, IIT Jammu</h3>
  </div>
</article>
```
- Items sit on a continuous vertical line (left `border-left: 2px solid rgba(37,99,235,0.18)`)
- Each item has a dot marker: `8px` circle, filled accent
- `resp-period`: small muted date above the title
- `resp-title`: Raleway 600, `18px`
- Generous `padding-left: 32px; margin-bottom: 40px` — breathable

#### Filter tabs (redesigned)
- Horizontal pill row, clean
- Active: `background: var(--accent-color); color: #fff; border-radius: 50px; padding: 8px 22px`
- Inactive: `color: var(--muted-color); padding: 8px 22px; border-radius: 50px` — no background, no border
- Hover: accent color text
- Spacing: `gap: 4px`

---

### 7. Contact Section

#### Layout (no info-item cards)
- Two-column: contact info left, form right — same as current
- Contact info items: `display: flex; align-items: flex-start; gap: 16px; padding: 20px 0; border-bottom: 1px solid rgba(37,99,235,0.08)` — ruled list, no card wrapping
- Icon: small accent-colored icon, no background circle/tile behind it
- Form: full-width glass surface — here the glass is intentional as a writing surface
  ```css
  .contact-form-wrap {
    background: rgba(255,255,255,0.58);
    backdrop-filter: blur(14px);
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.55);
    padding: 40px 48px;
  }
  ```
- Input fields: `border: none; border-bottom: 1px solid rgba(37,99,235,0.2); border-radius: 0; background: transparent; padding: 12px 4px` — underline-only style
- Submit: `background: var(--accent-color); color: #fff; border-radius: 50px; padding: 12px 40px; font-weight: 600; letter-spacing: 0.5px`

---

### 8. Footer

- Clean, centered typographic footer
- No heavy border or background box
- Soft top gradient fade: `background: linear-gradient(to bottom, transparent, rgba(37,99,235,0.04))`
- Name in large Raleway heading
- Social icons: circular, 36px, accent fill

---

## Motion System

- AOS `fade-up` default for most elements (staggered delay)
- `fade-right` / `fade-left` for project row alternation
- Scroll: smooth (preserved)
- Typed.js: preserved in hero
- Circle hover: `scale(1.035)` over `0.6s ease` — one place only
- No parallax, no flip, no bounce, no scale-in on sections
- Preloader: preserved

---

## Open Questions

> [!IMPORTANT]
> **Q1: FeedbackFlow project** — `feedbackflow.webp` exists in assets but has no HTML entry. Should I add it as a 5th editorial project row? If yes: short description + link.

> [!NOTE]
> **Q2: Contact form backend** — The form currently submits to `/send-email` (FastAPI route) and falls back to a `mailto:` handler. I'll preserve this behavior exactly. Is there anything to change here?

> [!NOTE]
> **Q3: Typed.js subtitle** — Currently cycles: `"Software Engineer, AI/ML Developer, Data Scientist"`. Keep as-is, or update the copy?

> [!NOTE]
> **Q4: Skills content** — I'll rewrite the skills section as a typographic two-column list (skill name + proficiency label) instead of progress bars. Confirm this direction or let me know if you want to keep bars.

---

## Verification Plan

### Browser test (automated subagent)
- Confirm orbital ring renders and rotates
- Confirm all filter tabs work (isotope shows correct items per filter)
- Confirm project rows alternate correctly
- Confirm mobile layout stacks correctly
- Confirm glass form, underline inputs, and submit button

### No build step
- Static HTML → Vercel serves `index.html` directly
- No `vercel.json` changes needed
