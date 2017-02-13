from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_info():
    if len(request.form['first_name'])>=1 and len(request.form['last_name'])>=1:
        if request.form['first_name'].isalpha() != True or request.form['last_name'].isalpha() != True:
            flash("Name cannot contain numbers!", 'error_name_alpha')
    else:
        flash("Name cannot be blank!", 'error_name_length')
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!", 'error_email')
    else:
        if not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
    if len(request.form['password']) < 1 or len(request.form['confirm_password']) < 1:
        flash("Password cannot be blank!")
    elif len(request.form['password']) < 8:
        flash("Password must contain more than 8 characters!")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password fields must match!")
    elif not re.match(r'[A-Za-z0-9]', request.form['password']):
            flash("Password must contain at least one uppercase letter AND at least one number!")
    else:
        flash("Thanks for submitting your information!")

    return redirect('/')



app.run(debug=True)
