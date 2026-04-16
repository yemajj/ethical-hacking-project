# Project Context

## Project Name
Beginner-Friendly Cybersecurity Learning App

## Core Goal
Build a beginner-friendly web app that teaches cybersecurity fundamentals through safe, interactive lessons and exercises.

This project has two equal goals:
1. Help me learn the material myself in a hands-on way
2. Create a useful tool for other beginners to use

## Product Framing
This is an educational platform only.

It should focus on:
- safe learning
- beginner-friendly explanations
- guided exercises
- sandbox/legal practice
- strong fundamentals

It should NOT become:
- a real-world attack tool
- an exploit launcher
- a recon toolkit for public targets
- anything built for unauthorized access or misuse

## Learning + Building Philosophy
For each topic, follow this loop:
1. Learn it myself
2. Practice it myself
3. Note what was confusing
4. Turn that into a lesson/exercise
5. Improve the app based on real learning friction

The app should be built from real understanding, not from shallow generated content.

## Current Phase
Phase 1: Terminal Foundations

## Initial Lesson Scope
Start very small with:
- `pwd`
- `ls`
- `cd`

## Initial Exercise Scope
Beginner exercises only, such as:
- find your current directory
- list files in a folder
- move into a folder and back out

## MVP Goal
Build a very small, usable MVP that includes:
- homepage
- phase/module navigation
- lesson page template
- exercise page template
- notes area
- simple progress tracking
- clean docs folder
- easy-to-expand structure

## Constraints
Keep the project:
- simple
- modular
- readable
- beginner-friendly
- fast to iterate on

Do NOT add:
- auth
- payments
- multi-user systems
- dashboards
- overengineered abstractions
- unnecessary dependencies
- advanced infrastructure

## Preferred Tech Direction
Current stack:
- Flask
- HTML/CSS/JS
- localStorage (progress tracking and notes — no server-side DB for this MVP)

SQLite is a possible Phase 4 addition for multi-device sync. Do not introduce it before then.

## Build Philosophy
Use vertical slices.
Do not build a giant framework first.

Preferred order:
1. repo structure
2. docs
3. homepage
4. lesson template
5. exercise template
6. notes area
7. progress tracking
8. starter content for `pwd`, `ls`, `cd`

## Docs To Keep In Repo
Create and maintain:
- `docs/roadmap.md`
- `docs/curriculum_plan.md`
- `docs/mvp_checklist.md`
- `docs/learning_journal.md`

These repo docs should be the main source of truth so AI coding tools can read them directly.

## Audience
Primary audience:
- me while learning
- beginners who are just behind me in knowledge

Build for clarity, not for experts.

## Content Style
Lessons should include:
- what the concept is
- why it matters
- example command or example
- expected output or behavior
- beginner mistakes
- small practice task

Exercises should be:
- safe
- simple
- guided
- realistic for beginners
- easy to expand later

## Immediate Next Step
Scaffold the initial MVP for Phase 1 with:
- basic project structure
- starter docs
- homepage
- lesson page template
- exercise page template
- notes area
- simple progress tracking
- starter content for `pwd`, `ls`, and `cd`

## Instructions For AI Coding Assistant
When helping with this project:
- keep scope tight
- avoid overbuilding
- prioritize readability
- use sensible naming
- keep the app easy to extend
- treat this as an educational platform only
- do not introduce real-world attack functionality
- explain proposed changes clearly
- suggest the next smallest logical step after each coding task
