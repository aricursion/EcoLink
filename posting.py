import pyrebase

"""
import json

with open("db_creds.json") as f:
    firebaseConfig = json.load(f)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
"""

def likePost(db, uid, post):
    likes = db.child("posts").child(post).child("likes").get().val()
    likes.append(uid)

    db.child("posts").child(post).update({"likes" : likes})

def confirmAttendance(db, uid, post):
    attends = db.child("posts").child(post).child("attendees").get().val()
    attends.append(uid)

    db.child("posts").child(post).update({"attendees" : attends})

def createPost(db, uid, desc, img, loc, ts):
    user = "{0} {1}".format(
        db.child("users").child(uid).child("firstname").get().val(),
        db.child("users").child(uid).child("lastname").get().val()
    )

    data = {
        "attendees" : [uid], 
        "author" : uid, 
        "description" : desc, 
        "image" : img, 
        "likes" : [uid], 
        "location" : loc, 
        "name" :user, 
        "timestamp" : ts
    }
    
    name = db.child("posts").push(data)["name"]
    pids = db.child("users").child(uid).child("postids").get().val()
    pids.append(name)
    db.child("users").child(uid).update({"postids" : pids})

    return name

def deletePost(db, post):
    author = db.child("posts").child(post).child("author").get().val()
    arr = db.child("users").child(author).child("postids").get().val()
    arr.remove(post)
    db.child("users").child(author).update({"postids" : arr})

    db.child("posts").child(post).remove()
    return post

def fetchAllPosts(db):
    posts = db.child("posts").get()
    ans = {}
    for post in posts.each():
        ans[post.key()] = post.val()
    return ans

def fetchFollowingPost(db, user):
    following = db.child("users").child(user).child("following").get().val()
    posts = fetchAllPosts(db)
    ans = {}
    for i in posts:
        if (posts[i]["author"] in following):
            ans[i] = posts[i]
    return ans

"""
name = createPost(db,
"kpGSUuqnruSOvfQRZRBy71aBTAg1",
"fun stuff",
"https://cerncourier.com/wp-content/uploads/2018/06/CCnew13_01_17-1.jpg",
"123 peepee lane, richardson, tx 75081",
1587788097
)
print(name)
likePost(db,"jeff",name)
confirmAttendance(db,"jeff",name)

deletePost(db, "-M5jgXVgKjI1UhM9CvUw")
"""