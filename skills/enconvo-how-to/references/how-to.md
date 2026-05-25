# EnConvo Settings How-To Reference

Use these paths to answer practical EnConvo Settings questions. Prefer short answers that combine the access method, sidebar path, exact control, and a source link to the closest matching guide anchor.

## Source Links

Build source links as:
`GUIDE_BASE_URL + anchor`

Current `GUIDE_BASE_URL`:
`file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html`

When the production document URL is provided, replace only `GUIDE_BASE_URL` and keep the matching anchor suffix.

## Open Settings

- Press `Cmd+,` while EnConvo is frontmost and active.
- Or click EnConvo in the macOS menu bar and choose Settings.

## Global Provider Defaults

Global Providers Settings define app-wide defaults. New agents inherit these unless their agent-level tabs override them.

- AI model defaults: `Global Providers Settings > AI Model`. Choose the baseline LLM provider, credential provider, model name, reasoning effort, and temperature.
- Text-to-speech defaults: `Global Providers Settings > Text-to-Speech`. Choose spoken-output provider, credential provider, voice, and language.
- Web search defaults: `Global Providers Settings > Web Search`. Choose the default search provider and credential surface.
- Image generation defaults: `Global Providers Settings > Image Generation`.
- Video generation defaults: `Global Providers Settings > Video Generation`.
- Web fetch defaults: `Global Providers Settings > Web Fetch`.
- OCR defaults: `Global Providers Settings > OCR`.

## Agents

- Agent list: `Agents > Agent List`. Create, inspect, and edit individual agents.
- Voice trigger: `Agents > Voice Trigger`. Configure voice activation and spoken-entry behavior.
- Memory: `Agents > Memory Management`. Review and control stored memory. Treat memory content as private.
- IM channels: `Agents > IM Channels`. Configure external messaging channel integrations. Keep account/channel details private.
- Browser companion: `Agents > Browser Companion`. Configure browser-side context or interaction.
- Computer use: `Agents > Computer-Use`. Configure desktop automation and computer-control settings.
- Scheduled jobs: `Agents > Scheduled Jobs`. Configure recurring agent jobs. Verify schedule, timezone, and run target before enabling.
- Skills: `Agents > Skills`. Inspect installed skills and callable capability modules.
- Variables: `Agents > Variables`. Manage reusable values for prompts and templates. Keep secrets and local paths private.

## Create A New Agent

Path: open Settings, then `Agents > Agent List`.

Source anchor:
`#agent-list-create-create-new-agent-menu`

Current source link:
`file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html#agent-list-create-create-new-agent-menu`

Steps:
1. In the middle Agent List column, open the bottom action menu.
2. Click `Create New Agent`.
3. Choose `New Agent` for the default EnConvo model settings, `New OpenClaw Agent` for an OpenClaw-first setup, or `New Hermes Agent` for a Hermes-first setup.

## Configure An Existing Agent

Path: open Settings, then `Agents > Agent List`, then select the agent.

- Agent prompt and behavior: open the agent's `Agent Definition` tab. Use the Instruction editor for the agent's role, behavior, and operating rules. Scroll down for User Message, Working Folder, and attached context files. Expand rows such as `CHARACTER.md` or `IDENTITY.md` only when you need to inspect or edit them.
- Change portrait/icon: click the portrait/icon beside the selected agent name. Choose a local PNG, JPG, GIF, or SVG in the Change Icon dialog.
- Agent model override: open the agent's `AI Model` tab. Choose AI Model Provider, Credential Provider, Model Name, Reasoning Effort, and Temperature when this agent should differ from global defaults.
- Agent tools: open the agent's `Tools` tab, then click `Manage`. Review enabled tools at the top, scroll through tool groups, expand row chevrons for settings, and toggle tools only when you intend to change what the agent can use.
- Agent voice: open the agent's `Text to Speech` tab. Choose agent-level spoken-output provider, voice, and language.
- Agent runtime behavior: open the agent's `More` tab. Scroll through Dynamic Context, Live Screen, Tutor Mode, Run Mode, Response Language, Post Action, and memory controls.

