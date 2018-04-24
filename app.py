#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy, sqlalchemy
from flask.ext.socketio import emit, SocketIO
from flask.ext.session import Session
import os, uuid, psycopg2

app = Flask(__name__, template_folder='pages')
login_manager = LoginManager()
login_manager.init_app(app);
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ubuntu:Unl0ck@localhost/unlock"
app.config["SECRET_KEY"] = "something unique and secret"
app.config['SESSION_TYPE'] = 'filesystem'
db = SQLAlchemy(app)
socketIO = SocketIO(app)
url_prefix = "https://capstone-brocksmith225.c9users.io/"
Session(app)






#-----USER ACCOUNT SET-UP-----#
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
        
class NileUser(db.Model):
    
    __tablename__ = "nile_users"
    
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
        
class PursueUser(db.Model):
    
    __tablename__ = "pursue_users"
    
    account = db.Column(db.String(40), unique=True, primary_key=True)
    pwd = db.Column(db.String(64))
    balance = db.Column(db.Integer, default=1000)

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
        
class SIRUser(db.Model):
    
    __tablename__ = "sir_user"
    
    email = db.Column(db.String(40))
    pwd = db.Column(db.String(64))
    uid = db.Column(db.Integer, primary_key=True)

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
        
db.create_all()
db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
#-----END USER ACCOUNT FUNCTIONALITY-----#
    
    
    


#-----BASE WEBSITE FUNCTIONALITY-----#
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

@app.route("/logout")
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_prefix)
#-----END BASE WEBSITE FUNCTIONALITY-----#

   



#-----UI FUNCTIONALITY-----#
@app.route("/level-1")
@login_required
def level1():
    if int(current_user.progress) >= 1:
        return render_template("ui.html", level="1", page="index", level_progress=current_user.level1_progress, max_level_progress=3, flag=True)
    return redirect(url_prefix)
    
@app.route("/level-2")
@login_required
def level2():
    if int(current_user.progress) >= 2:
        return render_template("ui.html", level="2", page="index", level_progress=current_user.level2_progress, max_level_progress=4, flag=False)
    return redirect(url_prefix)
    
@app.route("/level-3")
@login_required
def level3():
    if int(current_user.progress) >= 3:
        return render_template("ui.html", level="3", page="index", level_progress=current_user.level3_progress, max_level_progress=3, flag=False)
    return redirect(url_prefix)
    
@app.route("/level-4")
@login_required
def level4():
    if int(current_user.progress) >= 4:
        return render_template("ui.html", level="4", page="index", level_progress=current_user.level4_progress, max_level_progress=4, flag=True)
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
        if str(level) == "1":
            if int(current_user.level1_progress) <= 2:
                current_user.level1_progress = 3
            if int(current_user.progress) <= 1:
                current_user.progress = 2
        else:
            if int(current_user.level4_progress) <= 3:
                current_user.level4_progress = 4
            if int(current_user.progress) <= 4:
                current_user.progress = 5
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
#-----END UI FUNCTIONALITY-----#

    
    
    
    
#-----FIRST LEVEL FUNCTIONALITY-----#
@app.route("/level-1/index")
@login_required
def level1Index():
    socketIO.emit("level-progress-update", {"level_progress" : "test"})
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
            session["account"] = user.account
            return redirect(url_prefix + "level-1/inbox", code=307)
    return redirect(url_prefix + "level-1/index")

@app.route("/level-1/inbox", methods=["POST"])
@login_required
def level1Inbox():
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM bmail_emails;")
    res = cur.fetchall()
    cur.close()
    conn.close()
    emails = [dict() for x in range(len(res))]
    account = session["account"]
    for i in range(len(res)-1, -1, -1):
        if res[i][4] == account:
            emails[i]["title"] = res[i][0]
            emails[i]["body"] = res[i][1]
            emails[i]["sender"] = res[i][2]
            emails[i]["tags"] = res[i][3]
    return render_template("level-1/inbox.html", account=account, emails=emails, count=len(emails))

@app.route("/level-1/<page>")
@login_required
def level1Subpage(page):
    return render_template("level-1/" + page + ".html")
    
@app.route("/level-1/info")
@login_required
def info1():
    if int(current_user.progress) > 1:
        return render_template("info-pages/level-1.html")
    return redirect(url_prefix)
