# first, import Flask to allow us to create our app.
from flask import Flask, render_template #can also import 'redirect' and redirect to a file
app = Flask(__name__) # Global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

@app.route('/') # The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
def hello():
    return render_template('index.html', name="Rae") #if using 'redirect', would replace 'render' with 'redirect' here

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True) # Run the app in debug mode.
