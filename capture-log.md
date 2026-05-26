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
- Reorganized the AI Model navigation to remove the extra `AI Model Configuration` layer. The direct AI Model children now follow the same structure style as Text-to-Speech: `Provider Inventory`, `EnConvo Cloud Plan`, then `OpenAI`.
- Removed redundant standalone `OpenAI Overview` and `OpenAI Credential Menu` leaves from the AI Model OpenAI subsection. The OpenAI subsection now moves from setup into `OpenAI Credential Type Menu`, `OpenAI ApiKey Setup`, `OpenAI API Type Menu`, and `OpenAI OAuth2 Credential Sheet`.

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

## Global AI Model Selected Provider Expansion

Added after the user selected a focused set of additional AI Model providers instead of documenting every provider in the full inventory.

- Captured `global-ai-model/anthropic-01-overview.png` and `global-ai-model/anthropic-02-model-menu.png` for Anthropic / Claude.
- Captured `global-ai-model/gemini-01-overview.png` and `global-ai-model/gemini-02-model-menu.png` for Google Gemini AI.
- Captured `global-ai-model/ollama-01-overview.png` and `global-ai-model/ollama-02-model-menu.png` for Ollama.
- Captured `global-ai-model/groq-01-overview.png` and `global-ai-model/groq-02-model-menu.png` for Groq AI.
- Captured `global-ai-model/zai-01-overview.png` and `global-ai-model/zai-02-model-menu.png` for Z.AI / GLM.
- Added these as direct AI Model sibling sections after OpenAI: Anthropic, Google Gemini AI, Ollama, Groq AI, and Z.AI / GLM.
- Added an `etc.` note to the provider inventory to clarify that the guide expands selected examples rather than documenting every provider in the full inventory.
- No credential was edited or validated, no OAuth flow was started, no model was selected, no local model service was started, and no default provider was changed.

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
- Reordered `EnConvo Cloud Plan TTS` so the main Cloud Plan guidance appears before the xAI Cloud Plan screenshots.
- Flattened the `Text-to-Speech` navigation so its six first-level items are `Provider Inventory`, `EnConvo Cloud Plan TTS`, `Edge TTS`, `OpenAI TTS`, `Gemini TTS`, and `xAI TTS`.
- Reordered the `Text-to-Speech` body content to match the left navigation sequence.
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

## Global Text-to-Speech Provider Cleanup

Added after the user requested provider subsection deduplication and missing credential-pencil coverage.

- Removed redundant provider overview leaves for Edge TTS, OpenAI TTS, Gemini TTS, and xAI TTS from the sidebar/body flow.
- Renamed each provider guide entry to a single configuration section: Edge TTS Configuration, OpenAI TTS Configuration, Gemini TTS Configuration, and xAI TTS Configuration.
- Kept Edge TTS focused on preview text, voice, and output format because it has no credential provider or pencil editor.
- Captured `global-text-to-speech/tts-16-openai-credential-oauth-sheet.png` for the OpenAI TTS OAuth2 credential editor opened from the pencil icon.
- Captured `global-text-to-speech/tts-17-openai-credential-type-menu.png` for the OpenAI TTS credential type menu.
- Captured `global-text-to-speech/tts-18-openai-credential-apikey-setup.png` for the OpenAI TTS ApiKey setup branch.
- Removed the standalone OpenAI TTS credential menu leaf from the public guide flow so the OpenAI subsection moves directly from configuration to credential type, ApiKey setup, and OAuth2 setup.
- Captured `global-text-to-speech/tts-19-gemini-credential-apikey-setup.png` for the Gemini TTS ApiKey setup branch.
- Corrected the Gemini TTS documentation to show ApiKey setup only; unsupported authentication references and screenshots were removed after review.
- Account identifiers in OpenAI OAuth2 credential screenshots were redacted before saving public screenshots.
- No API key was entered, no OAuth connect/reconnect action was triggered, no credential was validated, no voice/model was changed, and no default provider was changed.

## Global Text-to-Speech Additional Providers

Added after the user requested three more provider sections under `Global Providers Settings > Text-to-Speech`: Eleven Labs TTS, Kokoro MLX TTS, and Qwen3 MLX TTS.

