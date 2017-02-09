import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessThis'

@app.route('/')
def index():
    secretNum = random.randrange(1, 101)
    if secretNum in session:
        print session['secretNum']
    else:
        secretNum = session['secretNum']
        print session['secretNum']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess_num():
    guessNum =  int(request.form['guess'])
    print session['secretNum']
    print guessNum
    if (guessNum == session['secretNum']):
        result = "correct"
    elif (guessNum > session['secretNum']):
        result = "high"
    elif (guessNum < session['secretNum']):
        result = "low"
    return render_template('index.html',result=result, guessNum=guessNum)

@app.route('/replay', methods=['POST'])
def new_game():
    replay = 'Play again?'
    session.clear()
    return render_template('index.html', replay=replay)

app.run(debug=True)
