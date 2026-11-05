/**
 * Receives lesson results and adds one row per attempt to a "Results" sheet.
 *
 * Setup (once per Google Sheet):
 * 1. In the Google Sheet: Extensions > Apps Script. Delete what is there and paste this file. Save.
 * 2. Deploy > New deployment > type: Web app.
 *    Execute as: Me. Who has access: Anyone. Deploy, then allow the permissions.
 * 3. Copy the Web app URL (it ends in /exec). That is the WEBHOOK_URL for your lesson.
 *
 * Columns are created automatically from the names the lesson sends,
 * so new fields can be added later without editing this script.
 */
const SHEET_NAME = 'Results';

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(10000); // several students may finish at the same moment
  try {
    const sheet = getSheet_();
    const data = readPayload_(e);
    data.timestamp = new Date();

    const lastCol = sheet.getLastColumn();
    const headers = lastCol ? sheet.getRange(1, 1, 1, lastCol).getValues()[0] : [];
    Object.keys(data).forEach(function (key) {
      if (headers.indexOf(key) === -1) {
        headers.push(key);
        sheet.getRange(1, headers.length).setValue(key);
      }
    });

    sheet.appendRow(headers.map(function (h) {
      const v = data[h];
      if (v === undefined || v === null) return '';
      return typeof v === 'object' && !(v instanceof Date) ? JSON.stringify(v) : v;
    }));

    return json_({ status: 'success' });
  } catch (err) {
    return json_({ status: 'error', message: String(err) });
  } finally {
    lock.releaseLock();
  }
}

// Lets you check the deployment in a browser: open the /exec URL and you should see "ok"
function doGet() {
  return json_({ status: 'ok' });
}

function readPayload_(e) {
  if (e && e.postData && e.postData.contents) {
    try { return JSON.parse(e.postData.contents); } catch (err) { /* fall through */ }
  }
  return Object.assign({}, (e && e.parameter) || {});
}

function getSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  return ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
