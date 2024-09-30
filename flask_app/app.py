# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes after initializing the app and database
from routes import *

# Create the database tables only once, when the app starts
with app.app_context():
    from models import User  # Import User here to avoid circular import
    db.create_all()  # Create tables if they don't exist

if __name__ == '__main__':
    app.run(debug=True)
