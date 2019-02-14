from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import app
from playground import models

def create_app(config_class=Config):
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    
create_app(app.config)