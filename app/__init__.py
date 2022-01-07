import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    db.init_app(app)

    from app.auth.views import auth
    from app.main.views import main
    from app.account.views import account
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(account, url_prefix="/user")

    from app.main.errors import page_not_found
    app.register_error_handler(404, page_not_found)

    with app.app_context():
        db.create_all()

    return app

app = create_app()