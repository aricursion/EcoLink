from flask import Flask, render_template, request, jsonify
import pyrebase

from getpass import getpass
import json

from login import createAccount

with open("db_creds.json") as f:
	firebaseConfig = json.load(f)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/login")
def login():
    return render_template("/login.html")

@app.route('/api/login', methods=["POST"])
def actionLogin():
    data = request.form
    email = data["email"]
    password = data["password"]
    createAccount(db, auth, email, password, "first", "last", "bio", ["NA"])
    return "penis"

app.run()