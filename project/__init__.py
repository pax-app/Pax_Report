import os
from flask import Flask, jsonify
from project.api.views import reports_blueprint
from database import db, migrate


# instantiate the app
def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set Configuration
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(reports_blueprint)

    return app
