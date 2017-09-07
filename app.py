from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/harekaze/ship.json")
def api_ship():
    # 進入 Request 後，發出一個 Request
    request = requests.get('https://api.harekaze.moe/ship.json')

    # 把結果丟回去
    return request.text

    ## 思考：如果 API 有很多路徑，你要怎麼處裡？可能會無法窮舉喔！