- Captured `global-text-to-speech/tts-20-elevenlabs-overview.png` for the Eleven Labs TTS provider overview.
- Captured `global-text-to-speech/tts-21-elevenlabs-credential-menu.png` for the Eleven Labs TTS credential provider menu.
- Captured `global-text-to-speech/tts-22-elevenlabs-apikey-setup.png` for the Eleven Labs API-key credential sheet opened from the pencil icon.
- Captured `global-text-to-speech/tts-23-elevenlabs-model-menu.png` for the Eleven Labs model menu state before a credential-backed model list is available.
- Captured `global-text-to-speech/tts-24-elevenlabs-voice-menu.png` for the Eleven Labs voice menu state before a credential-backed voice list is available.
- Captured `global-text-to-speech/tts-25-kokoro-mlx-overview.png` for the Kokoro MLX local-provider overview.
- Captured `global-text-to-speech/tts-26-kokoro-voice-menu.png` for the Kokoro MLX voice menu.
- Captured `global-text-to-speech/tts-27-qwen3-mlx-overview.png` for the Qwen3 MLX local-provider overview.
- Captured `global-text-to-speech/tts-28-qwen3-model-manager.png` for the Qwen3 MLX All Models manager.
- Captured `global-text-to-speech/tts-29-qwen3-voice-menu.png` for the Qwen3 MLX voice menu.
- No API key was entered, no model was loaded or deleted, no refresh/play action was triggered, no voice/model/default provider was changed, and no credential was validated.

## Global AI Model Credential Coverage

Added after the user requested the newly added AI Model provider sections to include the credential authentication paths.

- Captured `global-ai-model/anthropic-03-oauth-credential-sheet.png` for the Anthropic OAuth2 credential branch.
- Captured `global-ai-model/anthropic-04-credential-type-menu.png` for the Anthropic credential type menu showing ApiKey and OAuth2.
- Captured `global-ai-model/anthropic-05-apikey-setup.png` for the Anthropic ApiKey setup branch.
- Captured `global-ai-model/gemini-03-oauth-credential-sheet.png` for the Google Gemini AI OAuth2 credential branch.
- Captured `global-ai-model/gemini-04-credential-type-menu.png` for the Google Gemini AI credential type menu showing ApiKey and OAuth2.
- Captured `global-ai-model/gemini-05-apikey-setup.png` for the Google Gemini AI ApiKey setup branch.
- Captured `global-ai-model/groq-03-apikey-setup.png` for the Groq AI ApiKey setup branch.
- Captured `global-ai-model/zai-03-apikey-setup.png` for the Z.AI / GLM ApiKey setup branch.
- Updated Anthropic and Google Gemini AI to follow the same credential sequence as OpenAI: credential type, ApiKey setup, OAuth2 setup, then model selection.
- Updated Groq AI and Z.AI / GLM as API-key-only provider examples in the observed UI.
- Kept Ollama documented as a local API/service setup path; no OAuth2 credential branch was observed for Ollama.
- Credential type was temporarily changed inside Anthropic and Google Gemini AI sheets to capture both branches, then returned to OAuth2. No API key was entered, no credential was validated, no OAuth reconnect/connect action was triggered, no model/default provider was changed, and no local service was started.

## Global AI Model Guide Copy Cleanup

Added after the user requested the AI Model guide to read less like screenshot notes and more like a user manual.

- Captured `global-ai-model/enconvo-cloud-plan-gpt-54-mini-example.png` for the EnConvo Cloud Plan GPT-5.4 mini example.
- Simplified the AI Model Provider Inventory section to one provider-column screenshot plus the provider list.
- Simplified the EnConvo Cloud Plan section to the setup screenshot, the GPT-5.4 mini example, and the Cloud Plan model list.
- Removed `Observed` wording from public inventory headings and removed `masked API key` phrasing from the public guide copy.
- No API key was entered, no credential was validated, no OAuth reconnect/connect action was triggered, and no default provider was changed.

## Remaining Global Provider Sections

Added after the user requested the remaining global provider panes to follow the AI Model and Text-to-Speech guide pattern.

