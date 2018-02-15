#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
import os, uuid, psycopg2

app = Flask(__name__, template_folder='pages')
login_manager = LoginManager()
login_manager.init_app(app);
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ubuntu:Unl0ck@localhost/unlock"
app.config["SECRET_KEY"] = "something unique and secret"
db = SQLAlchemy(app)
url_prefix = "https://capstone-brocksmith225.c9users.io/"

class User(db.Model):
    
    __tablename__ = "unlock_users"
    
    email = db.Column(db.String(40), unique=True, primary_key=True)
    pwd = db.Column(db.String(64))
    progress = db.Column(db.Integer, default=1)
    level1_progress = db.Column(db.Integer, default=0)
    level2_progress = db.Column(db.Integer, default=0)
    level3_progress = db.Column(db.Integer, default=0)
    level4_progress = db.Column(db.Integer, default=0)
    authenticated = db.Column(db.Boolean, default=False)
    difficulty = db.Column(db.Integer, default=0)

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated
        
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.email
        
    @staticmethod
    def get(user_id):
        return 1
        
class BMailUser(db.Model):
    
    __tablename__ = "bmail_users"
    
    account = db.Column(db.String(40), unique=True, primary_key=True)
    pwd = db.Column(db.String(64))

    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated
        
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.account
        
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
    try:
        if current_user.is_authenticated():
            return render_template("menu.html", progress=current_user.progress, level1_progress=current_user.level1_progress, level2_progress=current_user.level2_progress, level3_progress=current_user.level3_progress, level4_progress=current_user.level4_progress)
        return render_template("opening.html")
    except Exception:
        pass
    return render_template("opening.html")
    
@app.route("/create-account", methods=["POST"])
def createAccount():
    pwd = request.form["password"]
    email = request.form["email"]
    difficulty = request.form["difficulty"]
    user = User(email=email, pwd=pwd, difficulty=difficulty)
    db_user = User.query.get(email)
    if db_user:
        return render_template("login.html", success=False)
    user.authenticated = True
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)
    return redirect(url_prefix)
    
@app.route("/login", methods=["POST"])
def login():
    user = User.query.get(request.form["email"])
    if user:
        if request.form["password"] == user.pwd:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_prefix)
    return render_template("unsuccessful-login.html")
    
@app.route("/tutorial")
@login_required
def tutorial():
    return ""

@app.route("/logout")
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return "logged out"
    
@app.route("/level-<level>")
@login_required
def level1(level):
    if int(current_user.progress) >= int(level):
        return render_template("ui.html", level=level, page="index")
    return redirect(url_prefix)
    
@app.route("/flag-check/<level>", methods=["POST"])
def flagCheck(level):
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM unlock_flags WHERE level=" + level + ";")
    res = cur.fetchone()
    cur.close()
    conn.close()
    if str(request.form["flag"]) == str(res[1]):
        if int(current_user.level1_progress) <= 2:
            current_user.level1_progress = 3
        if int(current_user.progress) <= 1:
            current_user.progress = 2
        db.session.commit()
        return "true"
    return "false"
    
@app.route("/get-hint/<level>", methods=["POST"])
def getHint(level):
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    if int(level) == 1:
        cur.execute("SELECT hint FROM unlock_hints WHERE level=1 AND progress=" + str(current_user.level1_progress) + " AND difficulty=" + str(current_user.difficulty) +";")
        res = cur.fetchone()
    elif int(level) == 2:
        cur.execute("SELECT hint FROM unlock_hints WHERE level=2 AND progress=" + str(current_user.level2_progress) + " AND difficulty=" + str(current_user.difficulty) +";")
        res = cur.fetchone()
    elif int(level) == 3:
        cur.execute("SELECT hint FROM unlock_hints WHERE level=3 AND progress=" + str(current_user.level3_progress) + " AND difficulty=" + str(current_user.difficulty) +";")
        res = cur.fetchone()
    elif int(level) == 4:
        cur.execute("SELECT hint FROM unlock_hints WHERE level=4 AND progress=" + str(current_user.level4_progress) + " AND difficulty=" + str(current_user.difficulty) +";")
        res = cur.fetchone()
    cur.close()
    conn.close()
    return str(res[0])

@app.route("/level-1/index")
@login_required
def level1Index():
    return render_template("level-1/index.html")

@app.route("/level-1/create-account", methods=["POST"])
@login_required
def level1CreateAccount():
    pwd = request.form["password"]
    account = request.form["account"]
    user = BMailUser(account=account, pwd=pwd)
    db_user = BMailUser.query.get(account)
    if db_user:
        return redirect(url_prefix + "level-1/index")
    db.session.add(user)
    db.session.commit()
    if int(current_user.level1_progress) <= 0:
        current_user.level1_progress = 1
        db.session.commit()
    return redirect(url_prefix + "level-1/inbox?account=" + user.account)

@app.route("/level-1/login", methods=["POST"])
@login_required
def level1Login():
    user = BMailUser.query.get(request.form["account"])
    if user:
        if request.form["password"] == user.pwd:
            if int(current_user.level1_progress) <= 1 and str(request.form["account"]) == "dev.team":
                current_user.level1_progress = 2
                db.session.commit()
            return redirect(url_prefix + "level-1/inbox?account=" + user.account)
    return redirect(url_prefix + "level-1/index")

@app.route("/level-1/inbox")
@login_required
def level1Inbox():
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bmail_emails;")
    res = cur.fetchall()
    cur.close()
    conn.close()
    emails = [dict() for x in range(len(res))]
    account = request.args.get("account")
    for i in range(0, len(res)):
        if res[i][4] == account:
            emails[i]["title"] = res[i][0]
            emails[i]["body"] = res[i][1]
            emails[i]["sender"] = res[i][2]
            emails[i]["tags"] = res[i][3]
    return render_template("level-1/inbox.html", account=account, emails=emails)

@app.route("/level-1/<page>")
@login_required
def level1Subpage(page):
    return render_template("level-1/" + page + ".html")
    
@app.route("/level-1/info")
@login_required
def info():
    if int(current_user.progress) > 1:
        return render_template("info-pages/level-1.html")
    return redirect("/")

@app.route("/screenshot/<page>")
@login_required
def screenshot(page):
    if current_user.email == "brocksmith225@gmail.com":
        return render_template(page + ".html")
    return redirect(url_prefix)

@app.route("/screenshot/<folder>/<page>")
@login_required
def screenshot2(folder, page):
    if current_user.email == "brocksmith225@gmail.com":
        return render_template(folder + "/" + page + ".html")
    return redirect(url_prefix)
    
app.run(host="0.0.0.0", port=8080, debug=True)