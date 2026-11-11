"""Quality check for a single file interactive learning system.

Usage: python check_lesson.py lesson.html
Prints PASS or FAIL for each check and exits with code 1 if anything fails.
"""
import os
import re
import sys


def main(path):
    html = open(path, encoding="utf-8").read()
    low = html.lower()
    checks = [
        ("Single file: no external scripts", not re.search(r"<script[^>]+src=", low)),
        ("Single file: no external stylesheets", "<link" not in low),
        # The Google Apps Script /exec address added by google-sheet-tracking is allowed
        ("No web addresses (http/https)", not re.search(r"https?://", re.sub(r"https://script\.google\.com/macros/s/[^\"']+/exec", "", low))),
        ("British English language tag (lang=\"en-GB\")", re.search(r"<html[^>]+lang=[\"']en-gb[\"']", low) is not None),
        ("Viewport meta tag for phones", 'name="viewport"' in low),
        ("Has a <title>", re.search(r"<title>[^<]+</title>", low) is not None),
        ("Interactive (contains JavaScript)", "<script" in low),
        ("Has tabs with \"Next\" buttons", "tab" in low and "next" in low),
        ("Has an XP progress bar", "xp" in low),
        ("Self-test shows a score", "score" in low),
        ("Has a \"Restart\" or \"Try again\" button", "restart" in low or "try again" in low),
        ("Has a certificate", "certificate" in low),
        ("No pop up boxes (alert, confirm, prompt)", not re.search(r"\b(alert|confirm|prompt)\s*\(", low)),
        ('No "All of the above" or "None of the above"', not re.search(r"(all|none) of the above", low)),
        ("File size under 300 KB", os.path.getsize(path) < 300 * 1024),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
        failed += not ok
    print()
    print("All checks passed." if not failed else f"{failed} check(s) failed. Fix them and run again.")
    print("Reminder: also confirm by hand that every answer comes from the lecturer's material.")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
