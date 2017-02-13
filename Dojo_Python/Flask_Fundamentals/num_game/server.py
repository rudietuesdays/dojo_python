import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessThis'

@app.route('/')
def index():
    if 'results' in session:
        print session['results']
    else:
        session['results'] = {}

    if 'secretNum' in session:
        print session['secretNum']
    else:
        session['secretNum'] = random.randrange(1, 101)
        print session['secretNum']


    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_num():
    guessNum =  int(request.form['guess'])
    print session['secretNum']
    print guessNum

    if guessNum == session['secretNum']:
        result = "correct"
        color = 'green'
    elif guessNum > session['secretNum']:
        result = "high"
        color = 'red'
    elif guessNum < session['secretNum']:
        result = "low"
        color = 'red'

    session['results'] = {
        'guessNum': guessNum,
        'result': result,
        'color': color,
    }

    print type(session['results']['result'])

    return redirect('/')

@app.route('/replay', methods=['POST'])
def new_game():
    session.clear()
    return redirect('/')

app.run(debug=True)
