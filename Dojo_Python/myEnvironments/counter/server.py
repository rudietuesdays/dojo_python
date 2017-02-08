from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():

    try:
        session['counter'] += 1
    except keyError:
        session['counter'] = 1

    return render_template('index.html')

@app.route('/count2', methods=['POST'])
def add_2():
    try:
        session['counter'] += 1
    except keyError:
        session['counter'] = 2
    return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset_count():
    try:
        session['counter'] = 0
    except keyError:
        session['counter'] = 0
    return redirect ('/')

app.run(debug=True) # run our server
