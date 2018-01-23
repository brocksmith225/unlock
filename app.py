#!/usr/bin/env python
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
import os, uuid, psycopg2
app = Flask(__name__, template_folder='pages')
login_manager = LoginManager()
login_manager.init_app(app);
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ubuntu:Unl0ck@localhost/unlock"
app.config["SECRET_KEY"] = "something unique and secret"
db = SQLAlchemy(app)

class User(db.Model):
    
    __tablename__ = "unlock_users"
    
    email = db.Column(db.String(40), unique=True, primary_key=True)
    pwd = db.Column(db.String(64))
    progress = db.Column(db.Integer, default=0)
    authenticated = db.Column(db.Boolean, default=False)
    
    def is_active(self):
        return True;
    
    def is_authenticated(self):
        return self.authenticsated
        
    def is_anonymous(self):
        return False;
    
    def get_id(self):
        return self.email
        
    @staticmethod
    def get(user_id):
        return 1
        
db.create_all()
db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/")
def opening():
    return render_template("opening.html")
    
@app.route("/ui")
def ui():
    return render_template("ui.html")
    
@app.route("/create-account", methods=["POST"])
def createAccount():
    pwd = request.form["password"]
    email = request.form["email"]
    user = User(email=email, pwd=pwd)
    db_user = User.query.get(email)
    if db_user:
        return render_template("login.html", success=False)
    db.session.add(user)
    db.session.commit()
    return render_template("login.html", success=True)
    
@app.route("/login", methods=["POST"])
def login():
    user = User.query.get(request.form["email"])
    if user:
        if request.form["password"] == user.pwd:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect("/")
    return render_template("unsuccessful-create-account.html")
    
app.run(host="0.0.0.0", port=8080, debug=True)