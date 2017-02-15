from flask import Flask, request, redirect, render_template, session, flash

from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "SuchASecretKeyOhEmGee!"
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():

    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/process', methods=['GET', 'POST'])
def process_email():
    # flag = False # Err status is false
    if not EMAIL_REGEX.match(request.form['email']):
        # flag = True
        flash("Invalid Email Address!", 'error')
    else:
        # flag = True
        flash("The email address you entered {} is a VALID email address. Thank you!".format(request.form['email']), 'success')

        query = """INSERT INTO users (email, created_at, updated_at)
            VALUES (:email, NOW(), NOW())"""
    # We'll then create a dictionary of data from the POST data received.
        data = {
            'email': request.form['email'],
            }
    # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)

    return redirect('/')

@app.route('/remove_user', methods=['POST'])
def delete():
    print request.form['user_to_delete']
    print "*"*10
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': request.form['user_to_delete']}
    mysql.query_db(query, data)


    return redirect('/')

app.run(debug=True)
