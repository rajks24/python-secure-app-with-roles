from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from flask_app import db, bcrypt
from flask_app.models import User, Role  # Import Role model
from flask_app.forms import RegistrationForm, LoginForm, EditUserForm
from functools import wraps

main = Blueprint('main', __name__)

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.role.name != role:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        reader_role = Role.query.filter_by(name='reader').first()  # Assign reader role by default
        user = User(username=form.username.data, password=hashed_password, firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, role=reader_role)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.login'))
    else:
        print("Form not validated")
        print(form.errors)  # Print form errors for debugging
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/profile")
@login_required
def profile():
    return render_template('profile.html', title='Profile')

@main.route("/admin")
@login_required
@role_required('admin')
def admin_dashboard():
    return render_template('admin_dashboard.html', title='Admin Dashboard')

@main.route("/admin/users")
@login_required
@role_required('admin')
def list_users():
    users = User.query.all()
    return render_template('list_users.html', title='User List', users=users)

@main.route("/admin/users/<int:user_id>/edit", methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = EditUserForm(original_username=user.username, original_email=user.email)
    form.role.choices = [(role.id, role.name) for role in Role.query.all()]
    if form.validate_on_submit():
        user.username = form.username.data
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.email = form.email.data
        user.role = Role.query.get(form.role.data)
        if form.password.data:
            user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.commit()
        flash('User details have been updated!', 'success')
        return redirect(url_for('main.list_users'))  # Redirect to user list page
    elif request.method == 'GET':
        form.username.data = user.username
        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.email.data = user.email
        form.role.data = user.role.id
    else:
        print("Form not validated")
        print(form.errors)  # Print form errors for debugging
    return render_template('edit_user.html', title='Edit User', form=form, user=user)

@main.route("/admin/users/<int:user_id>/delete", methods=['POST'])
@login_required
@role_required('admin')
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User has been deleted!', 'success')
    return redirect(url_for('main.list_users'))  # Redirect to user list page