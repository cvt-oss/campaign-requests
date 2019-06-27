import os
import connexion
from .models import init_app as models_init_app

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    connex_app = connexion.FlaskApp(__name__, specification_dir=basedir)
    app = connex_app.app
    app.config.from_object('config.DevelopmentConfig')
    connex_app.add_api("swagger.yml")

    models_init_app(app)
    return connex_app
