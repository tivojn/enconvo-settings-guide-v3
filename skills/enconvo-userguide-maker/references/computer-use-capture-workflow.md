# Computer Use Capture Workflow

Use this reference when fresh EnConvo screenshots or live UI traversal are needed.

## Start

1. List apps and confirm EnConvo is running.
2. Get EnConvo app state before every click or scroll.
3. Keep the target page visible and centered where possible.
4. Prefer clearly labeled UI actions: tabs such as `AI Model`, buttons such as `Manage`, and named sidebar items.
5. Avoid changing settings. Do not toggle switches, submit forms, delete data, create credentials, or save changes unless the user explicitly asks.

## Concept Model

The guide must teach the difference between app-level defaults and agent-level overrides:

- `Global Providers Settings` are EnConvo-wide defaults. These pages cover AI Model, Text-to-Speech, Web Search, Image Generation, Video Generation, Web Fetch, and OCR.
- Newly created agents inherit the global providers automatically.
- Agent List pages are per-agent customization surfaces. A specific agent can override model provider, credentials, TTS, tools, context, and runtime behavior.
- `Enconvo Cloud Plan` should be documented as EnConvo's subscription-backed provider option for mainstream model access. Record only the models/providers actually visible in the live UI, but explain that this option can expose models across major LLM platforms through the user's EnConvo plan.

## Capture Pattern

For each EnConvo page or nested leaf:

1. Prove screenshot export works by saving a test image into the guide folder and verifying the file exists.
2. Open the parent page.
3. Capture the overview state.
4. Click each clearly labeled sub-tab.
5. Open safe nested drawers or managers, such as `Tools > Manage`.
6. Scroll long regions in segments: top, middle, lower, bottom.
7. Save original segment screenshots with stable names.
8. Stitch a composite when a page is scrollable and the user requested full-page coverage.
9. Log what was captured in `capture-log.md`.

If step 1 fails, pause the capture work before changing settings. Computer Use screenshots visible in the conversation are useful for navigation, but they are not enough for a screenshot-backed guide unless they are saved as original image files in `screenshots/`.

## Exhaustive Leaf Audit SOP

Use this when the user asks for a full-scale guide, a proof of concept, or says the previous pass was too shallow.

1. Assume each tab body is scrollable until you test it. Capture the top first, scroll through the full body, and capture lower segments even when the first viewport looks self-contained.
2. Open every dropdown/search menu. For each menu, log the selected value, search placeholder, visible options, and any option descriptions.
3. Click every safe pencil, gear, fullscreen, info, expand, and chevron control. Name the resulting surface: popover, modal, side sheet, fullscreen editor, nested drawer, or cross-page navigation.
4. When an icon navigates away from the current hierarchy, capture/log the destination page and then return to the original page before continuing.
5. For nested managers, scrolling is not enough. Expand every row chevron and document each revealed row-level setting.
6. For prompt/file rows, expand the chevron and keep going. `User Message`, `CHARACTER.md`, and `IDENTITY.md` are not labels; they can reveal nested editors, private markdown bodies, Insert variable buttons, Fullscreen buttons, open buttons, and remove/delete controls.
7. For credential sheets, continue inside the sheet. Expand credential-type dropdowns, document each branch, and include setup-cycle states such as masked API key entry, Validate result, OAuth browser authorize, Copy Code, EnConvo authorization-code dialog, Complete Login, Connected, and Reconnect.
8. Do not mutate the user's setup while auditing unless the user explicitly asks for a setup cycle. Switches, sliders, delete buttons, save buttons, reconnect buttons, validate buttons, refresh icons, and play buttons are normally recorded but not pressed.
9. Treat credential sheets, account panes, API key fields, OAuth codes, callback URLs, tokens, memory, mail, recordings, and local paths as `Private`. Describe their purpose without copying secrets.
10. Save a screenshot for every durable leaf whenever screenshot export is available. If screenshot export fails, log the failure, reuse existing clean screenshots as proof context, and mark missing per-leaf screenshots as follow-up work.
11. Avoid using Page Down or similar keyboard paging to prove a tab is scrollable. In EnConvo it can move focus and change tabs. Scroll the inner content deliberately and verify the selected tab before logging the result.

## Credential Setup Screenshot Manifest

