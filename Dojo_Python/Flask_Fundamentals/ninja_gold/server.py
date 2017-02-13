import random, datetime
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'OnlyANinjaCouldFigureThisOut'

@app.route('/')
def index():

    if 'gold' in session:
        print session['gold']
    else:
        session['gold'] = 0
        print session['gold']

    if 'log' in session:
        print session['log']
    else:
        session['log'] = {}
        print session['log']

    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def get_coins():
    new_gold = 0
    if request.form['building'] == 'farm':
        farm_gold = random.randrange(10, 21)
        session['gold'] += farm_gold
        print 'random # is:', farm_gold, 'gold total is:', session['gold']
        new_gold = farm_gold
    elif request.form['building'] == 'cave':
        cave_gold = random.randrange(5, 11)
        session['gold'] += cave_gold
        print 'from the cave:', cave_gold, 'total:', session['gold']
        new_gold = cave_gold
    elif request.form['building'] == 'house':
        house_gold = random.randrange(2, 6)
        session['gold'] += house_gold
        print 'from the house:', house_gold, 'total:', session['gold']
        new_gold = house_gold
    elif request.form['building'] == 'casino':
        win_lose = round(random.random())
        if win_lose == 0:
            casino_gold = random.randrange(10, 51)
            session['gold'] += casino_gold
            print 'win =', win_lose, 'casino wins:', casino_gold, 'total:', session['gold']
            new_gold = casino_gold
        else:
            casino_gold = random.randrange(-50, -9)
            session['gold'] += casino_gold
            print 'lose =', win_lose, 'casino loses', casino_gold, 'total:', session['gold']
            new_gold = casino_gold

    session['log'] = {
        'created_at': datetime.datetime.now(),
        'new_gold': new_gold,
        'location': request.form['building'],
    }



    # session['log'].update('new_gold')
    # print activity_log

    return redirect ('/')

@app.route('/replay', methods=['POST'])
def new_game():
    session.clear()
    return redirect('/')

app.run(debug=True)
