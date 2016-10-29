from flask import Flask, render_template, request, redirect, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NUMBER_REGEX = re.compile(r'^[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = "secretandrew"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['first']) < 1:
        flash("First name cannot be blank. Try again.")
    elif not NUMBER_REGEX.match(request.form['first']):
        flash("First name must contain only text. Try again.")
        
    if len(request.form['last']) < 1:
        flash("Last name cannot be blank. Try again.")
    elif not NUMBER_REGEX.match(request.form['last']):
        flash("Last name must contain only text. Try again.") 
    
    if len(request.form['first']) < 1 and len(request.form['last']) < 1:
        flash("First and last name cannot be blank. Try again.")
    elif not NUMBER_REGEX.match(request.form['first']) and NUMBER_REGEX.match(request.form['last']):
        flash("First and last name must contain only text. Try again.")
        
    if len(request.form['password']) < 8:
        flash("Password must contain more than 8 characters. Try again.")
    
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid E-mail. Try again.")
    
    if (request.form['password']) != (request.form['confirm']):
        flash("Passwords must match. Try again.")
    
    else:
        flash("Submission was successful!")
    
    return redirect('/')
app.run(debug=True)