- Captured `global-web-search/web-search-01-xai-default.png` for the current Web Search default, xAI X Search.
- Captured `global-web-search/web-search-02-xai-model-menu.png` for the xAI X Search model menu.
- Captured `global-image-generation/image-generation-01-openai-default.png` for the current Image Generation default, OpenAI.
- Captured `global-image-generation/image-generation-02-openai-model-menu.png` for the OpenAI image model menu.
- Captured `global-image-generation/image-generation-03-cloud-models.png` for EnConvo Cloud image models.
- Captured `global-video-generation/video-generation-01-xai-default.png` for the current Video Generation default, xAI.
- Captured `global-video-generation/video-generation-02-xai-model-menu.png` for the xAI video model menu.
- Captured `global-video-generation/video-generation-03-aspect-ratio-menu.png` for the video aspect ratio menu.
- Captured `global-video-generation/video-generation-04-resolution-menu.png` for the video resolution menu.
- Captured `global-web-fetch/web-fetch-01-local-default.png` for the current Web Fetch default, Local Fetch.
- Captured `global-ocr/ocr-01-ai-model-default.png` for the current OCR default, AI Model OCR.
- Captured `global-ocr/ocr-02-ai-model-provider-menu.png` for the OCR AI Model Provider menu.
- Captured `global-ocr/ocr-03-model-menu.png` for the OCR model menu.
- Captured `global-ocr/ocr-04-reasoning-menu.png` for the OCR reasoning effort menu.
- Added full guide sections for Web Search, Image Generation, Video Generation, Web Fetch, and OCR under Global Providers Settings.
- No provider was changed, no credential was edited or validated, no OAuth flow was started, no generation/fetch/OCR run was triggered, and no default provider was changed.

## Global Provider Credential Sheets

Added after the user noted that Web Search, Image Generation, and Video Generation needed credential-provider pencil coverage.

- Captured `global-web-search/web-search-03-xai-credential-apikey-sheet.png` for the xAI X Search X.AI-GROK ApiKey sheet.
- Captured `global-web-search/web-search-04-xai-credential-type-menu.png` for the xAI X Search credential type menu.
- Captured `global-web-search/web-search-05-xai-credential-oauth-sheet.png` for the xAI X Search OAuth2 sheet.
- Captured `global-image-generation/image-generation-04-openai-credential-apikey-sheet.png` for the OpenAI Image Generation ApiKey sheet.
- Captured `global-image-generation/image-generation-05-openai-credential-type-menu.png` for the OpenAI Image Generation credential type menu.
- Captured `global-image-generation/image-generation-06-openai-credential-oauth-sheet.png` for the OpenAI Image Generation OAuth2 sheet.
- Captured `global-video-generation/video-generation-05-xai-credential-apikey-sheet.png` for the xAI Video Generation X.AI-GROK ApiKey sheet.
- Captured `global-video-generation/video-generation-06-xai-credential-type-menu.png` for the xAI Video Generation credential type menu.
- Captured `global-video-generation/video-generation-07-xai-credential-oauth-sheet.png` for the xAI Video Generation OAuth2 sheet.
- Restored the open credential editors back to the ApiKey branch before closing them.
- No API key was entered, no existing key was copied, no Validate button was clicked, no OAuth Connect button was clicked, and no default provider was changed.

## Global AI Model OpenAI OAuth2 Cycle

Added after the user requested the missing full OpenAI OAuth2 cycle for Global Providers Settings > AI Model > OpenAI.

- Captured `global-ai-model/openai-oauth-cycle-01-connect-sheet.png` for the OpenAI OAuth2 sheet before starting authorization.
- Captured `global-ai-model/openai-oauth-cycle-02-connecting.png` for the EnConvo connecting state immediately after starting authorization.
- Captured `global-ai-model/openai-oauth-cycle-03-browser-account.png` for the OpenAI browser account chooser.
- Captured `global-ai-model/openai-oauth-cycle-04-browser-consent.png` for the OpenAI consent page.
- Captured `global-ai-model/openai-oauth-cycle-05-browser-success.png` for the browser success page. The callback URL and authorization code area in the browser address bar should be treated as private.
- Captured `global-ai-model/openai-oauth-cycle-06-enconvo-connected.png` for the returned EnConvo connected state.
- The live OAuth flow completed and returned OpenAI to Connected status in EnConvo. No authorization code, callback URL, token, or raw credential was stored in the guide.

## Global AI Model Full-Window Credential Recapture

Added after the user noted that several AI Model credential screenshots were cropped or cut off.

