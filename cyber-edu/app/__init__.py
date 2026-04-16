import markdown as md
from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)

    app.jinja_env.filters['markdown'] = lambda text: md.markdown(text, extensions=['fenced_code'])

    from app.routes import bp
    app.register_blueprint(bp)

    return app
