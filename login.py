import pyrebase

from getpass import getpass
import json

with open("db_creds.json") as f:
	firebaseConfig = json.load(f)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()


def createAccount():
	email = input("email: ")
	password = getpass("pass: ")
	firstname = input("first: ")
	lastname = input("last: ")
	bio = input("bio: ")
	skills = [0]
	posts = [0]
	user = auth.create_user_with_email_and_password(email, password)
	uid = user["localId"]
	data = {
		"uid": uid,
		"firstname": firstname,
		"lastname": lastname,
		"bio": bio,
		"posts": posts,  # array of post ids
		"skills": skills,
	}
	db.child("users").child(uid).set(data)


createAccount()
