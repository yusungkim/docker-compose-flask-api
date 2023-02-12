from flask import Flask, jsonify, request
import werkzeug
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return {"bad_request": "you should pass the 'sec' as integer"}, 400

# Hello
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Docker!'

# Delay
@app.route('/delay', methods=['GET', 'POST'])
def delay():
    if request.method == 'GET' and request.args:
        delay_sec = request.args.get("sec", default=0, type=int)
    elif request.method == 'POST' and request.json:
        delay_sec = request.json["sec"] or 0
    else:
        print("delay sec is Not specified.")
        delay_sec = 0
    delay_sec = max(min(100, delay_sec), 0)
    print(f"wait for {delay_sec}sec: ", flush=True, end="")

    for x in range(0, delay_sec):
        time.sleep(1)
        if (x+1) % 10 == 0:
            print(x, end="", flush=True)
        else:
            print(".", end="", flush=True)
    print(" TimesUp", flush=True)
    
    return jsonify({"delay": delay_sec})
