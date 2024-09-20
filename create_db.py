from flask_app import create_app, db
from flask_app.models import User, Role

app = create_app()
with app.app_context():
    db.create_all()
