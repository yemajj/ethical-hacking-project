# Plan: Cybersecurity Education Web App — Phase 1 MVP (Revised)

## Revised Scope Summary (1-weekend target)

**Build:**
- Flask skeleton + homepage
- Lesson page template (renders YAML content)
- Exercise page template (static steps — no fake terminal yet)
- Notes area (localStorage)
- Progress tracking (localStorage)
- 3 lessons + 3 exercises: pwd, ls, cd (minimal YAML)
- 7 docs files

**Defer to pass 2:** Fake terminal, step validation, command input
**Defer to pass 3:** SQLite, multi-user, search, admin panel

**Done when:** You can open the app, read a lesson, read its exercise steps, take notes, and mark the lesson complete. That is the entire MVP.

---

## Context

Building a beginner-friendly cybersecurity education platform. Phase 1 = Terminal Foundations (pwd, ls, cd). Dual goals: personal learning + shareable tool for beginners. Flask + Jinja2 + YAML content + localStorage for notes/progress. No auth, no DB, no unnecessary complexity.

---

## Tech Stack

| Layer | Choice |
|---|---|
| Backend | Flask |
| Templates | Jinja2 |
| Content | YAML files in `content/` |
| Progress + Notes | localStorage (browser) |
| Styling | Plain CSS |
| Python deps | Flask + PyYAML + mistune (Markdown → HTML) |

---

## Folder Structure

```
cyber-edu/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── content_loader.py
├── content/
│   └── phases/
│       └── phase1/
│           ├── meta.yaml
│           └── terminal-foundations/
│               ├── meta.yaml
│               ├── lessons/
│               │   ├── 01_pwd.yaml
│               │   ├── 02_ls.yaml
│               │   └── 03_cd.yaml
│               └── exercises/
│                   ├── 01_pwd.yaml
│                   ├── 02_ls.yaml
│                   └── 03_cd.yaml
├── static/
│   ├── css/
│   │   └── main.css
│   └── js/
│       └── progress.js
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── lesson.html
│   └── exercise.html
├── docs/
│   ├── roadmap.md
│   ├── curriculum_plan.md
│   ├── mvp_checklist.md
│   ├── learning_journal.md
│   ├── content_guide.md
│   ├── stack_decisions.md
│   └── learning_loop.md
├── config.py
├── requirements.txt
├── run.py
└── .gitignore
```

---

## Minimal YAML Schemas

### Lesson (`content/phases/phase1/terminal-foundations/lessons/01_pwd.yaml`)
```yaml
id: pwd
title: "pwd — Print Working Directory"
order: 1
description: "Learn how to find your current location in the filesystem."
body: |
  Markdown content here...
key_points:
  - pwd stands for Print Working Directory
  - Output always starts with /
  - No arguments needed
next_lesson: ls
```

### Exercise (`content/phases/phase1/terminal-foundations/exercises/01_pwd.yaml`)
```yaml
id: pwd_exercise
lesson_id: pwd
title: "Practice: pwd"
steps:
  - prompt: "You are in /home/user. What command shows your location?"
    expected: "pwd"
    output: "/home/user"
  - prompt: "You moved to /etc/nginx. Run pwd again."
    expected: "pwd"
    output: "/etc/nginx"
```

### Module meta (`terminal-foundations/meta.yaml`)
```yaml
id: terminal-foundations
title: "Terminal Foundations"
description: "Master the command line basics."
lessons:
  - pwd
  - ls
  - cd
```

### Phase meta (`phase1/meta.yaml`)
```yaml
id: phase1
title: "Phase 1: Terminal Foundations"
order: 1
modules:
  - terminal-foundations
```

---

## MVP Feature List

- [ ] Homepage: shows Phase 1 card with link to module
- [ ] Lesson page: title, body (Markdown rendered), key points, next/prev links
- [ ] Exercise page: static list of steps (prompt + expected answer shown), no terminal yet
- [ ] Notes textarea on lesson page: auto-saves to localStorage per lesson
- [ ] "Mark Complete" button on lesson page: saves to localStorage
- [ ] Completed lessons show a visual indicator on the homepage/phase page

---

## Implementation Order

1. Repo scaffold: `run.py`, `config.py`, `requirements.txt`, `.gitignore`, `app/__init__.py`
2. `app/content_loader.py` — load phase/module/lesson/exercise from YAML
3. `app/routes.py` — 4 routes: `/`, `/phase/<id>`, `/lesson/<phase>/<module>/<id>`, `/exercise/<phase>/<module>/<id>`
4. `templates/base.html` — nav, footer, shared structure
5. `templates/home.html` — phase cards
6. `templates/lesson.html` — content + notes + complete button
7. `templates/exercise.html` — static step list
8. `static/css/main.css` — minimal readable styles
9. `static/js/progress.js` — localStorage helpers
10. Phase/module meta YAMLs
11. 3 lesson YAMLs (pwd, ls, cd)
12. 3 exercise YAMLs (pwd, ls, cd)
13. 7 docs files

---

## First 15 Files (in creation order)

1. `run.py`
2. `config.py`
3. `requirements.txt`
4. `.gitignore`
5. `app/__init__.py`
6. `app/routes.py`
7. `app/content_loader.py`
8. `templates/base.html`
9. `templates/home.html`
10. `templates/lesson.html`
11. `templates/exercise.html`
12. `static/css/main.css`
13. `static/js/progress.js`
14. `content/phases/phase1/meta.yaml`
15. `content/phases/phase1/terminal-foundations/meta.yaml`

Then: 3 lesson YAMLs, 3 exercise YAMLs, 7 docs.

---

## Docs to Create

| File | Purpose |
|---|---|
| `docs/roadmap.md` | Phase 1 → 2 → 3 high-level plan |
| `docs/curriculum_plan.md` | All planned modules + lesson topics |
| `docs/mvp_checklist.md` | Pass 1 checklist, tick off as you build |
| `docs/learning_journal.md` | Personal notes as you learn the material |
| `docs/content_guide.md` | How to write a new lesson/exercise (field reference) |
| `docs/stack_decisions.md` | Why Flask, why YAML, why localStorage |
| `docs/learning_loop.md` | How to use the app as a learning tool yourself |

---

## Overbuilding Risks

| Trap | Avoid by |
|---|---|
| Adding fake terminal in pass 1 | Exercise page is static steps only — terminal is pass 2 |
| Bloated YAML schema | Only the fields listed above; add fields when needed |
| CSS framework | Plain CSS only; style after it works |
| Complex content_loader | Two functions: `load_lesson()` and `load_exercise()` |
| Phase nav system | Flat links for now; one phase, one module |

---

## Verification

1. `flask run` → homepage loads with Phase 1 card
2. Click module → see 3 lesson links
3. Click pwd lesson → title, body, key points render
4. Notes textarea → type text → refresh → text persists
5. Click "Mark Complete" → refresh → shows completed state
6. Click "Next" → goes to ls lesson
7. Click Exercise link → static steps list renders
8. All 3 lessons + exercises accessible without errors
