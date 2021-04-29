from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == 'GET':
        return render_template("kontakt.html")
    elif request.method == 'POST':
        print(request.form)
        return redirect("/kontakt")

@app.route('/index')
def index():
    return render_template("index.html")