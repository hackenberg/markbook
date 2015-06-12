from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from markbook.config import DevelopmentConfig


app = Flask(__name__)

# config
app.config.from_object(DevelopmentConfig)

# extensions
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db, directory=app.config["SQLALCHEMY_MIGRATE_REPO"])

# blueprints
if app.config["API"]:
    from markbook.blueprints import api
    app.register_blueprint(api)

# error handlers
# TODO

# views
import markbook.views