For provider setup such as Anthropic, create a manifest in `capture-log.md` with one row per action:

- entry path screenshot: global `AI Model` route and/or agent-level `Agent List > Mavis > AI Model` route
- credential pencil or settings entrance opened
- credential-type dropdown opened
- `ApiKey` branch selected
- masked API key entered
- `Validate` clicked
- validation success/failure shown
- `OAuth2` branch selected
- `Connect` or `Reconnect` clicked
- browser authorization page
- browser copy-code page
- EnConvo authorization-code dialog before paste
- EnConvo authorization-code dialog after paste
- `Complete Login` clicked
- final `Connected` state

Every row must have either a saved screenshot path or `missing screenshot: <reason>`. Never store raw API keys, OAuth authorization codes, callback URLs with codes, or tokens.

## Screenshot Cleanliness

If the user warns that other windows were visible, restart the affected screenshots after they minimize noise. Do not argue with the old captures; treat clean screenshots as the new source of truth.

If the normal screenshot command fails, continue with Computer Use state and available screenshot surfaces, but tell the user if you could not create new image files. When previous clean screenshots already exist, reuse them and document new findings against those files.

## Mavis Proof Pattern

For `Agents > Agent List > Mavis`, cover at least:

- Agent Definition: instruction editor, user message, working folder, attached files, fullscreen instruction editor, variable/skill insertion helper.
- AI Model: model provider, credential provider, model name, reasoning effort, temperature.
- Tools: summary row, enabled tool count, Manage drawer, all scrollable tool groups.
- Text to Speech: auto-play, provider, credential provider, voice, language.
- More: message count, highlight edits, IM verbose mode, dynamic context, live screen, tutor mode, run mode, response language, post-action, memory.

The current known Mavis settings observed in the proof pass:

- Model provider: Anthropic.
- Model name: Claude Opus 4.7.
- Reasoning effort: High.
- Temperature: 1.
- TTS provider: xAI TTS through Enconvo Cloud Plan.
- Voice: Ara (warm, friendly).
- Language: Auto Detect.
- More tab: Dynamic Context, Live Screen, Tutor Mode, Agent run mode, Auto response language, no post-action, memory enabled.

Treat those as observations from one captured setup, not universal defaults.

## Mavis Exhaustive Leaf Findings

These findings came from the 2026-05-25 proof pass and should guide future captures:

- Agent Definition has hidden lower content. Scroll from Instruction to User Message, Working Folder, and attached context files.
- Agent Definition `Fullscreen` opens a dedicated Instruction editor with Nunjucks/Jinja2 variable guidance.
- Agent Definition `Insert variable` opens a searchable `Insert Variable or Skill` modal with Variables and Skills sections.
- Agent Definition `User Message` is expandable and reveals a second prompt editor with its own Insert variable and Fullscreen controls.
- Agent Definition attached files such as `CHARACTER.md` and `IDENTITY.md` are expandable and can reveal long private markdown editors.
- AI Model dropdowns include AI Model Provider, Credential Provider, Model Name, and Reasoning Effort. Each should be captured open.
- AI Model credential pencil opens a private Anthropic credential sheet.
- AI Model Anthropic credential sheet contains a `Credentials Type` dropdown with `ApiKey` and `OAuth2` setup branches.
- ApiKey setup includes a masked key field, base URL, Validate button, and success/failure result. Never log the key.
- OAuth2 setup includes Connect/Reconnect to Anthropic, browser authorization, Copy Code, EnConvo OAuth Authentication dialog, Complete Login, and final Connected state. Never log the code or callback URL.
- AI Model credential gear navigates to Credential Management, so it must be logged as a cross-page entrance.
- Text to Speech dropdowns include TTS Provider, Voice, and Language. The credential pencil opens a private Enconvo Cloud sheet.
- More dropdowns include Dynamic Context, Live Screen, Tutor Mode, Run Mode, Response Language, and Post Action.
- Tools `Manage` must be audited by scrolling the manager and expanding every row chevron. The full-scroll inventory is not enough for an exhaustive guide.

## Safety Notes

Dropdowns, switches, and sliders are settings controls. Inspect and document visible values; do not change them during guide capture unless the user asks.

Icon-only controls are risky in tutor mode. If they are necessary, ask the user to click them or capture only their visible purpose from context.
