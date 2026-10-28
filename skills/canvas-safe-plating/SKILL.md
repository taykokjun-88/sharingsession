---
name: canvas-safe-plating
description: Converts an interactive lesson or any HTML into Canvas LMS safe HTML that survives the Rich Content Editor (inline styles only, no scripts), checks it, and gives paste instructions. Use when a lecturer wants to paste content straight into a Canvas Page, or when Canvas has stripped or broken their HTML.
---

# Canvas Safe Plating

Canvas Pages remove anything they consider unsafe. This recipe produces HTML that looks the same after saving as before.

## 1. What Canvas removes (never use these)

- `<script>` and any JavaScript, including `onclick` and other `on...` attributes
- `<style>` blocks, `<link>`, and `<html>`, `<head>`, `<body>` tags
- CSS classes and ids from your own stylesheet (they have no effect without `<style>`)
- `position: fixed`, animations, and custom fonts

## 2. Method

1. **Decide if it can be plated.** If the lesson needs scoring, drag and drop, timers or games, it cannot run inside a Canvas Page. Say so clearly, then give the Google Sites route (section 5) instead of a broken copy.
2. **Convert** using only the safe patterns in section 3. Every element gets inline `style="..."`.
3. **Measure** with section 4. Fix and measure again until everything passes.
4. **Serve** as in section 5.

## 3. Safe patterns

- **Wrapper:** `<div style="max-width:760px;margin:0 auto;font-size:16px;line-height:1.6;color:#1F2937;">`
- **Key idea card:** `<div style="border-left:4px solid #325494;background:#F1F5F9;padding:12px 16px;margin:12px 0;border-radius:0 6px 6px 0;">`
- **Self check question:** the question and its options as a list, then
  `<details style="margin:8px 0 16px;"><summary style="cursor:pointer;font-weight:bold;color:#325494;">Check your answer</summary><p style="margin:8px 0 0;">✓ Answer: ... Because ...</p></details>`
- **Flashcard:** `<details>` with the term in `<summary>` and the meaning inside.
- **Tables:** wrap in `<div style="overflow-x:auto;">`, table `style="width:100%;border-collapse:collapse;"`.
- **Images:** `https://` address only, `style="max-width:100%;height:auto;"`, and a meaningful `alt`.
- Widths in `%` or `max-width`, never fixed widths over 700px.
- Colours: text `#1F2937`, primary `#325494`, correct `#15803D`. Contrast at least 4.5 to 1.

## 4. Measure (quality checks)

If you can run code, save the result and run:

```
python scripts/check_canvas_html.py canvas.html
```

Every line must say PASS. If you cannot run code, check by hand:

- [ ] No `<script>`, `<style>`, `<link>`, `<html>`, `<head>`, `<body>`
- [ ] No `on...=` attributes and no `class=` or `id=` used for styling
- [ ] No `position:fixed`
- [ ] No fixed widths over 700px
- [ ] Every `<img>` has `alt` and an `https://` source
- [ ] Every question has its answer inside `<details>`

## 5. Serve

**If it can be plated:** one code block with the HTML only, then:

1. In Canvas, open or create a Page and click Edit.
2. Click the HTML editor icon `</>` at the bottom right of the editor.
3. Delete what is there, paste the code, click Save.

**If it needs JavaScript:** explain in one sentence why, then give these steps:

1. Google Sites: Insert, Embed, Embed code, paste the full lesson file, Insert, then Publish with public viewing.
2. In Canvas, add the published link to a Module as an External URL, or paste this into the Page HTML editor:

```
<iframe src="PASTE_YOUR_GOOGLE_SITE_LINK_HERE" width="100%" height="800" style="border:0;" loading="lazy" title="Interactive lesson"></iframe>
```
