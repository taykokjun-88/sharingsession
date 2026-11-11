---
name: interactive-lesson-recipe
description: Turns course notes, slides or readings into a complete single file HTML interactive learning system (tabs, key idea cards, a practice builder, an error clinic, a scenario, an apply task, XP and a self-test with a certificate), with a fixed structure, house style and quality checks. Use when a lecturer asks for an interactive lesson, learning system or practice activity for Google Sites and Canvas.
---

# Interactive Lesson Recipe

A fixed recipe for a complete interactive learning system on one topic. Follow every step in order, every time, so the result does not drift between lessons. This is Gongfu Tea: for a quick lesson in minutes, the lecturer can use Microsoft Learning Zone instead.

## 1. Ingredients (ask only for what is missing)

| Ingredient | Default if the lecturer does not say |
|---|---|
| Course or module | ask |
| Topic | ask; if the material is a whole chapter, suggest one topic that suits a 30 to 45 minute lesson |
| Students | first year undergraduates, English as a second language |
| Learning goals | write 3 to 6 "I can..." goals from the material and show them to the lecturer |
| Time on task | 45 minutes |
| Language course? | decide from the material; if yes, add read-aloud and a listening tab (section 3) |
| Language of the content | the language of the material (instructions stay in British English) |
| Material | ask; never build a lesson without the lecturer's material |

## 2. Method

1. **Read the material.** List the key ideas, terms, typical mistakes and one realistic scenario, using only what is in the material.
2. **Plan and confirm.** Show the lecturer a plan: for each tab below, what it will contain from the material. Wait for their OK before building.
3. **Build** one HTML file with these tabs, in this order, each ending with a "Next ➜" button:
   1. **Orientation:** the learning goals as "I can..." statements, and 3 short steps on how to use the system.
   2. **Key ideas:** clickable cards; the front shows a term or question, a click reveals the explanation and one example from the material.
   3. **Practice workshop:** one hands on builder that suits the subject (build a sentence, sort into groups, match causes to effects, order steps). Tap to select and tap to place, so it works on phones.
   4. **Error clinic:** 5 to 8 typical mistakes from the material. Students look for the error first, then press a button for the diagnosis and the corrected version.
   5. **Case or dialogue:** a realistic scenario from the material, with a "hide the text" mode: recall first, then click to reveal.
   6. **Apply it:** a short on screen task (fill in a form, solve a case, label parts) with "Check my answers", marking each part and explaining.
   7. **Listening** (language courses only): 5 to 8 items; play with 🔊, choose the answer, replay allowed.
   8. **Self-test:** 10 to 12 mixed questions, one attempt each, shuffled. Show the score and the missed questions with explanations, and a "Restart" button. 80% or above unlocks a certificate with the student's name, the topic and the date.
4. **Measure** with section 4. Fix anything that fails, then measure again.
5. **Serve** as in section 5. If the file is too long for one reply, stop at the end of a complete tab and ask the lecturer to type "continue". Never leave the file half finished.

## 3. House style (do not change unless the lecturer asks)

- One self contained HTML file. All CSS and JavaScript inline. No external libraries, fonts, images or links.
- `<html lang="en-GB">`, a viewport meta tag, and a `<title>`.
- A header with the course, topic and lecturer's name, and an **XP progress bar** that fills as activities are completed.
- A **support toggle** to show or hide translations or hints.
- **Language courses:** a 🔊 button on every word and sentence using `speechSynthesis` with the right language code (for example `zh-CN`), speed buttons 0.6x, 0.8x and 1.0x, and a pinyin or transcription toggle if the material has one.
- A warm, modern theme that suits the subject, an icon or emoji for each tab, body text at least 18px, line height 1.6.
- Correct `#15803D`, incorrect `#B91C1C`, and never colour alone: also show ✓ or ✗ and words. Contrast at least 4.5 to 1.
- Buttons at least 44px high. Content width at most 960px, centred, works at 375px wide; tabs scroll sideways on a phone.
- Feedback on every answer: right or wrong, then one sentence explaining why, taken from the material.
- Each multiple choice question has exactly one correct answer. No "All of the above" or "None of the above".
- Every message appears on the page. Never use `alert()`, `confirm()` or `prompt()`.
- British English for instructions, short and friendly. Course content stays in the language of the material.

## 4. Measure (quality checks)

If you can run code, save the file and run:

```
python scripts/check_lesson.py lesson.html
```

Every line must say PASS. If you cannot run code, check the same list by hand:

- [ ] Every fact, question and answer can be traced to the lecturer's material. Nothing invented.
- [ ] All tabs from section 2 are present, in order, each with "Next ➜".
- [ ] XP bar, support toggle, self-test with score, "Restart" and a certificate at 80%.
- [ ] Each multiple choice question has exactly one correct answer; no "All/None of the above".
- [ ] Every answer gives feedback with a reason, right or wrong.
- [ ] Builder and tasks work with a finger on a phone.
- [ ] No `alert()`, `confirm()` or `prompt()`.
- [ ] No `http://` or `https://` references, no `<link>`, no `<script src=...>` (only exception: the Google Apps Script `/exec` address added by `google-sheet-tracking`).
- [ ] File size under 300 KB.
- [ ] `lang="en-GB"` and the viewport meta tag are present.

## 5. Serve

1. The complete HTML file in one code block (never a partial file or "the rest stays the same").
2. Then a short note for the lecturer, at most 6 lines:
   - what each tab contains, with the number of items
   - how to test it: save as `lesson.html`, open it in a browser, work through every tab, answer some right and some wrong
   - how to publish: host it on Google Sites (Insert, Embed, Embed code), then link or embed it in Canvas
   - to save each student's self-test result in a Google Sheet, use the `google-sheet-tracking` skill
