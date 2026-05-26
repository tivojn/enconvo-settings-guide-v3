# EnConvo Settings How-To Reference

Use this reference to answer practical EnConvo Settings questions. Prefer short answers that combine:

1. How to open Settings.
2. The left-sidebar path.
3. The exact tab, menu, pencil, gear, switch, or button to use.
4. A privacy reminder when credentials, OAuth codes, recordings, logs, memory, or knowledge sources are involved.
5. **Always** a source URI to the closest guide anchor, rendered as plain text (not just a markdown link) so the URL is visible. Prefer the most specific matching anchor, especially credential-type, OAuth2, and ApiKey pages. If no exact anchor appears in this reference, do not claim it is absent unless you have checked the guide's generated anchor list; otherwise link the nearest parent section without speculation.

## Source Links

Build source links as:
`GUIDE_BASE_URL + anchor`

Current `GUIDE_BASE_URL`:
`file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html`

When the production document URL is provided, replace only `GUIDE_BASE_URL` and keep the matching anchor suffix.

## Open Settings

- Press `Cmd+,` while EnConvo is frontmost and active.
- Or click EnConvo in the macOS menu bar and choose Settings.

## Answer Patterns

Provider-default answer:
- Start at `Global Providers Settings > [provider pane]`.
- Pick the provider from the middle provider list or provider menu.
- Confirm the credential provider before choosing a model, voice, output setting, or default.
- Use `Set as Default Provider` only after the provider and credential are ready.

Credential answer:
- For local setup, use the pencil beside `Credential Provider`.
- For central credential inventory, use the gear beside `Credential Provider` or go to `Credential Management > Credential Management`.
- `OAuth2` uses browser account authorization.
- `ApiKey` uses a provider key, API type/base URL when exposed, and `Validate`.
- Remind the user to keep API keys, OAuth codes, callback URLs, tokens, and account identifiers private.

Agent answer:
- Start at `Agents > Agent List`.
- Select the agent, then choose the relevant tab: `Agent Definition`, `AI Model`, `Tools`, `Text to Speech`, or `More`.
- Agent tabs can override global provider defaults.
- For the worked example in the guide, use the Mavis anchors under `Agent Configuration (Mavis)`.

## Global Providers Settings

Top-level path: `Global Providers Settings`.

- AI model defaults: `Global Providers Settings > AI Model`. Choose the app-wide LLM provider, credential provider, model name, reasoning effort, and temperature. Source: `#global-providers-ai-model`.
- Text-to-speech defaults: `Global Providers Settings > Text-to-Speech`. Choose the app-wide voice provider, credential, voice, language, output format, and speed. Source: `#global-providers-text-to-speech`.
- Web search defaults: `Global Providers Settings > Web Search`. Choose the backend for current web/social-search context. Source: `#global-providers-web-search`.
- Image generation defaults: `Global Providers Settings > Image Generation`. Choose managed Cloud image models or credential-backed custom providers. Source: `#global-providers-image-generation`.
- Video generation defaults: `Global Providers Settings > Video Generation`. Choose provider, model, duration, aspect ratio, and resolution. Source: `#global-providers-video-generation`.
- Web fetch defaults: `Global Providers Settings > Web Fetch`. Choose how URL content is retrieved and extracted. Source: `#global-providers-web-fetch`.
- OCR defaults: `Global Providers Settings > OCR`. Choose local/native, Cloud, or model-backed OCR behavior. Source: `#global-providers-ocr`.

## Global AI Model Setup

Path: `Global Providers Settings > AI Model`.

Use this pane when choosing the app-wide model default inherited by new agents.

