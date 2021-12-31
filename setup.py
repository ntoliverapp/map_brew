# import os
from app import app, db
from app.models import User,Beer, Style
# from flask_migrate import Migrate

# app = create_app()
# migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Beer=Beer, Style=Style)