- Created a backup of the previous target screenshots outside the public repo at `/Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3-private-backup/full-window-recapture-20260525-203501/`.
- Replaced `global-ai-model/gemini-03-oauth-credential-sheet.png`, `global-ai-model/gemini-04-credential-type-menu.png`, and `global-ai-model/gemini-05-apikey-setup.png` with full-window captures.
- Replaced `global-ai-model/openai-oauth-cycle-05-browser-success.png` and `global-ai-model/openai-oauth-cycle-06-enconvo-connected.png` with full-window captures.
- Replaced `global-ai-model/anthropic-03-oauth-credential-sheet.png`, `global-ai-model/anthropic-04-credential-type-menu.png`, and `global-ai-model/anthropic-05-apikey-setup.png` with full-window captures.
- Applied privacy cover boxes only to visible personal identity areas and the OpenAI browser callback URL area. API-key fields were left as captured unless they also contained personal identity.
- Anthropic and Google Gemini AI credential type was temporarily switched to ApiKey for screenshots and restored to OAuth2 after capture. No credential was validated, no OAuth reconnect/connect action was triggered, and no default provider was changed.

## Global AI Model Anthropic OAuth2 Cycle

Added after the user requested the same full OAuth2 setup coverage for Global Providers Settings > AI Model > Anthropic.

- Reused the existing Mavis Anthropic OAuth2 screenshots because the browser authorization cycle and EnConvo handoff are the same credential flow.
- Copied `agent-mavis/anthropic-oauth-01-choose-oauth2.png` to `global-ai-model/anthropic-oauth-cycle-01-choose-oauth2.png`.
- Copied `agent-mavis/anthropic-oauth-02-connect-anthropic.png` to `global-ai-model/anthropic-oauth-cycle-02-connect-anthropic.png`.
- Copied `agent-mavis/anthropic-oauth-03-authorize.png` to `global-ai-model/anthropic-oauth-cycle-03-browser-authorize.png`.
- Copied `agent-mavis/anthropic-oauth-04-copy-code.png` to `global-ai-model/anthropic-oauth-cycle-04-copy-code.png`.
- Copied `agent-mavis/anthropic-oauth-05-copied-code.png` to `global-ai-model/anthropic-oauth-cycle-05-code-copied.png`.
- Copied `agent-mavis/anthropic-oauth-06-complete-login-done.png` to `global-ai-model/anthropic-oauth-cycle-06-complete-login.png`.
- No live Anthropic OAuth2 authorization was rerun in this pass, and no authorization code, callback URL, token, or raw credential was added to guide prose.

## Personal Identity Screenshot Redaction

Added after the user asked to keep API keys/tokens as-is for now but hide visible personal names and email addresses in screenshots before publishing.

- Created an unredacted backup outside the public repo at `/Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3-private-backup/personal-info-redaction-20260525-201812/`.
- Applied mosaic redaction boxes over visible personal name/email areas while keeping the original screenshot filenames unchanged so the guide image references remain valid.
- Redacted OpenAI identity surfaces in `global-ai-model/openai-03-oauth-sheet.png`, `global-ai-model/openai-oauth-cycle-02-connecting.png`, `global-ai-model/openai-oauth-cycle-03-browser-account.png`, `global-ai-model/openai-oauth-cycle-04-browser-consent.png`, `global-ai-model/openai-oauth-cycle-06-enconvo-connected.png`, and `global-image-generation/image-generation-06-openai-credential-oauth-sheet.png`.
- Redacted xAI identity surfaces in `global-web-search/web-search-05-xai-credential-oauth-sheet.png` and `global-video-generation/video-generation-07-xai-credential-oauth-sheet.png`.
- Redacted Anthropic identity surfaces in `global-ai-model/anthropic-oauth-cycle-01-choose-oauth2.png`, `global-ai-model/anthropic-oauth-cycle-02-connect-anthropic.png`, `global-ai-model/anthropic-oauth-cycle-05-code-copied.png`, `global-ai-model/anthropic-oauth-cycle-06-complete-login.png`, `agent-mavis/anthropic-oauth-01-choose-oauth2.png`, `agent-mavis/anthropic-oauth-02-connect-anthropic.png`, `agent-mavis/anthropic-oauth-05-copied-code.png`, and `agent-mavis/anthropic-oauth-06-complete-login-done.png`.
- Redacted account identity text in `41-account.png`. `40-my-profile.png` was reviewed and left unchanged because no personal name or email address was visible.

## User-Guide Copy Review

Added after the user asked for a full text pass so the guide reads as a configuration manual rather than screenshot descriptions.

