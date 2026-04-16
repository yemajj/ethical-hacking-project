# Stack Decisions

Why we chose what we chose.

## Flask
Lightweight Python web framework. No magic, easy to read, easy to extend. Right-sized for a solo builder. Python is also the dominant language in security tooling, so it's on-brand.

## Jinja2
Built into Flask. Server-side templates keep things simple — no JS build step, no framework overhead.

## YAML for content
Content lives as files, not in a database. Benefits: edit content in any text editor, version control works naturally, add new lessons by dropping a file. No code changes to add content.

## localStorage for progress and notes
Eliminates database setup entirely for the MVP. Progress and notes are per-browser, which is fine for a personal learning tool. Migrate to SQLite when multi-device sync or sharing is needed.

## Plain CSS
No Tailwind, no Bootstrap. Keeps the stylesheet readable and fully under control. Add a framework later if needed.

## No fake terminal (yet)
Deferred to Pass 2. The MVP value is in the content, not the interactivity. A static step list gets you 80% of the learning value with 10% of the complexity.
