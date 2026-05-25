# EnConvo Settings User Guide v3 Capture Log

Date: 2026-05-25  
Workspace: `/Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3`

## Version 3 Scope

Version 3 is a clean guide folder and a new HTML guide. It does not modify the v1 or v2 folders.

The v3 guide uses:

- `screenshots/00-capture-proof.png` - fresh screenshot export proof saved directly into v3.
- Imported original evidence from v1 `screenshots/` - 78 existing EnConvo Settings screenshots and nested Mavis screenshots copied into v3 so the new HTML is self-contained.

## Screenshot Export Proof

Screenshot export was tested before guide assembly.

- Initial sandboxed `screencapture` failed with `could not create image from display`.
- Escalated `screencapture` succeeded and saved `screenshots/00-capture-proof.png`.
- The file was verified as non-empty.

## Privacy Note

This guide is local/private. Screenshots may contain account details, memory entries, message channels, local paths, masked credentials, recordings, logs, or usage data. The guide labels sensitive surfaces as `Private` and does not write raw secrets, API keys, OAuth codes, callback URLs, or tokens into prose.

## Imported Full Settings Evidence

The v3 screenshot set includes the full first-level Settings inventory:

1. `01-ai-model.png` - AI Model
2. `02-text-to-speech.png` - Text-to-Speech
3. `03-web-search.png` - Web Search
4. `04-image-generation.png` - Image Generation
5. `05-video-generation.png` - Video Generation
6. `06-web-fetch.png` - Web Fetch
7. `07-ocr.png` - OCR
8. `08-agent-list.png` - Agent List
9. `09-voice-trigger.png` - Voice Trigger
10. `10-memory-management.png` - Memory Management
11. `11-im-channels.png` - IM Channels
12. `12-browser-companion.png` - Browser Companion
13. `13-computer-use.png` - Computer-Use
14. `14-scheduled-jobs.png` - Scheduled Jobs
15. `15-skills.png` - Skills
16. `16-variables.png` - Variables
17. `17-context-awareness.png` - Context Awareness
18. `18-appshots.png` - Appshots
19. `19-extension-store.png` - Extension Store
20. `20-installed-extensions.png` - Installed Extensions
21. `21-companion-orb.png` - Companion Orb
22. `22-popbar.png` - PopBar
23. `23-smartbar.png` - SmartBar
24. `24-dynamic-island.png` - Dynamic Island
25. `25-ai-cursor.png` - AI Cursor
26. `26-screen-doodle.png` - Screen Doodle
27. `27-sidebar.png` - Sidebar
28. `28-app-sidebar.png` - App Sidebar
29. `29-chat-window.png` - Chat Window
30. `30-credential-management.png` - Credential Management
31. `31-dictation-models.png` - Dictation Models
32. `32-dictation.png` - Dictation
33. `33-dictation-history.png` - Dictation History
34. `34-dictionary.png` - Dictionary
35. `35-transcription-models.png` - Transcription Models
36. `36-recordings.png` - Recordings
37. `37-ai-command-store.png` - AI Command Store
38. `38-ai-command-list.png` - AI Command List
39. `39-knowledgebase.png` - KnowledgeBase
40. `40-my-profile.png` - My Profile
41. `41-account.png` - Account
42. `42-points-usage.png` - Points Usage
43. `43-general-settings.png` - General Settings
44. `44-shortcut-settings.png` - Shortcut Settings
45. `45-about.png` - About
46. `46-developer-tools.png` - Developer Tools
47. `47-logging.png` - Logging
48. `48-apis.png` - APIs
49. `49-cli-guide.png` - CLI Guide

## Imported Agent Configuration Evidence (Mavis)

Nested screenshots copied into `screenshots/agent-mavis/` cover:

- Agent Definition top, lower, full-scroll, expanded `User Message`, expanded `CHARACTER.md`, and fullscreen/editor-related proof.
- AI Model full tab, Anthropic credential sheet, credential type dropdown, ApiKey setup, ApiKey validation, OAuth2 setup, browser authorization, code-copy handoff, and final connected state.
- Tools summary plus four `Select Tools` manager scroll segments and a stitched full-scroll composite.
- Text to Speech full tab.
- More tab top/lower/bottom segments and stitched full-scroll composite.

## Version 3 HTML Work

Created `index.html` from scratch with:

- fixed top navbar
- foldable left tree
- central article column
- right table of contents
- data-driven `sections` array
- screenshot cards linked to local evidence
- full hierarchy from Global Providers through Developer
- a dedicated `Agents > Agent List > Agent Configuration (Mavis)` section
- explicit distinction between global provider defaults and per-agent overrides
- privacy labels and setup-cycle cautions

Correction:

- Mavis was initially rendered as a top-level article section even though its metadata said `parent: "agents"`.
- The HTML renderer now nests `Agent Configuration (Mavis)` under `Agents > Agent List` in both the left sidebar and article content.

