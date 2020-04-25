from flask import Flask, render_template, request, jsonify

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
    username = data["username"]
    password = data["password"]