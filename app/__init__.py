from flask import Flask, render_template, request, jsonify
from flask import session, redirect, url_for

app = Flask(__name__)
app.secret_key = "vnnnnn"

@app.route("/", methods=["GET", "POST"])
def start():
    return render_template('start.html')
    
@app.route("/select", methods=["GET", "POST"])
def select():
    return render_template('select.html')
    
@app.route("/map", methods=["GET", "POST"])
def map():
    return render_template('map.html')
    
@app.route("/room", methods=["GET", "POST"])
def room():
    return render_template('room.html')

@app.route("/end", methods=["GET", "POST"])
def end():
    return render_template('end.html')
    
if __name__ == "__main__":
    app.debug = False
    app.run()