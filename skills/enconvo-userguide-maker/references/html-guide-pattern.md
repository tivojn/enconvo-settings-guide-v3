# HTML Guide Pattern

Use this reference when creating or updating `index.html`.

## Structure

Use a docs-style single HTML file:

- fixed top navbar
- left sidebar built from data
- central `<main class="doc">`
- right table of contents for major sections
- screenshot cards with captions

Represent guide content with a JavaScript `sections` array. A simple section:

```js
{
  id: "agents",
  title: "Agents",
  intro: "These panes control the assistants themselves.",
  pages: [
    ["08-agent-list.png", "Agent List", "Create and edit agents.", "Use this to shape agent personality and capability.", "Private"]
  ]
}
```

A nested deep dive:

```js
{
  id: "agent-mavis",
  title: "Agent List: Mavis Deep Dive",
  parent: "agents",
  parentPage: "Agent List",
  intro: "Agents -> Agent List -> Mavis.",
  deepDive: [
    {
      title: "Tools",
      proof: "agent-mavis/tools-manage-full-scroll.png",
      summary: "This is Mavis's capability boundary.",
      steps: [
        "Select Tools, then click Manage.",
        "Scroll the Select Tools manager from enabled core tools to lower utility groups."
      ]
    }
  ],
  pages: [
    ["agent-mavis/tools-01-summary.png", "Tools Summary", "Shows the tool bundle summary.", "Use this to see enabled tool count.", "Tools"]
  ]
}
```

## Hierarchy Alignment

Keep sidebar and article order identical. If the sidebar says:

`Agents > Agent List > Mavis Deep Dive > Tools walkthrough`

then the article content should place Mavis inside the `Agent List` page block and the Tools walkthrough inside Mavis.

Do not render child sections as siblings of their parent page when the user asked for a deep tree.

## CSS Notes

Use quiet docs styling:

- white background
- light gray borders
- 6-8px radius for cards and screenshot frames
- small badges for categories such as `Private`, `Segment`, `Tools`, `Voice`
- no decorative gradients or marketing hero sections

Screenshots should be large enough to inspect. Full-scroll composites may use a narrower max width to keep very tall images readable.

## Capture Log

Append a short dated section for each pass:

- what page or branch was captured
- which tabs and nested drawers were opened
- which scroll segments were saved
- which composites were made
- what changed in the HTML guide

Keep the log factual. It is the audit trail, not the tutorial itself.
