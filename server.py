from flask import Flask,request, make_response,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello World"

@app.route("/calculator/add", methods=['POST'])
def add():
    first=request.args.get('first')
    second=request.args.get('second')
    return jsonify(result=int(first)+ int (second))

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    first=request.args.get('first')
    second=request.args.get('second')
    return jsonify(result=int(first)- int (second))

if __name__ == '__main__':
    app.run(port=8080,host='127.0.0.1')
