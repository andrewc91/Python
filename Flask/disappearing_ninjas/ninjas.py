from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = "secretandrew"

turtles = {
    'blue':'leonardo.jpg','orange':'michelangelo.jpg','red':'raphael.jpg','purple':'donatello.jpg'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    return render_template('ninjas.html', ninja_color='everyone')

@app.route('/ninja/<ninja_color>')
def disappear_ninja(ninja_color):
    colors = ['blue', 'red', 'purple', 'orange', 'none']
    for color in colors:
        if color == ninja_color:
            return render_template('ninjas.html', ninja_color=ninja_color)

app.run(debug=True)