from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def hello_world():
    session["test"] = "shashlyk"
    return "<p>Hello, World!</p>"

@app.route("/cookie")
def return_cookie_id():
    return {"SessionID": session.sid, "test": session["test"]}