- Cloud Plan: choose `EnConvo Cloud Plan`, then choose `Model Name`, `Reasoning Effort`, and `Temperature`. Use `Set as Default Provider` only when this should become the app-wide default. Source: `#global-ai-model-enconvo-cloud-plan-setup`.
- Provider inventory: use the provider column to choose EnConvo Cloud Plan, OpenAI, OpenClaw, Hermes Agent, Anthropic, Google Gemini AI, Ollama, Groq AI, Z.AI, OpenRouter, LM Studio, MLX, and other providers. Source: `#global-ai-model-ai-model-provider-inventory`.
- OpenAI global setup: choose `OpenAI`, select or create an OpenAI credential, use the pencil beside `Credential Provider`, choose `OAuth2` or `ApiKey`, then choose model/runtime options. Source: `#global-ai-model-openai-global-provider-setup`.
- OpenAI OAuth2: choose `OAuth2`, click `Connect` or `Reconnect to OpenAI`, choose the account in Chrome, review consent, return after browser success, and confirm `Connected`. Source: `#global-ai-model-openai-oauth2-connect-or-reconnect`.
- OpenAI ApiKey: choose `ApiKey`, enter the OpenAI key, confirm API type/base URL, then validate when ready. Source: `#global-ai-model-openai-apikey-setup`.
- Anthropic global setup: choose `Anthropic`, configure the Anthropic credential, then choose Claude model, reasoning effort, and temperature. Source: `#global-ai-model-anthropic-global-provider-setup`.
- Anthropic OAuth2: choose `OAuth2`, click `Connect` or `Reconnect to Anthropic`, authorize in the browser, copy the code, return to EnConvo, paste it into OAuth Authentication, and complete login. Source: `#global-ai-model-anthropic-oauth2-complete-login`.
- Anthropic ApiKey: choose `ApiKey`, enter the Claude API key, keep the base URL as `https://api.anthropic.com` unless intentionally using a compatible proxy, then validate. Source: `#global-ai-model-anthropic-api-key-setup`.
- Google Gemini AI: choose `Google Gemini AI`, configure OAuth2 or ApiKey, choose the Gemini model, and enable Google Search Tool, URL Context Tool, or Show thoughts only when those should apply globally. Source: `#global-ai-model-google-gemini-ai-global-provider-setup`.
- Ollama: choose `Ollama`, make sure the local Ollama service is running, confirm the local API endpoint, choose an installed model, then set as default only when local models should be the global route. Source: `#global-ai-model-ollama-global-provider-setup`.
- Groq AI: choose `Groq AI`, configure the Groq API key, keep the standard OpenAI-compatible base URL unless intentionally using a gateway, then choose a Groq-hosted model. Source: `#global-ai-model-groq-ai-global-provider-setup`.
- Z.AI / GLM: choose `Z.AI`, configure the Z.AI API key, refresh/load model choices, then choose the GLM model. Source: `#global-ai-model-z-ai-glm-global-provider-setup`.

## Global Text-To-Speech Setup

Path: `Global Providers Settings > Text-to-Speech`.

Use this pane when configuring app-wide spoken-output defaults.

- Provider inventory: choose between Cloud Plan, direct online providers, no-key providers, and local MLX providers. Source: `#global-text-to-speech-provider-inventory`.
- EnConvo Cloud Plan TTS: use EnConvo Cloud as the credential provider when subscription-backed speech should avoid separate provider keys. Source: `#global-text-to-speech-enconvo-cloud-plan-tts`.
- Edge TTS: no API key path. Configure preview text, voice, and output format. Source: `#global-text-to-speech-edge-tts-configuration`.
- OpenAI TTS: choose the OpenAI TTS provider, configure OAuth2 or ApiKey through the credential pencil, then choose model, voice, and speed. Source: `#global-text-to-speech-openai-tts-configuration`.
- OpenAI TTS credential type: use the credential sheet's `Credentials Type` menu to choose OAuth2 or ApiKey. Source: `#global-text-to-speech-openai-tts-credential-type-menu`.
- OpenAI TTS OAuth2: choose `OAuth2`, review the connected account area, then use `Connect` or `Reconnect` only when you intend to authorize or repair the OpenAI account connection. Source: `#global-text-to-speech-openai-tts-oauth2-credential-sheet`.
- OpenAI TTS ApiKey: choose `ApiKey`, paste the OpenAI API key, confirm API type/base URL when shown, and validate only when ready. Source: `#global-text-to-speech-openai-tts-apikey-setup`.
- Gemini TTS: configure the Gemini ApiKey credential first, then choose TTS model and speaking voice. Source: `#global-text-to-speech-gemini-tts-configuration`.
- Gemini TTS ApiKey: paste the Gemini API key, confirm the base URL, then validate only when ready. Source: `#global-text-to-speech-gemini-tts-apikey-setup`.
- xAI TTS: configure the xAI credential through OAuth2 or ApiKey, then choose xAI voice/language behavior. Source: `#global-text-to-speech-xai-tts-configuration`.
- xAI TTS credential type: click the pencil beside `Credential Provider`, then use `Credentials Type` to choose `OAuth2` for browser account authorization or `ApiKey` for direct key setup. Source: `#global-text-to-speech-xai-tts-credential-type-menu`.
- xAI TTS OAuth2: choose `OAuth2`, review the connected account area, then click `Connect` or `Reconnect` only when you intend to authorize, change, or repair the xAI account connection. Source: `#global-text-to-speech-xai-tts-oauth2-credential-sheet`.
- xAI TTS ApiKey: choose `ApiKey`, paste the xAI API key, and validate only after confirming the key is correct. Source: `#global-text-to-speech-xai-tts-apikey-setup`.
- Eleven Labs TTS: configure the Eleven Labs API key, then refresh/open model and voice menus before making it default. Source: `#global-text-to-speech-eleven-labs-tts-configuration`.
- Eleven Labs TTS ApiKey: paste the Eleven Labs API key, validate when ready, then return to choose model and voice. Source: `#global-text-to-speech-eleven-labs-tts-apikey-setup`.
- Kokoro MLX TTS: local on-device TTS through the `mlx_manage` extension; choose a local Kokoro voice preset. Source: `#global-text-to-speech-kokoro-mlx-tts-configuration`.
- Qwen3 MLX TTS: local on-device TTS with Qwen3-TTS variants, voices, and an Instruction field for style/emotion guidance. Source: `#global-text-to-speech-qwen3-mlx-tts-configuration`.

