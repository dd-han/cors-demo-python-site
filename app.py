from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/harekaze/ship.json")
def api_ship():
    request = requests.get('https://api.harekaze.moe/ship.json')
    return request.text