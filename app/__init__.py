from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')
    db.init_app(app)

    with app.app_context():
         db.create_all()

    migrate.init_app(app, db)

    from app.routes import rest_api
    CORS(rest_api, resources={r"/api/v1/*": {"origins": "*"}})
    app.register_blueprint(rest_api, url_prefix='/api/v1')

    return app
