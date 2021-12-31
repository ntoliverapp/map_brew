import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
# from extensions import db
db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)

#     app.config.from_mapping(
#     SECRET_KEY=os.getenv("SECRET_KEY"), 
#     SQLALCHEMY_DATABASE_URI='postgresql://ncfuovrqzottdj:681913a04ef70f0ceaed4b0933a3ab9e4ba355310f115512ba175f6ba169af3f@ec2-44-198-24-0.compute-1.amazonaws.com:5432/dfpbsev5j06u17',
#     SQLALCHEMY_TRACK_MODIFICATIONS=False,
#     DEBUG=True
# )

#     db.init_app(app)

#     from app.auth.views import auth
#     from app.main.views import main
#     from app.account.views import account
#     app.register_blueprint(auth)
#     app.register_blueprint(main)
#     app.register_blueprint(account, url_prefix="/user")

#     from app.main.errors import page_not_found
#     app.register_error_handler(404, page_not_found)

#     return app

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