from flask_app import create_app, db, bcrypt
from flask_app.models import User, Role

app = create_app()
with app.app_context():
    admin_role = Role.query.filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin')
        db.session.add(admin_role)
        db.session.commit()
    
    hashed_password = bcrypt.generate_password_hash('adminpassword').decode('utf-8')
    admin_user = User(username='admin', password=hashed_password, firstname='Admin', lastname='User', email='admin@example.com', role=admin_role)
    db.session.add(admin_user)
    db.session.commit()
