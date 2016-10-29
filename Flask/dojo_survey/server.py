from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="secretandrew"

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    name = request.form['name']
    locations = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    
    if len(request.form['name']) < 1:
        flash("Please enter name inside box!")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Please enter comments inside box!")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Please keep comments no more than 120 characters!")
        return redirect('/')
    else:
        flash("Thank you!")
        
    return render_template('result.html', name=name, location=locations, language=language, comment=comment)
    return redirect('/result')

app.run(debug=True)