## Web Search, Media, Web Fetch, And OCR

Web Search path: `Global Providers Settings > Web Search`.
- Provider inventory: choose the global search backend and credential route. Source: `#global-web-search-provider-inventory`.
- xAI X Search: choose `xAI X Search`, confirm `X.AI-GROK` credential, configure OAuth2 or ApiKey if needed, then choose the search model. Source: `#global-web-search-xai-x-search-configuration`.

Image Generation path: `Global Providers Settings > Image Generation`.
- Provider inventory: choose EnConvo Cloud image models or custom credential-backed providers. Source: `#global-image-generation-provider-inventory`.
- EnConvo Cloud Image Models: use managed image generation/editing models without separate provider credentials. Source: `#global-image-generation-enconvo-cloud-image-models`.
- OpenAI Image Generation: open `Custom Providers`, confirm the OpenAI credential, configure OAuth2 or ApiKey if needed, then choose the image model. Source: `#global-image-generation-openai-image-generation-configuration`.

Video Generation path: `Global Providers Settings > Video Generation`.
- Provider inventory: choose the global backend and output defaults for video commands. Source: `#global-video-generation-provider-inventory`.
- xAI Video Generation: choose `xAI`, confirm the `X.AI-GROK` credential, configure OAuth2 or ApiKey if needed, then set model, duration, aspect ratio, and resolution. Source: `#global-video-generation-xai-video-generation-configuration`.

Web Fetch path: `Global Providers Settings > Web Fetch`.
- Provider inventory: choose how URL content is retrieved before it is summarized or passed to agents. Source: `#global-web-fetch-provider-inventory`.
- Local Fetch: choose `Local Fetch` for local URL extraction without a provider credential; adjust max length, start index, and raw HTML only when needed. Source: `#global-web-fetch-local-fetch-configuration`.

OCR path: `Global Providers Settings > OCR`.
- Provider inventory: choose the default OCR engine, including AI Model OCR, Apple Native OCR, or Mistral OCR where configured. Source: `#global-ocr-provider-inventory`.
- AI Model OCR: choose AI Model OCR, pick AI Model Provider and Model Name, keep temperature deterministic for extraction, and raise reasoning only for difficult layouts. Source: `#global-ocr-ai-model-ocr-configuration`.

## Agents

Top-level path: `Agents`.

- Agent list: `Agents > Agent List`. Create, inspect, and edit individual agents. Source: `#agents-agent-list`.
- Voice trigger: `Agents > Voice Trigger`. Configure voice phrases or spoken entry points. Source: `#agents-voice-trigger`.
- Memory: `Agents > Memory Management`. Review and control stored memory. Treat memory content as private. Source: `#agents-memory-management`.
- IM channels: `Agents > IM Channels`. Configure external messaging channel integrations. Keep account/channel details private. Source: `#agents-im-channels`.
- Browser companion: `Agents > Browser Companion`. Configure browser-side helper behavior. Source: `#agents-browser-companion`.
- Computer use: `Agents > Computer-Use`. Configure desktop automation permissions. Source: `#agents-computer-use`.
- Scheduled jobs: `Agents > Scheduled Jobs`. Configure recurring agent jobs. Verify schedule, timezone, and run target before enabling. Source: `#agents-scheduled-jobs`.
- Skills: `Agents > Skills`. Manage specialized workflows agents can invoke. Source: `#agents-skills`.
- Variables: `Agents > Variables`. Manage reusable prompt/template values. Keep secrets and local paths private. Source: `#agents-variables`.

