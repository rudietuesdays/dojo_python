from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'SuchASecretKeyWahHaHa'

# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# the server is listening for a POST request to: localhost:5000/result
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        # display validation errors
        flash("Name cannot be empty!")
        return redirect ('/')
    if len(request.form['comment']) < 1:
        flash("Comments field cannot be blank!")
        return redirect ('/')
    elif len(request.form['comment']) > 120:
        flash("Wow, you've sure got a lot to say! Please keep your message to under 120 characters.")
        return redirect ('/')
    else:
        print "Got Post Info"

        info = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment'],
        }

        return render_template("result.html", info = info)
    # recall the name attributes we added to our form inputs
    # we use request.form['name_of_input'] to access the data that the user input into the fields

    # redirects back to the '/' route

    # return redirect('/result')  **BEST PRACTICE: always redirect after handling POST data to avoid handling it more than once!

@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True) # run our server
