# Content Guide

How to add a new lesson and exercise.

## Adding a lesson

Create a file at `content/phases/<phase_id>/<module_id>/lessons/<lesson_id>.yaml`.

Then add it to `<module_id>/meta.yaml` under `lessons`.

### Lesson fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Matches filename, used in URLs |
| `title` | yes | Display title |
| `order` | yes | Sort order within module |
| `description` | yes | One-line subtitle shown on lesson page |
| `body` | yes | Markdown content |
| `key_points` | yes | List of bullet points |
| `prev_lesson` | no | id of previous lesson (null if first) |
| `next_lesson` | no | id of next lesson (null if last) |

## Adding an exercise

Create a file at `content/phases/<phase_id>/<module_id>/exercises/<lesson_id>_exercise.yaml`.

### Exercise fields

| Field | Required | Description |
|---|---|---|
| `id` | yes | Must be `<lesson_id>_exercise` |
| `lesson_id` | yes | The lesson this exercise belongs to |
| `title` | yes | Display title |
| `steps` | yes | List of step objects |

### Step fields

| Field | Required | Description |
|---|---|---|
| `prompt` | yes | The scenario/question shown to the user |
| `expected` | yes | The correct command |
| `output` | yes | Expected terminal output (can be empty string) |
| `explanation` | no | Optional note shown after the step |

## Linking exercise from lesson

The lesson template automatically links to `<lesson_id>_exercise`. No extra config needed.
