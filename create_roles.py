from flask_app import create_app, db
from flask_app.models import Role

app = create_app()
with app.app_context():
    if not Role.query.filter_by(name='admin').first():
        admin_role = Role(name='admin')
        db.session.add(admin_role)
    if not Role.query.filter_by(name='reader').first():
        reader_role = Role(name='reader')
        db.session.add(reader_role)
    db.session.commit()
