---
name: enconvo-userguide-maker
description: Create or update full-scale, screenshot-backed EnConvo user guides from the live EnConvo Settings app. Use when the user asks to make an EnConvo settings guide, document EnConvo pages, deep-dive agent settings such as Agents / Agent List / Mavis, capture screenshots with Computer Use, align an HTML guide with the EnConvo docs style, or update the guide-making workflow after a new UI trick or unexpected EnConvo behavior appears.
---

# EnConvo User Guide Maker

## Output Contract

Produce a local guide folder with:

- `index.html`: a docs-style HTML guide with a top navbar, foldable left tree, article column, and optional right table of contents.
- `screenshots/`: original screenshot evidence, preserving nested folders such as `screenshots/agent-mavis/`.
- `capture-log.md`: a concise audit trail of what was opened, clicked, scrolled, captured, stitched, and documented.

Keep the guide screenshot-backed. Every page or nested leaf described in the guide should point to an original EnConvo Settings screenshot or a stitched full-scroll composite made from original segments.

Before changing settings or running a setup cycle, prove screenshot export works by saving one test screenshot into the guide folder and verifying the file exists. If screenshot export is broken, pause and fix capture first; do not rely on live Computer Use screenshots alone for a screenshot-backed guide.

The guide is a user manual, not a screenshot catalog. Use screenshots as evidence for instructions. Each screenshot-backed section should tell the user what to configure, when to use the setting, what to click or choose, what to verify before closing, and what not to change unless intentional. Avoid public copy that merely says what is visible in the screenshot, such as "showing", "visible", "observed", "captured", or "this screenshot".

## Core Workflow

Use Computer Use to drive the live EnConvo app. Read `references/computer-use-capture-workflow.md` before operating EnConvo if the task needs fresh screenshots, nested drawers, scrollable pages, or a proof-of-concept pass.

Use the existing guide as a living artifact when one exists:

1. Inspect the current `index.html`, `capture-log.md`, and `screenshots/`.
2. Preserve existing screenshots and notes unless the user asks to restart them.
3. Add new sections under the matching hierarchy. For example, Mavis belongs under `Agents > Agent List > Mavis Deep Dive`, not as a sibling of `Agent List`.
4. Keep the left sidebar tree and article content hierarchy aligned.
5. When a page uses a workflow walkthrough, pair each text step with the screenshot that proves that exact step. Do not render one long text block followed by a screenshot dump.
6. If a new workflow screenshot supersedes an older page overview screenshot, keep the old screenshot file for archive history but suppress it from user-facing rendering with a data flag such as `hidePageShot`.
7. Verify all image paths and JavaScript before finishing. When available, run `scripts/audit_guide.py <guide-dir>` from this skill folder to catch missing image refs, duplicate extensions, and screenshot-caption style copy.

When building or extending the HTML structure, read `references/html-guide-pattern.md`.

## EnConvo Navigation Baseline

Use one of these entry points when the user wants Settings:

- Menu bar: EnConvo menu -> Settings.
- Keyboard: `Cmd+,` while EnConvo is active.
- Bring EnConvo forward or open its command surface with the user's configured shortcut, commonly `Cmd+Shift+D`, when the user explicitly asks for it.

If the Settings window disappears, falls behind other windows, or is no longer reachable during automation, recover it before continuing screenshots:

1. Preferred recovery: use the macOS menu bar while EnConvo is active: EnConvo -> Settings.
2. Shortcut recovery: press `Cmd+Shift+D` to bring EnConvo to the front and make it active, then immediately press `Cmd+,`.
3. After `Cmd+,`, EnConvo's main app surface may move behind other windows while the Settings window becomes the frontmost layer. Verify the visible front window is Settings before taking screenshots.
4. If Settings does not appear, repeat from the menu bar route instead of continuing from stale Computer Use screenshots.

Respect the `ai-tutor` style when teaching live:

- Point at what is visible on screen.
- Keep explanations short while operating.
- Avoid changing settings unless the user explicitly asks.
- For risky or fiddly controls, document the visible state instead of toggling.

## Depth Rule

Do not stop at the first layer when the user asks for a full-scale guide.

Global Providers are a core concept and must be explained before agent-specific configuration:

