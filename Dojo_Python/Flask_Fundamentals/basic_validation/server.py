from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/process', methods=['Post'])
def process():
    #do some validations here!
    if len(request.form['name']) < 1:
        # display validation errors
        flash("Name cannot be empty!")
    else:
        # display success message
        flash("Success! Your name is {}".format(request.form['name'])) # pass a string to the flash function

    # either way the application should return to the index and display the message
    return redirect('/')
app.run(debug=True)
