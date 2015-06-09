from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from markbook.config import DevelopmentConfig


app = Flask(__name__)

# config
app.config.from_object(DevelopmentConfig)

# extensions
db = SQLAlchemy(app)

# blueprints
from markbook.blueprints import api
app.register_blueprint(api)

# error handlers
# TODO

# views
import markbook.views