#-----END FIRST LEVEL FUNCTIONALITY-----#

    
    
    

#-----SECOND LEVEL FUNCTIONALITY-----#
@app.route("/level-2/index", methods=["GET", "POST"])
@login_required
def level2Index():
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM nile_items;")
    res = cur.fetchall()
    cur.close()
    conn.close()
    items = [dict() for x in range(len(res))]
    for i in range(len(res)-1, -1, -1):
        items[i]["name"] = res[i][0]
        items[i]["price"] = res[i][1]
        items[i]["image"] = res[i][2]
    if (request.method == "POST"):
        return render_template("level-2/index.html", items=items, count=len(items), username=str(session["account"]))
    return render_template("level-2/index.html", items=items, count=len(items), username="anonymous")

@app.route("/level-2/search", methods=["POST"])
@login_required
def level2Search():
    if int(current_user.level2_progress) <= 0:
        current_user.level2_progress = 1
        db.session.commit()
    term = str(request.form["term"])
    if "'" in term or ";" in term or "--" in term:
        if int(current_user.level2_progress) <= 1:
            current_user.level2_progress = 2
            db.session.commit()
    conn = psycopg2.connect("dbname=nile user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE tags LIKE '%" + term + "%';")
    res = cur.fetchall()
    cur.close()
    conn.close()
    items = [dict() for x in range(len(res))]
    for i in range(len(res)-1, -1, -1):
        for j in range(0, len(res[i])):
            if str(res[i][j]) == "letmein":
                if int(current_user.level2_progress) <= 2:
                    current_user.level2_progress = 3
                    db.session.commit()
        items[i]["name"] = res[i][0]
        items[i]["price"] = res[i][1]
        items[i]["image"] = res[i][2]
    return str(items)

@app.route("/level-2/signin", methods=["POST"])
@login_required
def level2SignIn():
    user = NileUser.query.get(request.form["username"])
    if user:
        if request.form["password"] == user.pwd:
            if str(request.form["username"]) == "realDonaldTrump":
                if int(current_user.level2_progress) <= 3:
                    current_user.level2_progress = 4
                if int(current_user.progress) <= 2:
                    current_user.progress = 3
                db.session.commit()
            session["account"] = user.account
            return redirect(url_prefix + "level-2/index", code=307)
    return redirect(url_prefix + "level-2/index")

@app.route("/level-2/signup", methods=["POST"])
@login_required
def level2SignUp():
    pwd = request.form["password"]
    account = request.form["username"]
    user = NileUser(account=account, pwd=pwd)
    db_user = NileUser.query.get(account)
    if db_user:
        return redirect(url_prefix + "level-2/index")
    db.session.add(user)
    db.session.commit()
    session["account"] = user.account
    return redirect(url_prefix + "level-2/index", code=307)

@app.route("/level-2/<page>")
@login_required
def level2Subpage(page):
    return render_template("level-2/" + page + ".html")
    
@app.route("/level-2/info")
@login_required
def info2():
    if int(current_user.progress) > 2:
        return render_template("info-pages/level-2.html")
    return redirect(url_prefix)
#-----END SECOND LEVEL FUNCTIONALITY-----#




#-----THIRD LEVEL FUNCTIONALITY-----#
@app.route("/level-3/index")
@login_required
def level3Index():
    return render_template("level-3/index.html")
    
@app.route("/level-3/account-control", methods=["POST"])
@login_required
def level3AccountControl():
    b = PursueUser.query.get(session["account"]).balance
    balance = "$" + "%.2f" % (b/100)
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT * FROM pursue_actions;")
    res = cur.fetchall()
    cur.close()
    conn.close()
    actions = [dict() for x in range(len(res))]
    for i in range(len(res)-1, -1, -1):
        if str(res[i][0]) == str(session["account"]):
            actions[i]["name"] = str(res[i][1])
            actions[i]["type"] = str(res[i][2])
            actions[i]["change"] = str(res[i][3])
    return render_template("level-3/account-control.html", account=session["account"], newAccount=session["new"], balance=balance, actions=actions, count=len(actions))

@app.route("/level-3/signin", methods=["POST"])
@login_required
def level3SignIn():
    user = PursueUser.query.get(request.form["account"])
    if user:
        if request.form["password"] == user.pwd:
            session["account"] = user.account
            session["new"] = False
            return redirect(url_prefix + "level-3/account-control", code=307)
    return redirect(url_prefix + "level-3/account")

