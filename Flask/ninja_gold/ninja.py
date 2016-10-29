from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = 'secretandrew'

@app.route('/')
def index():
    #set session['gold'] to 0
    if 'gold' not in session:
        session['gold'] = 0
        
    if 'total_gold' not in session:
        session['total_gold'] = 0
        
    #set session['activity'] to []
    if 'activity' not in session:
        session['activity'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    #create a dictionary! key/values are the buildings and their gold ranges!
    place = {'farm': (10,20), 'cave': (5,10), 'house': (2,5), 'casino': (-50,50)}
    session['gold'] = random.randint(place[request.form['building']][0], place[request.form['building']][1])
    
    if session['gold'] >= 0:
        session['activity'].append (" Earned " + str(session['gold']) + " golds from the " + request.form['building'] + "! " + str(datetime.datetime.now()))
    else:
        session['activity'].append (" Entered a casino and lost " + str(session['gold']) + " golds... Ouch. " + str(datetime.datetime.now()))
    session['total_gold'] = session['total_gold'] + session['gold']
    return redirect('/')

app.run(debug=True)