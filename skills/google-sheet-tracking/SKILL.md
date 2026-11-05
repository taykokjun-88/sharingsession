---
name: google-sheet-tracking
description: Adds result tracking to a single file interactive lesson so every attempt is saved as a row in the lecturer's Google Sheet, then helps analyse those results. Use when a lecturer wants to see how students did on an interactive lesson, game or quiz hosted on Google Sites.
---

# Google Sheet Tracking

A fixed recipe for collecting student results from an interactive lesson into a Google Sheet, and reading them back as teaching insight.

## 1. Ingredients (ask only for what is missing)

| Ingredient | Default if the lecturer does not say |
|---|---|
| The lesson file | ask; it must be a complete HTML file |
| WEBHOOK_URL | ask; it is the Apps Script Web app URL ending in `/exec` (setup in section 3) |
| What to identify students by | Student ID and name, typed at the start |
| What to record | score, total questions, percentage, time taken, and each wrong answer |

Collect only what the lecturer needs. Never ask students for passwords, IC numbers, phone numbers or other sensitive details.

## 2. Method

1. **Check the lesson** has a clear end (a score or summary screen). If not, add one first.
2. **Add a start screen** with Student ID and Name fields. The lesson cannot start until both are filled.
3. **Record during play**: for each question keep the question id, the student's answer, the correct answer and whether it was right.
4. **Send once at the end** using exactly this pattern, with `WEBHOOK_URL` as a constant at the top of the script:

   ```js
   fetch(WEBHOOK_URL, {
     method: 'POST',
     mode: 'no-cors',
     headers: { 'Content-Type': 'text/plain;charset=utf-8' },
     body: JSON.stringify(payload)
   });
   ```

   `payload` is one flat object: `studentID`, `studentName`, `lessonTitle`, `score`, `total`, `percent`, `seconds`, `wrongAnswers` (a short text list). `no-cors` is required: Google Apps Script does not allow normal cross site requests, and the request still arrives.
5. **Confirm to the student** ("Your result has been sent to your lecturer") and also save the payload in `localStorage` as a backup, so a failed network never loses work.
6. **Keep everything else unchanged**: same questions, same design, same behaviour.
7. **Measure** with section 4, then **serve** as in section 5.

## 3. Google Sheet setup (tell the lecturer, once per Sheet)

1. Create a Google Sheet. **Extensions > Apps Script**.
2. Replace the code with `apps-script/Code.gs` from this skill. Save.
3. **Deploy > New deployment > Web app**. Execute as **Me**. Who has access **Anyone**. Deploy and allow permissions.
4. Copy the **Web app URL** (ends in `/exec`). Open it in a browser: it should show `{"status":"ok"}`.
5. Paste that URL as `WEBHOOK_URL` in the lesson.

After editing the script later, use **Deploy > Manage deployments > Edit > New version**, or the URL keeps running the old code.

## 4. Measure (quality checks)

If you can run code: `python scripts/check_tracking.py lesson.html`. Every line must say PASS. Otherwise check by hand:

- [ ] `WEBHOOK_URL` is defined once and ends in `/exec`
- [ ] The request uses `mode: 'no-cors'` and `text/plain`
- [ ] Student ID and name are required before starting
- [ ] Results are sent once, at the end, not after every question
- [ ] A backup copy is kept in `localStorage`
- [ ] No sensitive personal data is collected
- [ ] Test: finish the lesson once and see a new row appear in the Sheet

## 5. Serve

1. The complete updated HTML file in one code block.
2. A short note: where `WEBHOOK_URL` is, how to test with one attempt, and that the lesson must be republished on Google Sites after the change.

## 6. Reading the results (when the lecturer shares the Sheet as CSV)

Report, in this order: number of attempts and students; average percentage; the three most missed questions with the wrong answer most often chosen; students who may need support (lowest percentage, or many attempts without improvement); one concrete suggestion for the next class. Use only the data given; never guess.
