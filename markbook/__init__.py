import os

from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from markbook import config


app = Flask(__name__)

# config
profile = os.getenv("MARKBOOK_SETTINGS", "DevelopmentConfig")
app.config.from_object(getattr(config, profile))

# extensions
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db, directory=app.config["SQLALCHEMY_MIGRATE_REPO"])

# blueprints
if app.config["API"]:
    from markbook.blueprints import api
    app.register_blueprint(api)

# views
import markbook.views
