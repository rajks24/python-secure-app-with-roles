# Python Secure App with Roles

## Description
Python Secure App is a web application built using Flask, SQLAlchemy, and Flask-Login. It provides user authentication and role-based access control using AWS Cognito. The app allows users to register, log in, and access different routes based on their roles (admin or reader). Admin users can view, edit, and delete user details.

This project can be used as a boilerplate for building secure web applications with user authentication and role-based access control.

## Configuration

### Prerequisites
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/python-secure-app.git
    cd python-secure-app
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add the following variables:
    ```env
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///site.db
    ```

5. **Initialize the database:**
    ```bash
    python create_db.py
    python create_roles.py
    ```

6. **Create an admin user:**
    ```bash
    python create_admin.py
    ```

## Running the App

1. **Run the Flask app:**
    ```bash
    python app.py
    ```

2. **Access the app in your browser:**
    Open your browser and go to `http://127.0.0.1:5000`

## Routes and Their Purpose

- **`/` or `/home`**: Home page accessible to all users.
- **`/register`**: Registration page for new users.
- **`/login`**: Login page for existing users.
- **`/logout`**: Logout route to log out the current user.
- **`/profile`**: Profile page accessible to logged-in users.
- **`/admin`**: Admin dashboard accessible only to admin users.
- **`/admin/users`**: List of all users accessible only to admin users.
- **`/admin/users/<int:user_id>/edit`**: Edit user details accessible only to admin users.
- **`/admin/users/<int:user_id>/delete`**: Delete user accessible only to admin users.

## Additional Information

- **Role-Based Access Control**: The app uses role-based access control to restrict access to certain routes based on the user's role (`admin` or `reader`).
- **Password Hashing**: User passwords are hashed using `bcrypt` for security.
- **CSRF Protection**: The app uses `Flask-WTF` for form handling and CSRF protection.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please contact connect@rajeshscribe.com.
