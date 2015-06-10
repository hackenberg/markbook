from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from markbook.config import DevelopmentConfig


app = Flask(__name__)

# config
app.config.from_object(DevelopmentConfig)

# extensions
db = SQLAlchemy(app)
manager = Manager(app)

# blueprints
if app.config["API"]:
    from markbook.blueprints import api
    app.register_blueprint(api)

# error handlers
# TODO

# views
import markbook.views
