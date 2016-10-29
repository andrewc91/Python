from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretandrew'

@app.route('/')
def randomInt():
    if 'random' not in session:
        session['random'] = random.randrange(0, 101)
    if 'guess' not in session:
        session['guess'] = 0
    return render_template("index.html")

@app.route('/guesses', methods=['POST'])
def guesses():
    if request.form['number']:
        session['guess'] = int(request.form['number'])
    return redirect('/')

@app.route('/again')
def again():
    session.clear()
    return redirect('/')

app.run(debug=True)