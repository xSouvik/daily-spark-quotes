"""Checks quotes.json before you push it. Run:  python check_quotes.py

The Daily Spark app downloads this file, so a mistake here reaches every phone.
The app already skips broken entries, but this catches them before anyone sees them.
"""
import json
import sys

CATS = {"motivation", "discipline", "courage", "calm", "study", "self_love", "gratitude", "wisdom"}
MAX_TEXT = 400   # the app ignores longer quotes; keep them under ~200 so they fit widgets

path = sys.argv[1] if len(sys.argv) > 1 else "quotes.json"
try:
    data = json.load(open(path, encoding="utf-8"))
except (OSError, ValueError) as e:
    sys.exit(f"Can't read {path}: {e}")

quotes = data.get("quotes")
if not isinstance(quotes, list) or not quotes:
    sys.exit('The file needs a non-empty "quotes" list.')

problems, ids, texts = [], set(), set()
for i, q in enumerate(quotes, 1):
    where = f"#{i} ({q.get('id', 'no id')})"
    if not str(q.get("id", "")).strip():
        problems.append(f"{where}: missing id")
    elif q["id"] in ids:
        problems.append(f"{where}: id used twice")
    ids.add(q.get("id"))
    text = str(q.get("text", "")).strip()
    if not text:
        problems.append(f"{where}: missing text")
    elif len(text) > MAX_TEXT:
        problems.append(f"{where}: text is {len(text)} characters (max {MAX_TEXT})")
    elif len(text) > 200:
        print(f"note  {where}: {len(text)} characters, may be small on widgets")
    if text.lower() in texts:
        problems.append(f"{where}: same text as another quote")
    texts.add(text.lower())
    if q.get("lang", "en") != "en":
        problems.append(f"{where}: lang must be \"en\" (the app is English-only)")
    if q.get("cat") not in CATS:
        problems.append(f"{where}: cat must be one of {', '.join(sorted(CATS))}")
    if any(ord(c) > 0x024F and not (0x2000 <= ord(c) <= 0x206F) for c in text):
        problems.append(f"{where}: text has non-English characters")

if problems:
    print("\n".join(problems))
    sys.exit(f"\n{len(problems)} problem(s). Fix them before pushing.")
print(f"OK: {len(quotes)} quotes, version {data.get('version')}.")
