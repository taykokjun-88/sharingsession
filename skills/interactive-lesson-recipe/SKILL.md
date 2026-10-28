---
name: interactive-lesson-recipe
description: Turns course notes, slides or question sets into a single file HTML interactive lesson with a fixed structure, house style and quality checks, so every lesson comes out the same standard. Use when a lecturer asks for an interactive lesson, self check quiz or practice activity for Canvas or Google Sites.
---

# Interactive Lesson Recipe

A fixed recipe for interactive lessons. Follow every step in order, every time, so the result does not drift between lessons.

## 1. Ingredients (ask only for what is missing)

| Ingredient | Default if the lecturer does not say |
|---|---|
| Course or module | ask |
| Topic | ask |
| Students | first year undergraduates, English as a second language |
| Learning goal | write one from the material and show it to the lecturer |
| Activity types | multiple choice with feedback, plus one of: matching, sorting, fill in the blanks |
| Material | ask; never write a lesson without the lecturer's material |

## 2. Method

1. **Read the material.** List 3 to 5 key ideas, using only facts found in the material.
2. **Plan the lesson** in this fixed order:
   1. Title and one sentence learning goal
   2. Key ideas: short cards, at most 120 words in total
   3. Activity 1: multiple choice, 5 to 8 questions
   4. Activity 2: the second activity type, 5 to 8 items
   5. Summary: score, list of missed items with the correct answers, and a "Try again" button
3. **Build** one HTML file using the house style below.
4. **Measure** with the checks in section 4. Fix anything that fails, then measure again.
5. **Serve** in the format in section 5.

## 3. House style (do not change unless the lecturer asks)

- One self contained HTML file. All CSS and JavaScript inline. No external libraries, fonts, images or links.
- `<html lang="en-GB">`, a viewport meta tag, and a `<title>`.
- Font: `system-ui, 'Segoe UI', Arial, sans-serif`, body at least 18px, line height 1.6.
- Colours: background `#FFFFFF`, text `#1F2937`, primary `#325494`, correct `#15803D`, incorrect `#B91C1C`. Never rely on colour alone: also show ✓ or ✗ and words.
- Buttons at least 44px high. Content width at most 760px, centred, works at 375px wide.
- Feedback on every answer: say right or wrong, then one sentence explaining why, taken from the material.
- Progress shown as "Question 3 of 8" and a running score.
- Shuffle question order and answer options on each load.
- British English. Short, friendly instructions.

## 4. Measure (quality checks)

If you can run code, save the file and run:

```
python scripts/check_lesson.py lesson.html
```

Every line must say PASS. If you cannot run code, check the same list by hand:

- [ ] Every question and answer can be traced to the lecturer's material. Nothing invented.
- [ ] Each multiple choice question has exactly one correct answer.
- [ ] Every answer gives feedback with a reason.
- [ ] Score, progress and a "Try again" button are present.
- [ ] No `http://` or `https://` references, no `<link>`, no `<script src=...>`.
- [ ] File size under 200 KB.
- [ ] `lang="en-GB"` and the viewport meta tag are present.

## 5. Serve

1. The complete HTML file in one code block (never a partial file or "the rest stays the same").
2. Then a short note for the lecturer, at most 5 lines:
   - what the lesson contains (activities and number of items)
   - how to test it: save as `lesson.html`, open in a browser, answer some right and some wrong
   - how to publish: this file uses JavaScript, so host it on Google Sites (Insert, Embed, Embed code) and link or embed it in Canvas. For a version that pastes straight into a Canvas Page, use the `canvas-safe-plating` skill.
