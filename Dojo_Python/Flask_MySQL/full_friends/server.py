from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime
now = datetime.now()
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "SuchASecretKeyOhEmGee!"
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create_user():
    # Write query as a string. Notice how we have multiple values we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"

    # We'll then create a dictionary of data from the POST data received.
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
    }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route("/friends/<id>/edit", methods=['POST'])
def edit_user(id):
    user_id = id
    print '*'*10
    print user_id
    print '*'*10
    query = "SELECT * FROM friends WHERE id = {}".format(user_id)
    friend = mysql.query_db(query)
    # mysql.query_db(query, friend)

    return render_template("edit_user.html", all_friends=friend)

@app.route("/friends/<id>", methods=['POST'])
def edit_submit(id):
    user_id = id
    print '*'*10
    print user_id
    print '*'*10
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = NOW() WHERE id = {}".format(user_id)
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation'],
    }
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/friends/<id>/delete', methods=['POST'])
def delete_user(id):
    user_id = id
    print user_id
    print "*"*10
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)


    return redirect('/')


app.run(debug=True)
