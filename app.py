from flask_app import create_app
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
