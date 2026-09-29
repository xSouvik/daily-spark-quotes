# Daily Spark quotes

The quotes shown in the Daily Spark app. The app downloads `quotes.json` from this repo
about once a day, so adding quotes here reaches every phone **without an app update**.

App URL: `https://raw.githubusercontent.com/xSouvik/daily-spark-quotes/main/quotes.json`
(set as `QUOTES_URL` in the app's `app/build.gradle.kts`).

## Add quotes

1. Add entries to `quotes.json`:

   ```json
   { "id": "en151", "text": "Your quote here.", "author": "", "cat": "motivation", "lang": "en" }
   ```

   - `id`: unique and never reused. Continue the numbering.
   - `cat`: motivation, discipline, courage, calm, study, self_love, gratitude or wisdom.
   - `lang`: always `en`. The app is English-only and skips anything else.
   - `author`: leave empty for proverbs and original lines.
   - At most 160 characters, so every quote fits the smallest widget.
   - Only public-domain quotes, proverbs, or lines you wrote.
2. Bump `version` at the top.
3. Run `python check_quotes.py`. It must say OK.
4. Commit and push. Phones pick it up within a day.

## Safety

- The app keeps the last good download. A broken file never wipes quotes off anyone's phone.
- Quotes over 160 characters, non-English quotes, and entries without an id or text are skipped.
- Deleting a quote removes it from phones at the next sync. A user's saved favourite of it
  simply stops showing.
