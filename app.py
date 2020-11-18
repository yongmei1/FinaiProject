from flask import Flask, render_template, request
from flask import *
import pyrebase

config = {
    "apiKey": "AIzaSyACPL6AK5ais6oLbrRi7VIb3VLW1lSeCNU",
    "authDomain": "finaisystem.firebaseapp.com",
    "databaseURL": "https://finaisystem.firebaseio.com",
    "projectId": "finaisystem",
    "storageBucket": "finaisystem.appspot.com",
    "messagingSenderId": "248168444493",
    "appId": "1:248168444493:web:47dab40823f05afaa82204",
    "measurementId": "G-L0PKXBNWQ7"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child("names").push({"name" : "mei"})
# db.child("names").child("name").update({"name":"chen"})
# users = db.child("names").child("name").get()
# print(users.val())
# db.child("names").remove()  #deletes that column

app = Flask(__name__)
auth = firebase.auth()


@app.route('/webintro.html', methods=['GET', 'POST'])
def hello_world():
    return render_template('webintro.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    unsuccessful = 'Please check your credentials'
    successful = 'Login successful'
    if request.method == 'POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
            return render_template('new.html', s=successful)
        except:
            return render_template('new.html', us=unsuccessful)
    return render_template('login.html')


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/mainpage.html', methods=['GET', 'POST'])
def mainpage():
    return render_template('mainpage.html')


if __name__ == '__main__':
    app.run(debug=True)
