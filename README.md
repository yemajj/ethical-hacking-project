# Ethical Hacking Project

This repository contains a beginner-focused cybersecurity learning project centered on a small Flask app called `cyber-edu`.

## What's in this repo

- `cyber-edu/`: the Flask web app
- `cyber-edu/content/`: YAML lesson and exercise content
- `cyber-edu/docs/`: planning and curriculum documents
- `PLAN.md`: higher-level MVP plan for the project

## Current focus

The current MVP is a "Terminal Foundations" learning experience for beginners, covering:

- `pwd`
- `ls`
- `cd`

The app is designed to render lessons from YAML content, show exercises, and track notes and progress locally in the browser.

## Tech stack

- Python
- Flask
- Jinja2 templates
- YAML content files
- Plain CSS and JavaScript

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r cyber-edu/requirements.txt
```

3. Start the app:

```bash
python cyber-edu/run.py
```

4. Open the local Flask URL shown in the terminal.

## Project goal

The broader goal is to build a beginner-friendly cybersecurity education platform that is useful both as a personal learning project and as a shareable teaching tool.
