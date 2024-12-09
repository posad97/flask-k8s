from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector
import os

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def hello_world():
    session["test"] = "shashlyk"
    db = mysql.connector.connect(
        host = os.environ.get("DB_HOSTNAME"),      # Name of the MySQL container
        user = os.environ.get("DB_USERNAME"),      # MySQL user
        password = os.environ.get("DB_PASSWORD"),  # Root password
        database = os.environ.get("DB_NAME")       # Database name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")  # Query the users table
    result = cursor.fetchall()

    return str(result)
    # return "<p>Hello, World!</p>"



@app.route("/cookie")
def return_cookie_id():
    return {"SessionID": session.sid, "test": session["test"]}