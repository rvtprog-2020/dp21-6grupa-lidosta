<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 892ed2177138a57f7425effd1a6a327206c32115
>>>>>>> a87405ecb8307540b567b6b11a4db693775aed0b
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('Home_page.html')

@app.route('/lidostas')
def lidostas():
    return render_template('Lidostas.html')

@app.route('/lidmasinas')
def lidmasinas():
    return render_template('Lidmasinas.html')

@app.route('/reisi')
def reisi():
    return render_template('Reisi.html')

app.run(host='0.0.0.0', port=80, debug=True)
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
=======
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Home_page.html')

@app.route('/lidmasinas')
def contacts():
    return render_template('Lidmasinas.html')

@app.route('/lidostas')
def aboutUs():
    return render_template('Lidostas.html')

@app.route('/reis')
def help():
    return render_template('Reisi.html')


app.run(host='0.0.0.0', port='80', debug = True)
>>>>>>> 17f4842beeef419e2898a08af3f49f0c25b59936
>>>>>>> 892ed2177138a57f7425effd1a6a327206c32115
>>>>>>> a87405ecb8307540b567b6b11a4db693775aed0b