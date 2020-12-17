from flask import Flask, render_template, request, session, redirect, url_for
from pymongo import MongoClient
from bson.json_util import dumps
from random import randint


client = MongoClient("mongodb+srv://KileCodora:06907328D@cluster0.jzqkx.mongodb.net/myproject?retryWrites=true&w=majority")
app = Flask(__name__)

app.secret_key = "hkIbg#45f1"

db = client.users
users_db = db.users

db = client.data
data_db = db.data


@app.route('/home', methods=["GET","POST"])
def home():
    if "auth" in session:
        return render_template("Home_page.html")
    else:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            a = users_db.find_one({"email":email})
            b = users_db.find_one({"email":email},{"password":password})

            if a != None or b != None:
                a = a['email']
                b = b['password']

            if a != email or b != password:
                return redirect(url_for("home"))

            session["auth"] = email

            return redirect(url_for("home"))

        else:
            return render_template("Home_page.html")
@app.route('/lidostas', methods=["GET","POST"])
def lidostas():
    return render_template('Lidostas.html')

@app.route('/lidmasinas', methods=["GET","POST"])
def lidmasinas():
    return render_template('Lidmasinas.html')

@app.route('/reisi', methods=["GET","POST"])
def reisi():
    return render_template('Reisi.html')

@app.route('/admin', methods=["GET","POST"])
def admin():
    return render_template('admin.html')

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.pop("auth", None)
    return redirect(url_for("home"))

@app.route('/registration', methods=["GET","POST"])
def registration():
    if "auth" in session:
        return redirect(url_for("home"))
    else:
        if request.method == 'POST':

            id_ = randint(100,9999999)
            email = request.form['email']
            password = request.form['password']

            a = users_db.find_one({"email":email})
            if a != None:
                a = a['email']

            if a == email:
                return redirect(url_for("home"))

            session["auth"] = email

            users_db.insert_one({"id":id_,"email":email,"password":password})
            return redirect(url_for("home"))
        else:
            return render_template("registration.html")

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