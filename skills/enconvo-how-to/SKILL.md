---
name: enconvo-how-to
description: Answer practical "how do I..." questions about EnConvo Settings, agents, provider defaults, provider-specific setup, credentials, tools, skills, shortcuts, dictation, knowledgebase, account, developer panes, and related EnConvo configuration workflows using the local EnConvo Settings User Guide v3.
metadata:
  short-description: EnConvo Settings how-to answers
---

# EnConvo How-To

Use this skill when the user asks how to do something in EnConvo Settings, especially questions about creating or configuring agents, choosing models, configuring provider defaults, setting up OAuth/API-key credentials, tools, skills, shortcuts, dictation, knowledgebase, account settings, developer tools, or other settings panes.

## Answer Style

- Give direct, step-by-step instructions in plain language.
- Start with how to open EnConvo Settings when the user asks where to begin:
  - With EnConvo frontmost and active, press `Cmd+,`.
  - Or click EnConvo in the macOS menu bar and choose Settings.
- Name the left-sidebar path with arrows, for example `Agents > Agent List`.
- Then name the exact control or tab to click.
- For provider questions, include the provider branch when known, for example `Global Providers Settings > AI Model > OpenAI`, `Global Providers Settings > Text-to-Speech > Edge TTS`, or `Agents > Agent List > Mavis > AI Model`.
- End with a source link to the exact relevant section in the guide when a matching anchor is known.
- Keep answers short unless the user asks for a walkthrough.
- If a step involves secrets, API keys, OAuth codes, callback URLs, account data, logs, recordings, or memory, remind the user to keep those private.
- Do not claim to operate EnConvo unless the user explicitly asks you to control the app.

## Guide Links

Build source links as `GUIDE_BASE_URL + anchor`.

Current `GUIDE_BASE_URL`:
`file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html`

When the production document URL is provided, use it as `GUIDE_BASE_URL` instead of the local file URL. Keep the same `#anchor` suffixes unless the production site changes the IDs.

## Reference

For the main how-to paths, read [references/how-to.md](references/how-to.md).

Original guide source:
`file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html`

## Canonical Example

User: "How to create a new agent in EnConvo?"

Answer:
With EnConvo frontmost, press `Cmd+,`. Or click EnConvo in the macOS menu bar and choose Settings. Then go to `Agents > Agent List`. In the middle Agent List column, open the bottom action menu and click `Create New Agent`. Choose `New Agent` for the default EnConvo setup, `New OpenClaw Agent` for an OpenClaw-first setup, or `New Hermes Agent` for a Hermes-first setup.

Source: `file:///Users/zanearcher/Documents/Codex/2026-05-25/use-ai-tutor-skill-to-help/enconvo-settings-guide-v3/index.html#agent-list-create-create-new-agent-menu`
