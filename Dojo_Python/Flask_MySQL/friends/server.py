from flask import Flask, render_template, redirect, request
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template("index.html", users=users)

@app.route('/create', methods=['POST'])
def create_user():
    query = "INSERT INTO users (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
    }
    # an example of running a query
    # print mysql.query_db("SELECT * FROM users")
    print data
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<user_id>')
def destroy(user_id):
    query = "DELETE FROM users where id=:id"
    data = {'id':id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
