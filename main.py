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