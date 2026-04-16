import os
import yaml
from flask import current_app


def _phases_dir():
    return current_app.config['CONTENT_DIR']


def load_phases():
    phases = []
    base = _phases_dir()
    for phase_id in sorted(os.listdir(base)):
        meta_path = os.path.join(base, phase_id, 'meta.yaml')
        if not os.path.isfile(meta_path):
            continue
        with open(meta_path, encoding='utf-8') as f:
            phase = yaml.safe_load(f)
        phase['modules_data'] = []
        for mod_id in phase.get('modules', []):
            mod_path = os.path.join(base, phase_id, mod_id, 'meta.yaml')
            if os.path.isfile(mod_path):
                with open(mod_path, encoding='utf-8') as f:
                    phase['modules_data'].append(yaml.safe_load(f))
        phases.append(phase)
    return phases


def load_lesson(phase_id, module_id, lesson_id):
    path = os.path.join(_phases_dir(), phase_id, module_id, 'lessons', f'{lesson_id}.yaml')
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_exercise(phase_id, module_id, exercise_id):
    path = os.path.join(_phases_dir(), phase_id, module_id, 'exercises', f'{exercise_id}.yaml')
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)
