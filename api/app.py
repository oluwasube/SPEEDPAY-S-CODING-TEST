from flask import Flask
from config.config import config_names
from utils.db import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import user
from v1.views.auth import auth_bp
from v1.views.transactions import transactions


def create(config=config_names['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(auth_bp, url_prefix="/api/v1")
    app.register_blueprint(transactions, url_prefix="/api/v1")
    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    @app.shell_context_processor
    def shell_context():
        return {
            "db": db,
            "user": user

        }

    return app


app = create()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