@app.route("/level-3/signup", methods=["POST"])
@login_required
def level3SignUp():
    pwd = request.form["password"]
    account = request.form["account"]
    user = PursueUser(account=account, pwd=pwd)
    db_user = PursueUser.query.get(account)
    if db_user:
        return redirect(url_prefix + "level-3/account")
    db.session.add(user)
    db.session.commit()
    if int(current_user.level3_progress) <= 0:
        current_user.level3_progress = 1
        db.session.commit()
    session["account"] = user.account
    session["new"] = True
    return redirect(url_prefix + "level-3/account-control", code=307)

@app.route("/level-3/transfer")
@login_required
def level3Transfer():
    amount = float(request.args.get("amount")) * 100
    account = request.args.get("account")
    selfTransfer = False
    if int(current_user.level3_progress) <= 1:
        current_user.level3_progress = 2
        db.session.commit()
    if not account is None:
        user = PursueUser.query.get(account)
        if user:
            selfTransfer = True
            if int(current_user.level3_progress) <= 2:
                current_user.level3_progress = 3
            if int(current_user.progress) <= 3:
                current_user.progress = 4
            db.session.commit()
            user.balance += amount
            db.session.commit()
            conn = psycopg2.connect("dbname=unlock user=ubuntu")
            cur = conn.cursor()
            cur.execute("INSERT INTO pursue_actions VALUES ('" + str(account) + "', 'Transfer from Another User', 'transfer', '+$" + "%.2f" % (amount/100) + "');")
            cur.close()
            conn.commit()
            conn.close()
    return render_template("level-3/transfer.html", amount="$" + "%.2f" % float(request.args.get("amount")), account=request.args.get("account", default="a random account"), selfTransfer=selfTransfer)

@app.route("/level-3/info")
@login_required
def level3Info():
    return render_template("info-pages/level-3.html")

@app.route("/level-3/<page>")
@login_required
def level3Subpage(page):
    return render_template("level-3/" + page + ".html")
#-----END THIRD LEVEL FUNCTIONALITY-----#




#-----FOURTH LEVEL FUNCTIONALITY-----#
@app.route("/level-4/login", methods=["POST"])
@login_required
def level3Login():
    conn = psycopg2.connect("dbname=unlock user=ubuntu")
    cur = conn.cursor()
    cur.execute("SELECT uid FROM sir_users WHERE email='" + request.form["email"] + "';")
    res = cur.fetchall()
    cur.close()
    conn.close()
    user = SIRUser.query.get(res)
    if user:
        if request.form["password"] == user.pwd:
            session["account"] = user.uid
            return redirect(url_prefix + "level-4/file", code=307)
    return redirect(url_prefix + "level-4/index")

@app.route("/level-4/create-account", methods=["POST"])
@login_required
def level4CreateAccount():
    pwd = request.form["password"]
    email = request.form["email"]
    user = SIRUser(email=email, pwd=pwd)
    db.session.add(user)
    db.session.commit()
    if int(current_user.level4_progress) <= 0:
        current_user.level4_progress = 1
        db.session.commit()
    session["account"] = user.uid
    return redirect(url_prefix + "level-4/file", code=307)
    
@app.route("/level-4/file", methods=["POST"])
@login_required
def level4File():
    return render_template("level-4/file.html", account=session["account"])
    
@app.route("/level-4/1040")
@login_required
def level41040():
    if str(request.args.get("account")) == "0":
        if int(current_user.level4_progress) <= 2:
            current_user.level4_progress = 3
            db.session.commit()
        return render_template("level-4/1040-0.html")
    else:
        if int(current_user.level4_progress) <= 1:
            current_user.level4_progress = 2
            db.session.commit()
    return render_template("level-4/1040-1.html")
    
@app.route("/level-4/info")
@login_required
def level4Info():
    return render_template("info-pages/level-4.html")

@app.route("/level-4/<page>")
@login_required
def level4Subpage(page):
    return render_template("level-4/" + page + ".html")
#-----END FOURTH LEVEL FUNCTIONALITY-----#




#-----SCREENSHOT FUNCTIONALITY-----#
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
#-----END SCREENSHOT FUNCTIONALITY-----#





app.run(host="0.0.0.0", port=8080, debug=True)
socketIO.run(app)