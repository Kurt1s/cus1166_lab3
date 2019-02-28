from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import models, app

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

def create_app(config_class = Config):
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app,db)
create_app(app.config)