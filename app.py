from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, Docker!'

@app.route('/delay', methods=['GET', 'POST'])
def delay():
    if request.args:
        delay_sec = request.args.get("sec", default=0, type=int)
    elif request.form:
        delay_sec = request.form.get("sec", default=0, type=int)
    else:
        print("delay sec is Not specified.")
        delay_sec = 1
    delay_sec = max(min(100, delay_sec), 0)
    print(f"wait for {delay_sec}", flush=True)

    for x in range(0, delay_sec):
        time.sleep(1)
        if x % 10 == 0:
            print(x, end="", flush=True)
        else:
            print(".", end="", flush=True)
    print("TimesOut", flush=True)
    
    return jsonify({"delay": delay_sec})