## Credentials And Model Setup

Global credential inventory: `Credential Management > Credential Management`. Keep API keys, OAuth tokens, authorization codes, callback URLs, and account identifiers private.

Agent credential setup path:
1. Open Settings.
2. Go to `Agents > Agent List`.
3. Select the agent.
4. Open `AI Model`.
5. Use the pencil beside `Credential Provider` for local provider setup.
6. Use the gear beside `Credential Provider` to jump to the global Credential Management page.

Credential type options:
- `OAuth2` uses a browser login flow.
- `ApiKey` uses a provider key and base URL.

Anthropic API key setup:
1. Open the agent's `AI Model > Credential Provider` pencil.
2. Open `Credentials Type` and choose `ApiKey`.
3. Enter the API key in the masked field and confirm the base URL.
4. For standard Anthropic, keep the base URL as `https://api.anthropic.com` unless intentionally using a compatible proxy.
5. Click `Validate` to test the credential.

Anthropic OAuth2 setup:
1. Open the agent's `AI Model > Credential Provider` pencil.
2. Choose `OAuth2`.
3. Click `Connect` or `Reconnect to Anthropic`.
4. Authorize in the browser.
5. Click `Copy Code` on the Claude Platform authentication-code page.
6. Return to EnConvo, paste the code into the OAuth Authentication dialog, complete login, and confirm the connected state.

## Context And Extensions

- Context awareness: `Context > Context Awareness`. Configure how much app, screen, or workflow context EnConvo can use.
- Appshots: `Context > Appshots`. Review application snapshot history and configuration. Appshots may include app names and screen content.
- Extension store: `Extensions > Store`. Browse and install EnConvo capabilities.
- Installed extensions: `Extensions > Installed`. Update, disable, or inspect installed extensions.

## Primary Function Area

- Companion Orb: `Primary Function Area > Companion Orb`.
- PopBar: `Primary Function Area > PopBar`.
- SmartBar: `Primary Function Area > SmartBar`.
- Dynamic Island: `Primary Function Area > Dynamic Island`.
- AI Cursor: `Primary Function Area > AI Cursor`.
- Screen Doodle: `Primary Function Area > Screen Doodle`.
- Sidebar: `Primary Function Area > Sidebar`.
- App Sidebar: `Primary Function Area > App Sidebar`.
- Chat Window: `Primary Function Area > Chat Window`.

## Dictation And Transcription

- Dictation models: `Dictation & Transcription > Dictation Models`.
- Dictation behavior: `Dictation & Transcription > Dictation`.
- Dictation history: `Dictation & Transcription > Dictation History`. Treat spoken content as private.
- Dictionary: `Dictation & Transcription > Dictionary`.
- Transcription models: `Dictation & Transcription > Transcription Models`.
- Recordings: `Dictation & Transcription > Recordings`. Treat audio files and titles as private.

## AI Commands, KnowledgeBase, Account, General, Developer

- Add AI command templates: `AI Commands > Store`.
- Manage installed/custom AI commands: `AI Commands > List`.
- Knowledge sources: `KnowledgeBase > KnowledgeBase`. Names, paths, and indexed content may be sensitive.
- Profile: `Account > My Profile`.
- Account/subscription: `Account > Account`.
- Points/credit usage: `Account > Points Usage`.
- General app preferences: `General > General Settings`.
- Keyboard shortcuts: `General > Shortcut Settings`. Use this to avoid conflicts with macOS or other apps.
- Version/build information: `General > About`.
- Developer utilities: `Developer > Developer Tools`.
- Logs: `Developer > Logging`. Logs may include paths, account data, or request metadata.
- API settings: `Developer > APIs`. Keep endpoints, keys, and tokens private.
- CLI instructions: `Developer > CLI Guide`.
