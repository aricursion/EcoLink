import pyrebase

from getpass import getpass
import json

# with open("db_creds.json") as f:
# 	firebaseConfig = json.load(f)

# firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()
# auth = firebase.auth()


def createAccount(db, auth, email, password, firstname, lastname, bio, skills):
	# email = input("email: ")
	# password = getpass("pass: ")
	# firstname = input("first: ")
	# lastname = input("last: ")
	# bio = input("bio: ")
	# skills = [0]
	# postids = [0]
	user = auth.create_user_with_email_and_password(email, password)
	uid = user["localId"]
	data = {
		"uid": uid,
		"email": email,
		"firstname": firstname,
		"lastname": lastname,
		"bio": bio,
		"postids": [0],  # array of post ids
		"skills": skills,
	}
	db.child("users").child(uid).set(data)


# createAccount("test@test.com", "TESTTEST", "test", "test", "test", ["NA"])

def loginAccount(db, auth, email, password):
	signin = auth.sign_in_with_email_and_password(email, password)
	print("hoorary!")
	return auth.get_account_info(signin["idToken"])["users"][0]["localId"]

