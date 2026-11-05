"""Check that an interactive lesson sends its results to a Google Sheet correctly.

Usage: python check_tracking.py lesson.html
Prints PASS or FAIL for each check and exits with code 1 if anything fails.
"""
import re
import sys


def main(path):
    html = open(path, encoding="utf-8").read()
    low = html.lower()
    urls = re.findall(r"webhook_url\s*=\s*[\"']([^\"']+)[\"']", html, re.I)
    checks = [
        ("WEBHOOK_URL is defined once", len(urls) == 1),
        ("WEBHOOK_URL is an Apps Script /exec address",
         bool(urls) and urls[0].startswith("https://script.google.com/") and urls[0].rstrip("/").endswith("/exec")),
        ("Sends with fetch to WEBHOOK_URL", re.search(r"fetch\(\s*webhook_url", low) is not None),
        ("Uses mode: 'no-cors'", re.search(r"mode\s*:\s*[\"']no-cors[\"']", low) is not None),
        ("Uses a text/plain body", "text/plain" in low),
        ("Asks for a student ID", re.search(r"student\s*_?id|studentid", low) is not None),
        ("Keeps a localStorage backup", "localstorage.setitem" in low),
        ("No password or IC number fields", not re.search(r"type=[\"']password|ic\s*number|nric", low)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
        failed += not ok
    print()
    print("All checks passed. Finish the lesson once and look for the new row in the Sheet."
          if not failed else f"{failed} check(s) failed. Fix them and run again.")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
