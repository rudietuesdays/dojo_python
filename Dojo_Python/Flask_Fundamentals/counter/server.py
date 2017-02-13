from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():

    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    # try:
    #     session['counter'] += 1
    # except keyError:
    #     session['counter'] = 1

    return render_template('index.html')

@app.route('/count2', methods=['POST'])
def add_2():
    session['counter'] += 1

    return redirect ('/')

@app.route('/reset', methods=['POST'])
def reset_count():

    session.clear()
    # session['counter'] = 0
    # session.pop('counter', None)


    return redirect ('/')

app.run(debug=True) # run our server
