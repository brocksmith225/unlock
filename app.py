#!/usr/bin/env python
from flask import Flask, render_template
import os
app = Flask(__name__, template_folder='pages')

@app.route("/")
def opening():
    return render_template("opening.html", title="Unlock")

app.run(host="0.0.0.0", port=8080, debug=True)