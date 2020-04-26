from flask import *
import pyrebase
import ast 
from getpass import getpass
import json
import time

from accountHandling import createAccount, loginAccount
from posting import *

with open("db_creds.json") as f:
	firebaseConfig = json.load(f)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

app = Flask(__name__)

@app.route("/")
def index():
	uids = [i.val()["uid"] for i in db.child("users").get().each()]
	if request.cookies.get('uid') in uids:
		uid = request.cookies.get('uid')
		data = db.child("users").child(uid).get()
		bio = data.val()["bio"]
		name = data.val()["firstname"] + " " + data.val()["lastname"]
		avatar = "/static/avatar.png"
		return render_template("/landingpage.html", bio=bio, name=name, avatar=avatar)
	else:
		print(0)
		return render_template("/index.html")
	return ""

@app.route("/register")
def register():
	return render_template("/register.html")

@app.route('/api/register', methods=["POST"])
def actionRegister():
	data = request.form
	email = data["email"]
	password = data["password"]
	firstName = data["firstName"]
	lastName = data["lastName"]
	bio = data["bio"]
	skills= data["skills"]
	print(skills[:-1])
	skills = skills[:-1].split(",")
	print(skills)
	createAccount(db, auth, email, password, firstName, lastName, bio, skills)
	return "penis"

@app.route("/login")
def login():
	return render_template("/login.html")

def setCookie(key, value):
	resp = make_response("Setting cookie")
	resp.set_cookie(key, value)
	return resp

@app.route("/api/login", methods=["POST"])
def actionLogin():
	data = request.form
	email = data["email"]
	password = data["password"]
	uid = loginAccount(db, auth, email, password)

	resp = make_response(redirect("/"))
	resp.set_cookie("uid", uid)
	return resp

@app.route("/api/createPost", methods=["POST"])
def actionPost():
	data = request.form
	uid = request.cookies.get("uid")
	title = data["title"]
	desc = data["description"]
	img = data["image"]
	loc = data["location"]
	ts = int(time.time())
	return createPost(db, uid, title, desc, img, loc, ts)

@app.route("/api/deletePost", methods=["POST"])
def actionDelete():
	data = request.form
	uid = request.cookies.get("uid")
	postid = data["postid"]
	if(not deletePost(db, uid, postid)):
		return "fail"
	return "success"

@app.route("/api/likePost", methods=["POST"])
def actionLike():
	data = request.form
	uid = request.cookies.get("uid")
	postid = data["postid"]
	if(not likePost(db, uid, postid)):
		return "fail"
	return "success"

@app.route("/api/attendPost", methods=["POST"])
def actionAttend():
	data = request.form
	uid = request.cookies.get("uid")
	postid = data["postid"]
	if(not confirmAttendance(db, uid, postid)):
		return "fail"
	return "success"

@app.route("/api/followingPosts", methods=["GET"])
def getFollowingPosts():
	data = request.form
	uid = request.cookies.get("uid")
	ans = fetchFollowingPost(db, uid)
	return json.dumps(ans)

@app.route("/logout")
def logout():
	resp = make_response(redirect("/"))
	resp.set_cookie('uid', '', expires=0)
	return resp

@app.route("/get")
def getcookie():
	return ""

@app.route("/map", methods=["GET"])
def maps():
	return render_template("/map.html")


app.run()