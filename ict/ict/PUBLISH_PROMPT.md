# Task: publish one finished chapter into the "ICT Playbook" doc

A chapter has been written as Markdown at `/home/claude/ict/book/<chXX>.md`, with diagram modules in `/home/claude/ict/book/<chXX>_d<N>.jsx`. Your job is to put it into its tab of the shared doc, section by section, with the diagrams embedded where the placeholders are. Do not rewrite or shorten the text: publish it exactly (you may only fix Markdown that the doc refuses, and diagram code the validator refuses).

Tools: `mcp__Claude_Docs__update`, `mcp__Claude_Docs__batch`, `mcp__Claude_Docs__read` (load them with ToolSearch `select:mcp__Claude_Docs__update,mcp__Claude_Docs__batch,mcp__Claude_Docs__read` if they are not loaded). Reference for the doc API: /home/claude/ict/DOC_GUIDE_FULL.txt (lines 139–270 cover editing; lines 443–534 cover diagrams). Read the diagram part before your first diagram.

Your assignment gives: `DOC` (doc id), `FILE` (the tab's file id), `BODY` (the tab's prose node id), `PENDING` (the id of the single pending block in the tab). `C` below means `{"kind":"project","id":"<DOC>"}`.

## Step 0 — read and split
Read the chapter file completely. Split it into: the **lead** (everything before the first line starting with `## `) and the **sections** (each starts at a `## ` line and runs to the next one). A section may contain diagram placeholder lines of the form
`[[DIAGRAM chXX_dN | caption | reading sentence]]`.

## Step 1 — plant the plan (one call)
Replace the tab's pending block with the lead plus one pending block per section, so the reader sees the chapter outline:
```
mcp__Claude_Docs__update(
  ref = {"object":"node","id":"<BODY>"}, engine = "prose", container = C,
  payload = {"ops":[{"op":"replace","target":{"kind":"blocks","ids":["<PENDING>"]},
    "with":{"as":"markdown",
            "blocks":{"s1":{"type":"pending","intent":"<heading of section 1>"},"s2":{"type":"pending","intent":"<heading of section 2>"}, …},
            "from":{"kind":"inline","content":"<lead text>\n\n<?claude block s1?>\n\n<?claude block s2?>\n\n…"}}}]})
```
The ack's `keys` maps `s1` → `[n]`; the full id is `<session>.<n>` where `<session>` is the ack's `session` field (e.g. `mpje5a2t2rz.512`). Record every section's pending id.

## Step 2 — fill each section in order (one call per section or segment)
For a section WITHOUT placeholders:
```
mcp__Claude_Docs__update(ref = {"object":"node","id":"<BODY>"}, engine = "prose", container = C,
  payload = {"ops":[{"op":"replace","target":{"kind":"blocks","ids":["<that section's pending id>"]},
    "with":{"as":"markdown","from":{"kind":"inline","content":"## Heading\n\n<section body>"}}}]})
```
If a section is longer than ~10,000 characters, split it at `### ` boundaries into chunks of ≤ ~10,000 characters: the first chunk replaces the pending block; each later chunk is inserted after the last block written so far:
```
{"op":"insert","target":{"kind":"blocks","ids":["<last block id>"]},"side":"after",
 "source":{"as":"markdown","from":{"kind":"inline","content":"<next chunk>"}}}
```
**Last block id**: the ack's `xml` lists what the op wrote as `<doc op='0'>…</doc>`; take the id of the LAST element directly inside `<doc>` (a list or table counts as one element; ignore ids nested inside it). Ids print short after the first full one (`.455` = `mpje5a2t2rz.455`, prefix = the last full id printed above it); always send the full form.

For a section WITH placeholders, cut it into text segments around the placeholders and go in order:
1. The first text segment (starting with the `## Heading`) replaces the pending block (as above). Note the last block id.
2. For each placeholder: one `batch` that creates the widget AND inserts its embed after the last block id:
```
mcp__Claude_Docs__batch(container = C, batch = [
 {"$lid":"w","verb":"create","object":"node","engine":"widget",
  "payload":{"parent":{"object":"file","id":"<FILE>"},"code":"<the exact contents of chXX_dN.jsx, as one string>"}},
 {"verb":"update","ref":{"object":"node","id":"<BODY>"},"engine":"prose",
  "payload":{"ops":[{"op":"insert","target":{"kind":"blocks","ids":["<last block id>"]},"side":"after",
   "source":{"as":"markdown","blocks":{"dia":{"type":"embed","ref":"node/$lid:w","caption":"<caption>"}},
    "from":{"kind":"inline","content":"<?claude block dia?>\n\n<reading sentence>"}}}]}}])
```
   The new last block id = the reading-sentence paragraph id in the prose member's ack. The widget's id is in `lids.w`.
3. The next text segment (if any) is inserted after that last block id, and so on.

## Diagram problems
- If the widget member is refused (`widget-invalid`, `text-id`, `text-literal`, `segment-literal`, `eval-family`, `provenance`, etc.), read the diagnostic, fix the module following the rules in DOC_GUIDE_FULL.txt lines 443–534 (typical fixes: give every `<text>` a literal unique `data-claude-text-id`; move any `<text>` out of `.map()`; replace `xs[i]` with `.at(i)` or named fields; rename identifiers called `top`/`parent`/`self`/`window`; replace hex colours with tokens), save the fixed code back to the .jsx file, and resend the whole batch. Up to 3 attempts. If it still fails, insert instead an italic paragraph `*Diagram: <caption>. <reading sentence>*` and report it.
- After each diagram publishes, look at it once: `mcp__Claude_Docs__read(ref={"object":"node","id":"<widget id>"}, engine="widget", container=C, payload={"kind":"screenshot"})`. If labels overlap each other or the candles/zones, run past the frame, or the picture is visibly wrong, fix it once: `update(ref={"object":"node","id":"<widget id>"}, engine="widget", container=C, payload={"kind":"draft-edit","edits":[{"quote":{"exact":"<exact stored code snippet>"},"replacement":"<new>"}]})` then `payload={"kind":"publish"}`. Save the final code to the .jsx file. Don't chase perfection: one fix round per diagram.

## Other refusals
- A refused call changed nothing. Read its `code`/`detail`, fix the call (often a Markdown construct the doc doesn't accept: simplify it, e.g. remove nested formatting inside table cells), and resend. `guide(items=["refusal.<code>"])` explains any code.
- Never resend with `force`. Never touch other tabs.

## When done
Reply with only: number of sections published, number of diagrams published (and any replaced by italic notes), and any text you had to change. Under 120 words.
