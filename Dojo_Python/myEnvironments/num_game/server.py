import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessThis'

secretNum = random.randrange(0, 101)

@app.route('/')
def index():
    print secretNum
    return render_template('index.html')

app.run(debug=True)