## Create A New Agent

Path: `Agents > Agent List`.

Steps:
1. In the middle Agent List column, open the bottom action menu.
2. Click `Create New Agent`.
3. Choose `New Agent` for the default EnConvo setup, `New OpenClaw Agent` for an OpenClaw-first setup, or `New Hermes Agent` for a Hermes-first setup.

Source: `#agent-list-create-create-new-agent-menu`.

## Configure An Existing Agent

Path: `Agents > Agent List > [agent name]`.

Mavis is the guide's worked example, but the same tab pattern applies to other agents.

- Change portrait/icon: click the portrait beside the selected agent name and choose a local PNG, JPG, GIF, or SVG. Source: `#agent-mavis-change-agent-portrait`.
- Agent prompt and behavior: open `Agent Definition`. Use `Instruction` for role/behavior rules, then scroll for `User Message`, `Working Folder`, and attached files. Source: `#agent-mavis-agent-definition-full-scroll`.
- Expanded prompt leaves: expand lower rows such as `User Message`, `CHARACTER.md`, or `IDENTITY.md` only when you need to inspect or edit nested prompt content. Source: `#agent-mavis-agent-definition-leaves`.
- Agent model override: open `AI Model`. Choose `Global Provider` to inherit app defaults, or choose a direct provider when this agent needs its own model path. Source: `#agent-mavis-ai-model-override`.
- Agent credential pencil: in `AI Model`, click the pencil beside `Credential Provider` to open local provider setup. Source: `#agent-mavis-ai-model-pencil-and-gear-entrances`.
- Agent credential gear: in `AI Model`, click the gear beside `Credential Provider` to jump to global `Credential Management`. Source: `#agent-mavis-ai-model-pencil-and-gear-entrances`.
- Agent Anthropic ApiKey: open `AI Model > Credential Provider` pencil, choose `ApiKey`, enter the key, confirm base URL, and validate. Source: `#agent-mavis-anthropic-apikey-setup-cycle`.
- Agent Anthropic OAuth2: open `AI Model > Credential Provider` pencil, choose `OAuth2`, connect in browser, copy the code, return to EnConvo, paste, complete login, and confirm connected state. Source: `#agent-mavis-anthropic-oauth2-setup-cycle`.
- Agent tools: open `Tools`, click `Manage`, review enabled tools, expand row chevrons for settings, and toggle only the capabilities the agent should use. Source: `#agent-mavis-tools-manager`.
- Agent voice: open `Text to Speech` to override global spoken-output provider, voice, and language for that agent. Source: `#agent-mavis-text-to-speech`.
- Agent runtime behavior: open `More` to configure Dynamic Context, Live Screen, Tutor Mode, Run Mode, Response Language, Post Action, and memory controls. Source: `#agent-mavis-more-runtime-settings`.

## Credentials And Model Setup

Global path: `Credential Management > Credential Management`.

- Use Credential Management as the central provider-account and credential inventory. Source: `#credential-management-credential-management`.
- Keep API keys, OAuth tokens, authorization codes, callback URLs, and account identifiers private.
- Agent setup path: `Agents > Agent List > [agent] > AI Model`.
- Global setup path: `Global Providers Settings > AI Model` or the matching provider pane.
- Pencil beside `Credential Provider`: opens local provider setup.
- Gear beside `Credential Provider`: opens central Credential Management.
- `OAuth2`: browser login/authorization flow.
- `ApiKey`: pasted provider key plus API type/base URL when exposed.

## Context And Extensions

- Context awareness: `Context > Context Awareness`. Configure how much app, screen, or workflow context EnConvo can use. Source: `#context-context-awareness`.
- Appshots: `Context > Appshots`. Review application snapshot history and configuration. Appshots may include app names and screen content. Source: `#context-appshots`.
- Extension store: `Extensions > Store`. Browse and install EnConvo capabilities. Source: `#extensions-store`.
- Installed extensions: `Extensions > Installed`. Update, disable, or inspect installed extensions. Source: `#extensions-installed`.

## Primary Function Area

