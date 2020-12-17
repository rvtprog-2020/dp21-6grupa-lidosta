from flask import Flask, render_template, request, session, redirect, url_for
from pymongo import MongoClient
from bson.json_util import dumps


client = MongoClient("mongodb+srv://admin:admin@cluster0.gi8gq.mongodb.net/myproject?retryWrites=true&w=majority")

app = Flask(__name__)

# Datubazes
db = client.myproject


# Tabulas/Dokumenti
users_db = db.users
preces_db = db.preces

#  Datubaze bruv
user1 = {"id":"1", "vards":"Gusts","uzvards":"Stanga"}
user2 = {"id":"2", "vards":"Maikls","uzvards":"Beginskis"}

users_db.insert_one(user1)
users_db.insert_one(user2)


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

@app.route("/login", methods=["GET","POST"])
def login():
    if "name" in session and "password" in session:
        if session["name"] == "admin" and session["password"] == "admin":
            return redirect(url_for("panel"))
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        session["name"] = name
        session["password"] = password
        return redirect(url_for("panel"))
    else:
        return render_template("login.html")

app.run(host='0.0.0.0', port=80, debug=True)