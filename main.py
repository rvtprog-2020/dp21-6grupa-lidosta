from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient("mongodb+srv://admin:<admin>@cluster0.gi8gq.mongodb.net/<lidostaBRUV>?retryWrites=true&w=majority")

app = Flask(__name__)

#  Datubaze bruv
db=client.lidostaBRUV



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

@app.route('/admin')
def admin():
    return render_template('admin.html')

app.run(host='0.0.0.0', port=80, debug=True)