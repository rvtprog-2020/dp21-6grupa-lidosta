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