"""Check that HTML will survive the Canvas LMS Rich Content Editor.

Usage: python check_canvas_html.py canvas.html
Prints PASS or FAIL for each check and exits with code 1 if anything fails.
"""
import re
import sys


def main(path):
    html = open(path, encoding="utf-8").read()
    low = html.lower()
    imgs = re.findall(r"<img\b[^>]*>", low)
    # fixed widths only; max-width is fine
    widths = [int(w) for w in re.findall(r"(?<![-a-z])width\s*:\s*(\d+)px", low)]
    checks = [
        ("No <script> or JavaScript", "<script" not in low and "javascript:" not in low),
        ("No event attributes (onclick and similar)", not re.search(r"\son[a-z]+\s*=", low)),
        ("No <style> block", "<style" not in low),
        ("No <link> tags", "<link" not in low),
        ("No <html>, <head> or <body> tags", not re.search(r"<(html|head|body)\b", low)),
        ("No class or id styling", not re.search(r"\s(class|id)\s*=", low)),
        ("No position:fixed", not re.search(r"position\s*:\s*fixed", low)),
        ("No fixed widths over 700px", all(w <= 700 for w in widths)),
        ("Every image has alt text", all("alt=" in i for i in imgs)),
        ("Every image uses https", all(re.search(r"src=[\"']https://", i) for i in imgs)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
        failed += not ok
    print()
    print("All checks passed. Ready to paste into Canvas." if not failed else f"{failed} check(s) failed. Fix them and run again.")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