- Rewrote `index.html` guide text only; screenshots, image paths, hierarchy, sidebar structure, CSS, and JavaScript behavior were preserved.
- Reworked page-card summaries and guidance across Global Providers, AI Model, Text-to-Speech, Web Search, Image Generation, Video Generation, Web Fetch, OCR, Agents, Context, Extensions, Primary Function Area, Dictation, Account, General, Developer, Create New Agent, and Agent Configuration (Mavis).
- Reworked selected workflow inventories so they explain what users should configure or verify instead of listing UI status labels.
- Reduced screenshot-description wording such as "showing", "visible", "selected", "current", and similar capture-note phrasing in user-facing guide copy.
- No screenshots were recaptured, no settings were changed, no provider credentials were opened, and no deployment was run in this pass.

## Guide Layout Simplification

Added after the user asked the HTML body to start directly with the actual settings guide content and to remove nested card-like framing.

- Removed the visible top introduction block from the rendered document body so the guide starts at Global Providers Settings.
- Removed visible badge labels such as Private, Provider, Voice, Media, and Runtime from rendered page and workflow cards.
- Changed screenshot rendering to a frameless full-width image button with no caption or "Click to enlarge" text.
- Flattened page-card, deep-card, and inventory styling so sections read as a simpler document rather than card-in-card panels.
- No screenshots were edited, no guide hierarchy was changed, and no deployment was run in this pass.

## Duplicate Section Merge

Added after the user noted that Global Provider sections rendered a parent card and then a repeated child section with the same title and similar screenshot.

- Updated the HTML renderer so flat Global Provider child sections, such as AI Model, Text-to-Speech, Web Search, Image Generation, Video Generation, Web Fetch, and OCR, are embedded into the parent page section instead of rendering a second repeated title block.
- Combined the child intro text into the parent section's instruction flow, then rendered the detailed provider subsections below it.
- Preserved screenshots, anchors, sidebar tree structure, and the underlying `sections` data.

## Dictation Post Action Command Deep Dive

Added after the user asked for deeper Dictation documentation covering Post Action Commands.

- Used the live EnConvo Settings UI at `Dictation & Transcription > Dictation` to open `Add Post Action Command`, search `profess`, and select `Change Tone Professional` from Writing Toolkit.
- Verified that `Change Tone Professional` was added to the Post Action Commands list below `Dictation Polish` and `Dictation Translate`.
- Added the user's supplied bottom-center dictation input indicator image as `screenshots/dictation-post-action-indicator.png`.
- `screencapture` failed in this pass with `could not create image from display`, so no additional full-window screenshot was saved.
- No provider credentials, secrets, authorization codes, callback URLs, API keys, or tokens were opened or stored.

## Dictation Post Action Command Step Screenshots

Added after the user noted that the Post Action Command walkthrough needed actual step screenshots, not only text.

- Added `screenshots/dictation-post-action-01-before-add.png` for the Dictation page before opening the add-command sheet.
- Added `screenshots/dictation-post-action-02-search-professional.png` for the `Add Post Action Command` sheet after searching `profess`.
- Added `screenshots/dictation-post-action-03-command-added.png` for the Dictation page after `Change Tone Professional` was added.
- Updated the Dictation workflow renderer so the walkthrough can show a sequence of full screenshots plus the small bottom-center dictation indicator image.
- The step screenshots were captured manually by the user because sandboxed `screencapture` still returned `could not create image from display` even after Screen & System Audio Recording entries were enabled for Codex, Codex Computer Use, node, Terminal, iTerm, and zsh.

## Dictation Post Action Guide Layout Tightening

Added after the user noted that the Dictation Post Action section should pair each text step with its screenshot instead of rendering all text followed by all screenshots.

- Changed the Post Action Command workflow to render step-by-step instruction blocks with the matching screenshot directly under each step.
- Moved the small bottom-center dictation indicator image into the final step about selecting a post action during live voice input.
- Suppressed the old `32-dictation.png` page screenshot for the Dictation page because the new first and final Post Action screenshots cover the same visible pane more specifically.

## Sidebar Anchor Sync

Added after the user checked the deployed Dictation URL and asked for the left panel and content body to stay in sync.

- Added active-link styling for the left navigation and right table of contents.
- Added hash and scroll synchronization so visiting `#dictation-transcription-dictation` opens the matching left-nav branch, highlights `Dictation`, and scrolls it into view.
- Reused the same `hidePageShot` handling in the top-level page renderer so the old `32-dictation.png` screenshot no longer renders on the Dictation page.