- `Global Providers Settings` are app-level defaults for EnConvo. They define the default AI model, TTS, Web Search, Image Generation, Video Generation, Web Fetch, and OCR providers.
- New agents automatically inherit those global provider defaults unless the user customizes the agent.
- `Agents > Agent List > <Agent> > AI Model`, `Text to Speech`, `Tools`, and `More` are per-agent overrides. For example, Mavis can use Anthropic by ApiKey or OAuth2 even when the app-level provider defaults differ.
- `Enconvo Cloud Plan` means EnConvo supplies access to many mainstream model providers through the user's EnConvo monthly or yearly subscription. Document it as a convenience/default provider option that can expose models across platforms such as OpenAI/GPT, Anthropic/Claude, Gemini, DeepSeek, GLM, Kimi, and others, depending on what the live UI shows.

For each settings page:

- Open the page.
- Identify tabs, drawers, popovers, expandable rows, segmented controls, nested managers, and scrollable regions.
- Click clearly labeled tabs/buttons once when they are safe and read-only.
- Scroll through long pages and drawers; capture top, middle, lower, and bottom segments.
- Create a full-scroll composite when a page cannot fit in one screenshot.
- Treat every tab as scrollable until proven otherwise. Scroll even if the first viewport looks complete.
- Open every dropdown/search menu and document the selected value, visible choices, descriptions, and search placeholder.
- Click every safe pencil, gear, fullscreen, info, expand, and chevron control. Document whether it opens a popover, local sheet, nested drawer, fullscreen editor, or navigates to another settings page.
- For cross-page entrances, capture/log the destination and then return to the original hierarchy before continuing.
- For manager pages such as `Tools > Manage`, expand every row chevron and document each revealed sub-setting; a full-scroll inventory alone is not exhaustive.
- For prompt/file rows such as `Agent Definition > User Message`, `CHARACTER.md`, or `IDENTITY.md`, expand each chevron. These rows can reveal editors with their own Insert variable, Fullscreen, open, and delete controls.
- For credential sheets, audit the setup cycle inside the sheet. Expand credential-type dropdowns, document each branch such as `ApiKey` and `OAuth2`, validate when the user explicitly asks, and record success/failure without storing secrets.
- For OAuth flows, document the browser authorization page, copy-code handoff, EnConvo authorization-code dialog, Complete Login action, and final Connected/Reconnect state. Treat authorization codes, callback URLs, API keys, and tokens as secrets.
- For each setup/configuration cycle, maintain a per-step screenshot manifest before finishing. Every action step needs either a saved screenshot path or an explicit `missing screenshot` entry in `capture-log.md`.
- Treat switches, sliders, delete buttons, save buttons, reconnect buttons, validate buttons, and refresh/play icons as documentable controls, but do not change or trigger them unless the user explicitly asks.
- Avoid keyboard paging as a substitute for scrolling inside EnConvo tabs. It can change tabs. Use deliberate inner-panel scrolling and verify the selected tab after each movement.
- Document both the overview and each meaningful leaf.

Examples of EnConvo leaf nodes:

- `Agents > Agent List > Mavis > Agent Definition > Fullscreen instruction editor`
- `Agents > Agent List > Mavis > Agent Definition > User Message expanded`
- `Agents > Agent List > Mavis > Agent Definition > CHARACTER.md expanded`
- `Agents > Agent List > Mavis > Tools > Manage > Select Tools`
- `Agents > Agent List > Mavis > Tools > Manage > Code Runner row expanded`
- `Agents > Agent List > Mavis > AI Model > Credential Provider > pencil credential sheet`
- `Agents > Agent List > Mavis > AI Model > Credential Provider > pencil > Credentials Type > ApiKey > Validate`
- `Agents > Agent List > Mavis > AI Model > Credential Provider > pencil > Credentials Type > OAuth2 > browser authorize > paste code > Connected`
- `Global Providers Settings > AI Model > Anthropic > credential setup`
- `Agents > Agent List > Mavis > AI Model > Credential Provider > gear to Credential Management`
- `Agents > Agent List > Mavis > More > Dynamic Context dropdown`
- `Agents > Agent List > Mavis > More > lower runtime settings`

## Screenshot Rules

Before capture, ask the user to clear noisy windows if they care about clean screenshots. If noise appears, restart that capture pass when requested.