## Known Follow-Up

The guide is full-scale and screenshot-backed, but some dropdowns, row chevrons, and modals reuse broader tab screenshots instead of a separate v3-only fresh screenshot for every individual leaf. A future v3.1 pass can recapture every dropdown and manager-row expansion as separate files if a fully exhaustive per-leaf image manifest is required.

## Fresh Recapture Pass

Added on 2026-05-25 after the user clarified that v3 must not rely on imported v1 screenshots for the main Settings manual.

Fresh screenshots saved directly into v3:

- `01-ai-model.png` through `49-cli-guide.png` were recaptured from the live EnConvo Settings UI.
- The 49 first-level screenshots were verified present and non-empty.
- `agent-mavis/agent-definition-01-top.png`, `agent-mavis/ai-model-01-full.png`, `agent-mavis/tools-01-summary.png`, `agent-mavis/tools-manage-01-top.png`, `agent-mavis/tools-manage-full-scroll.png`, `agent-mavis/text-to-speech-01-full.png`, `agent-mavis/more-01-top.png`, and `agent-mavis/more-full-scroll.png` were refreshed from the live Mavis agent settings.

Safety notes:

- No switches, sliders, reset buttons, validate buttons, delete buttons, refresh/play buttons, or save actions were triggered during the recapture.
- Credential and account panes were captured only in their visible masked states.
- Anthropic setup-cycle screenshots from the earlier proof pass remain in the folder for the setup-cycle section, because re-running ApiKey validation or OAuth login would mutate credentials and browser authorization state.

## Mavis AI Model Detail Merge

Added after the user noted that the v3 Mavis AI Model area was missing the deeper v1 credential setup sectors.

- `Agents > Agent List > Agent Configuration (Mavis) > AI Model` now includes the Credential Provider pencil and gear behavior directly in the AI Model card.
- Added AI Model screenshot cards for the Anthropic credential-type dropdown, ApiKey setup branch, four ApiKey validation screenshots, and six OAuth2 browser handoff screenshots.
- Added deep-dive walkthroughs for AI Model pencil/gear entrances, Anthropic evidence checklist, Anthropic API key setup, and Anthropic OAuth2 setup.
- Reused existing private proof screenshots already present in `screenshots/agent-mavis/`; credential validation and OAuth login were not rerun because that would change sensitive account/session state.

## Left Tree And Agent Definition Recapture

Added after the user requested a more thorough left-panel tree and cleaner Agent Definition screenshots.

- Optimized the HTML sidebar into nested collapsible branches.
- `Agents > Agent List > Agent Configuration (Mavis)` now groups child links under `Agent Definition`, `AI Model`, `Tools`, `Text to Speech`, and `More`.
- `Agent Definition` now exposes its four screenshot leaves together: Top, Lower, Full Scroll, and Expanded Leaves.
- Replaced noisy `agent-mavis/agent-definition-02-lower.png` with a fresh live EnConvo capture.
- Rebuilt `agent-mavis/agent-definition-full-scroll.png` from clean fresh top/lower evidence.
- No Agent Definition text, files, switches, or settings were edited during this pass.

## Agent List Column And Agent Portrait Controls

Added after the user pointed out two missing Agent List interfaces.

- Captured `agent-mavis/agent-list-create-new-agent-menu.png` from the `Create New Agent` button at the bottom of the middle Agent List column.
- The menu exposes `New Agent`, `New OpenClaw Agent`, and `New Hermes Agent`; no option was selected and no agent was created.
- Captured `agent-mavis/agent-list-change-icon-dialog.png` from the Mavis portrait/icon in the selected agent header.
- The Change Icon dialog documents where to choose a local portrait file and shows the current file path; no file was chosen and the portrait was not changed.
- Moved the create-agent menu to its own child section at `Agents > Agent List > Create New Agent`, parallel to `Agent Configuration (Mavis)`.
- Moved the portrait-change screenshot into `Agents > Agent List > Agent Configuration (Mavis)`, before `Agent Definition`, because it changes the selected agent's portrait and belongs to the agent configuration structure.

## Global AI Model Configuration

Added after the user requested an expanded configuration section for `Global Providers Settings > AI Model`.

