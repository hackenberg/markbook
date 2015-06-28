import os

from flask import Flask
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

# blueprints
if app.config["API"]:
    from markbook.blueprints import api
    app.register_blueprint(api)

# views
import markbook.views