Name screenshots with stable, sortable filenames:

- first-level pages: `08-agent-list.png`
- nested pages: `agent-mavis/tools-manage-03-lower.png`
- full composites: `agent-mavis/tools-manage-full-scroll.png`

Capture credential and OAuth screenshots full-window unless the user asks for cropping. If a full-window browser OAuth page exposes a callback URL or authorization code, keep the full-window context and redact only the sensitive address/code area.

Record privacy-sensitive panes internally if useful, but do not render visible labels such as `Private` in the public guide unless the user requests badges. Do not expose secrets in prose. Personal names and email addresses should be redacted before public deployment. API keys, tokens, callback URLs, and authorization codes are secrets unless the user explicitly says otherwise.

Before redacting screenshots, create an unredacted backup outside the public repository. Never put privacy backups inside the guide repo that will be pushed to GitHub.

After manual screenshot replacement by the user, check for duplicate extensions such as `.png.png`, deleted originals, and broken HTML references before committing.

## HTML Guide Rules

Match a clean EnConvo docs/manual feel:

- left docs sidebar with foldable tree branches
- article content aligned to the same hierarchy as the sidebar
- right `On this page` outline when useful
- restrained typography and short explanatory paragraphs
- body starts with real guide content by default, not a large marketing-style introduction
- screenshots render full text-column width and are clickable to enlarge
- screenshot captions, filenames, and "Click to enlarge" text should be hidden by default unless the user asks for them
- avoid card-in-card or box-in-box visual structure; use plain sections and frameless screenshots unless the existing guide design requires cards
- do not render internal tags such as `Private`, `Provider`, `Voice`, or `Runtime` as visible badges by default
- when users open a deep hash link such as `#dictation-transcription-dictation`, the left navigation should open the matching branch, highlight the active link, and scroll the sidebar to keep the navigation and content body in sync

Prefer a data-driven `sections` array over hand-writing many repeated HTML blocks. Nested content should be represented with parent metadata such as:

- `parent: "agents"`
- `parentPage: "Agent List"`
- optional `deepDive` entries for tab-by-tab proof maps

## Validation

Before final response:

1. Parse the HTML.
2. Compile or syntax-check any inline JavaScript.
3. Verify every referenced screenshot file exists.
4. Inspect changed anchors for the requested hierarchy.
5. Update `capture-log.md` with the new capture pass and any oddities.

Do not push or deploy unless the user explicitly asks. When asked to push/deploy, run validation first, commit the exact intended changes, push, deploy, and report the commit hash plus the production URL.

After publishing guide changes that affect anchors, source URLs, or practical answer content, update the bundled and installed `enconvo-how-to` skill as part of the same pass. Confirm the installed skill copy and repo-bundled skill copy match, and validate that every referenced anchor exists in the generated guide.

Useful checks:

```bash
python3 - <<'PY'
from html.parser import HTMLParser
from pathlib import Path
HTMLParser().feed(Path('enconvo-settings-guide/index.html').read_text())
print('html-ok')
PY
```

```bash
node - <<'NODE'
const fs = require('fs');
const html = fs.readFileSync('enconvo-settings-guide/index.html', 'utf8');
for (const script of [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1])) new Function(script);
console.log('js-syntax-ok');
NODE
```

```bash
python3 - <<'PY'
from pathlib import Path
import re
html = Path('enconvo-settings-guide/index.html').read_text()
refs = re.findall(r'"((?:[a-z0-9-]+/)?[0-9a-zA-Z][^"]+\.png)"', html)
missing = [r for r in refs if not (Path('enconvo-settings-guide/screenshots') / r).exists()]
print(f'images={len(refs)} unique={len(set(refs))} missing={len(missing)}')
if missing:
    print('\n'.join(missing))
PY
```

If this skill's helper script is available, prefer:

```bash
python3 /Users/zanearcher/.agents/skills/enconvo-userguide-maker/scripts/audit_guide.py enconvo-settings-guide
```

## Updating This Skill

When a future EnConvo guide task reveals a new trick, failure mode, naming convention, or nested UI pattern, update this skill immediately:

- Put essential rules in `SKILL.md`.
- Put detailed procedural notes in `references/`.
- Keep additions short and practical.
- Re-run skill validation after edits.
