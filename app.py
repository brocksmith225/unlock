#!/usr/bin/env python
from flask import Flask, render_template, request
from flask.ext.login import LoginManager
import os, uuid, psycopg2
app = Flask(__name__, template_folder='pages')
login_manager = LoginManager()

@app.route("/")
def opening():
    return render_template("opening.html")
    
@app.route("/ui")
def ui():
    return render_template("ui.html")
    
@app.route("/create-account", methods=["POST"])
def createAccount():
    usr = request.form["username"]
    pwd = request.form["password"]
    email = request.form["email"]
    
    try:
        conn = psycopg2.connect(dbname="unlock", user="ubuntu", password="Unl0ck", host="localhost")
    except:
        return render_template("unsuccessful-create-account.html")
        
    cur = conn.cursor()
    
    sql = "INSERT INTO users (usr, pwd, email, progress) values ('" + usr + "', '" + pwd + "', '" + email + "', 0);"
    
    try:
        cur.execute(sql)
    except Exception, e:
        return render_template("login.html", success=False)
    
    conn.commit()
    conn.close()
    return render_template("login.html", success=True)
    
@app.route("/test")
def test():
    return render_template("unsuccessful-create-account.html")
    
class User:
    is_authenticated = False
    is_active = True
    is_anonymous = True
    u_id = uuid.uuid4()
    def get_id():
        return u_id

app.run(host="0.0.0.0", port=8080, debug=True)