- Companion Orb: `Primary Function Area > Companion Orb`. Source: `#primary-function-area-companion-orb`.
- PopBar: `Primary Function Area > PopBar`. Source: `#primary-function-area-popbar`.
- SmartBar: `Primary Function Area > SmartBar`. Source: `#primary-function-area-smartbar`.
- Dynamic Island: `Primary Function Area > Dynamic Island`. Source: `#primary-function-area-dynamic-island`.
- AI Cursor: `Primary Function Area > AI Cursor`. Source: `#primary-function-area-ai-cursor`.
- Screen Doodle: `Primary Function Area > Screen Doodle`. Source: `#primary-function-area-screen-doodle`.
- Sidebar: `Primary Function Area > Sidebar`. Source: `#primary-function-area-sidebar`.
- App Sidebar: `Primary Function Area > App Sidebar`. Source: `#primary-function-area-app-sidebar`.
- Chat Window: `Primary Function Area > Chat Window`. Source: `#primary-function-area-chat-window`.

## Dictation And Transcription

- Dictation models: `Dictation & Transcription > Dictation Models`. Choose the model for live speech-to-text. Source: `#dictation-transcription-dictation-models`.
- Dictation behavior: `Dictation & Transcription > Dictation`. Tune live listening, transcription, and insertion behavior. Source: `#dictation-transcription-dictation`.
- Dictation history: `Dictation & Transcription > Dictation History`. Treat spoken content as private. Source: `#dictation-transcription-dictation-history`.
- Dictionary: `Dictation & Transcription > Dictionary`. Add vocabulary hints for better recognition. Source: `#dictation-transcription-dictionary`.
- Transcription models: `Dictation & Transcription > Transcription Models`. Choose the model for file-based transcription. Source: `#dictation-transcription-transcription-models`.
- Recordings: `Dictation & Transcription > Recordings`. Treat audio files, titles, and transcripts as private. Source: `#dictation-transcription-recordings`.

## AI Commands, KnowledgeBase, Account, General, Developer

- Add AI command templates: `AI Commands > Store`. Source: `#ai-commands-store`.
- Manage installed/custom AI commands: `AI Commands > List`. Source: `#ai-commands-list`.
- Knowledge sources: `KnowledgeBase > KnowledgeBase`. Names, paths, and indexed content may be sensitive. Source: `#knowledgebase-knowledgebase`.
- Profile: `Account > My Profile`. Source: `#account-my-profile`.
- Account/subscription: `Account > Account`. Source: `#account-account`.
- Points/credit usage: `Account > Points Usage`. Source: `#account-points-usage`.
- General app preferences: `General > General Settings`. Source: `#general-general-settings`.
- Keyboard shortcuts: `General > Shortcut Settings`. Use this to avoid conflicts with macOS or other apps. Source: `#general-shortcut-settings`.
- Version/build information: `General > About`. Source: `#general-about`.
- Developer utilities: `Developer > Developer Tools`. Source: `#developer-developer-tools`.
- Logs: `Developer > Logging`. Logs may include paths, account data, request metadata, or provider details. Source: `#developer-logging`.
- API settings: `Developer > APIs`. Keep endpoints, keys, and tokens private. Source: `#developer-apis`.
- CLI instructions: `Developer > CLI Guide`. Source: `#developer-cli-guide`.

## Default Shortcut Settings

Path: `General > Shortcut Settings`.

Use this list when the user asks for EnConvo's default shortcuts. Source: `#general-shortcut-settings`.

Windows:
- Show Smart Bar: `⇧+⌘+D`. Opens the main Smart Bar.
- Show Chat Window: `⌥+⌘+D`, trigger mode `Normal`. Opens the full chat window.
- Show Sidebar: `⇧+⌘+U`, trigger mode `Normal`. Opens the floating sidebar.
- Show App Sidebar: `⇧+⌘+T`, trigger mode `Normal`. Opens the application sidebar.
- Dynamic Island: not assigned by default. Shows, expands, or collapses Dynamic Island.

Voice:
- Dictation: `Right ⌘`, trigger mode `Hold or Toggle`. Starts voice-to-text dictation.
- Voice Command: `Right ⌥`, trigger mode `Hold or Toggle`. Runs commands from voice input.

Actions:
- Clear Conversation: `⌥+K`, trigger mode `Normal`. Clears the current Smart Bar conversation.
- Pin Smart Bar: `⌘+P`, trigger mode `Normal`. Keeps the current Smart Bar window pinned.
- Settings: `⌘+,`, trigger mode `Normal`. Opens EnConvo settings.
- Screen Doodle: `⇧+⌘+7`. Toggles the full-screen doodle overlay.
- Screenshot: `⌃+S`, trigger mode `Normal`. Captures a selected screen area.
- Translate: `⌥+D`, trigger mode `Normal`. Translates selected text or input.
- Silent OCR: `⌥+S`, trigger mode `Normal`. Captures an area and copies OCR text to the clipboard.