- Captured `global-ai-model/enconvo-cloud-plan-01-overview.png`, `global-ai-model/enconvo-cloud-plan-02-model-menu.png`, and `global-ai-model/enconvo-cloud-plan-03-reasoning-menu.png` for the EnConvo Cloud Plan path.
- Captured `global-ai-model/openai-01-overview.png`, `global-ai-model/openai-02-credential-menu.png`, `global-ai-model/openai-03-oauth-sheet.png`, `global-ai-model/openai-04-credential-type-menu.png`, `global-ai-model/openai-05-apikey-setup.png`, and `global-ai-model/openai-06-apikey-api-type-menu.png` for the OpenAI path.
- Documented the EnConvo Cloud Plan model menu and reasoning menu as the subscription-managed global provider route.
- Documented the OpenAI provider overview, credential menu, OAuth2 sheet, credential-type dropdown, ApiKey branch, and API Type menu.
- No API key was entered, no credential was validated, no OAuth login was started, no Reconnect action was triggered, and no Set as Default Provider action was clicked.
- OpenAI account details visible in credential sheets were redacted before the public screenshots were saved.

## Global AI Model Inventory Pass

Added after the user requested full visible lists for EnConvo Cloud Plan models and AI Model providers.

- Captured Cloud Plan model menu screenshots:
  - `global-ai-model/cloud-plan-model-list-01-top.png`
  - `global-ai-model/cloud-plan-model-list-02-gemini.png`
  - `global-ai-model/cloud-plan-model-list-03-gemini-details.png`
  - `global-ai-model/cloud-plan-model-list-04-deepseek-grok.png`
  - `global-ai-model/cloud-plan-model-list-05-mistral-glm-mimo.png`
- Captured AI Model provider column screenshots:
  - `global-ai-model/provider-list-01-top.png`
  - `global-ai-model/provider-list-02-lower.png`
  - `global-ai-model/provider-list-03-bottom.png`
- Added an observed Cloud Plan model inventory to the EnConvo Cloud Plan configuration section.
- Added an observed AI Model provider inventory to the global AI Model configuration section, including the lower providers down to Vercel AI Gateway.
- No model was selected, no provider was set as default, no credentials were opened, and no provider settings were changed.

## Global Text-to-Speech Configuration

Added after the user requested the next expanded section for `Global Providers Settings > Text-to-Speech`.

- Captured `global-text-to-speech/tts-01-overview-edge.png` for the default Edge TTS provider overview.
- Captured `global-text-to-speech/tts-02-edge-voice-menu.png` for the Edge TTS voice menu.
- Captured `global-text-to-speech/tts-03-edge-output-format-menu.png` for the Edge TTS output-format menu.
- Captured `global-text-to-speech/tts-04-xai-cloud-overview.png` for xAI TTS through EnConvo Cloud Plan.
- Captured `global-text-to-speech/tts-05-xai-cloud-voice-menu.png` for xAI Cloud Plan voice choices.
- Captured `global-text-to-speech/tts-06-xai-cloud-language-menu.png` for xAI Cloud Plan language choices.
- Captured `global-text-to-speech/tts-07-openai-overview.png` for OpenAI TTS direct-provider configuration.
- Captured `global-text-to-speech/tts-08-openai-credential-menu.png` for the OpenAI TTS credential menu.
- No preview/play button was triggered, no voice was selected, no output format was selected, no credential was opened, and no default provider was changed.

## Global Text-to-Speech Provider Structure And xAI Credentials

Added after the user requested the TTS section to follow the same global-provider structure as AI Model.

- Reorganized the guide into `EnConvo Cloud Plan TTS` and `Provider Inventory`.
- Removed the extra `Text-to-Speech Configuration` level from the left navigation so `EnConvo Cloud Plan TTS` and `Provider Inventory` sit directly under `Text-to-Speech`.
- Nested Edge TTS, OpenAI TTS, Gemini TTS, and xAI TTS under `Provider Inventory`.
- Reordered `EnConvo Cloud Plan TTS` so the main Cloud Plan guidance appears before the xAI Cloud Plan screenshots.
- Documented the observed Cloud Plan TTS providers: xAI TTS, Gemini TTS, Microsoft TTS, MiniMax TTS, and Xiaomi MiMo TTS.
- Captured `global-text-to-speech/tts-09-gemini-overview.png` for Gemini TTS direct-provider setup.
- Captured `global-text-to-speech/tts-10-gemini-model-menu.png` for the Gemini TTS model menu.
- Captured `global-text-to-speech/tts-11-gemini-voice-menu.png` for the Gemini TTS voice menu.
- Captured `global-text-to-speech/tts-12-xai-direct-overview.png` for xAI TTS direct-provider setup.
- Captured `global-text-to-speech/tts-13-xai-credential-oauth-sheet.png` for the xAI TTS OAuth2 credential sheet.
- Captured `global-text-to-speech/tts-14-xai-credential-type-menu.png` for the xAI TTS credential type menu showing ApiKey and OAuth2.
- Captured `global-text-to-speech/tts-15-xai-credential-apikey-setup.png` for the xAI TTS ApiKey setup branch.
- Account identifiers in the xAI OAuth2 credential sheet were redacted before saving public screenshots.
- No preview/play button was triggered, no voice was selected, no credential was validated, no reconnect action was triggered, and no default provider was changed.
