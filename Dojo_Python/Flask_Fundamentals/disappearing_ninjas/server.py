from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas/')
def show_ninjas():

    print 'no ninja'

    return render_template("ninjas.html", no_ninja=True)


@app.route('/ninjas/<ninja>')
def show_user_profile(ninja):
    # try:
    #     ninja
    #     print ninja
    #     no_ninja = False
    # except NameError:
    #     print 'no ninja'
    #     ninja = None

    # if ninja == undefined:
    print ninja

    return render_template("ninjas.html", ninja=ninja)


app.run(debug=True)
