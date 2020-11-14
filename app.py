from flask import Flask, render_template, request
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

db.child("names").push({"name":"mei"})

app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('webintro.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/register.html')
def register():
    return render_template('register.html')


@app.route('/mainpage.html')
def mainpage():
    return render_template('mainpage.html')


if __name__ == '__main__':
    app.run(debug=True)
