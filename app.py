import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# Allow insecure HTTP for OAuth (if you need it later)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)  # Secret key for sessions

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Home route
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('tiers'))  # Redirect to tiers page
    else:
        return redirect(url_for('login'))

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Check if the email is already in use
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please login.', 'error')
            return redirect(url_for('signup'))

        # Create a new user
        new_user = User(email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()

        flash('Signup successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the email exists
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Create session
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('tiers'))  # Redirect to tiers page after successful login
        else:
            flash('Invalid email or password.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

# Tiers page route
@app.route('/tiers')
def tiers():
    if 'user_id' not in session:
        flash('You need to log in first.', 'error')
        return redirect(url_for('login'))
    return render_template('tiers.html')  # This will render your tiers page

# Microsoft page route
@app.route('/microsoft')
def microsoft():
    return render_template('microsoft.html')

# Google page route
@app.route('/google')
def google():
    return render_template('google.html')

# Amazon page route
@app.route('/amazon')
def amazon():
    return render_template('amazon.html')

# Apple page route
@app.route('/apple')
def apple():
    return render_template('apple.html')

# Meta page route
@app.route('/meta')
def meta():
    return render_template('meta.html')

# Netflix page route
@app.route('/netflix')
def netflix():
    return render_template('netflix.html')

# Uber page route
@app.route('/uber')
def uber():
    return render_template('uber.html')

# Adobe page route
@app.route('/adobe')
def adobe():
    return render_template('adobe.html')

# Salesforce page route
@app.route('/salesforce')
def salesforce():
    return render_template('salesforce.html')

# Spotify page route
@app.route('/spotify')
def spotify():
    return render_template('spotify.html')

# Airbnb page route
@app.route('/airbnb')
def airbnb():
    return render_template('airbnb.html')

# X page route
@app.route('/x')
def x():
    return render_template('x.html')

# Mindtree page route
@app.route('/mindtree')
def mindtree():
    return render_template('mindtree.html')

# Infosys page route
@app.route('/infosys')
def infosys():
    return render_template('infosys.html')

# Wipro page route
@app.route('/wipro')
def wipro():
    return render_template('wipro.html')

# TCS page route
@app.route('/tcs')
def tcs():
    return render_template('tcs.html')

# Cognizant page route
@app.route('/cognizant')
def cognizant():
    return render_template('cognizant.html')

# Capgemini page route
@app.route('/Ccapgemini')
def capgemini():
    return render_template('capgemini.html')

# Initialize the database (only run once to create the tables)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)