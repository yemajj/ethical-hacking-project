from flask import Blueprint, render_template, abort
from app.content_loader import load_phases, load_lesson, load_exercise

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    phases = load_phases()
    return render_template('home.html', phases=phases)


@bp.route('/lesson/<phase_id>/<module_id>/<lesson_id>')
def lesson(phase_id, module_id, lesson_id):
    try:
        data = load_lesson(phase_id, module_id, lesson_id)
    except FileNotFoundError:
        abort(404)
    return render_template('lesson.html', lesson=data,
                           phase_id=phase_id, module_id=module_id)


@bp.route('/exercise/<phase_id>/<module_id>/<exercise_id>')
def exercise(phase_id, module_id, exercise_id):
    try:
        data = load_exercise(phase_id, module_id, exercise_id)
    except FileNotFoundError:
        abort(404)
    return render_template('exercise.html', exercise=data,
                           phase_id=phase_id, module_id=module_id)
