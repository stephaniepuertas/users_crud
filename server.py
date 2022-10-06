from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key= '23498dwjwurdenwue3i35748393i1lkkdSDKJRIWEICJ20rdjsdjn2ieuurd'

@app.route('/')
def index():
    return render_template('create.html')

@app.post('/process')
def insert_info():
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['email']= request.form['email']
    # return takes in a route only
    return redirect('/process')


@app.get('/process')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)