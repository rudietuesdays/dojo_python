from flask import Flask, render_template, request, redirect
app = Flask(__name__)
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
   print "Got Post Info"
   # recall the name attributes we added to our form inputs
   # we use request.form['name_of_input'] to access the data that the user input into the fields
   info = {
        'name': request.form['name'],
        'location': request.form['location'],
        'language': request.form['language'],
        'comment': request.form['comment'],
   }
   # redirects back to the '/' route
   return render_template("result.html", info = info)
   # return redirect('/result')  **BEST PRACTICE: always redirect after handling POST data to avoid handling it more than once!

@app.route('/show')
def show_user():
    return render_template('user.html', name='Jay', email='kpatel@codingdojo.com')

app.run(debug=True) # run our server
