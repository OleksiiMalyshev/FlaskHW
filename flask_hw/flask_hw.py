from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def index():
    return 'Hello world'

@app.route('/<a>/<b>/div')
def division(a, b):
    return f"{a} / {b} = {int(a)//int(b)}"

@app.route('/<a>/<b>/mult')
def multiply(a, b):
    return f"{a} * {b} = {int(a)*int(b)}"

@app.route('/<a>/<b>/plus')
def plus(a, b):
    return f"{a} + {b} = {int(a)+int(b)}"

@app.route('/<a>/<b>/minus')
def minus(a, b):
    return f"{a} - {b} = {int(a)-int(b)}"

app.run(host='0.0.0.0', port=8085, debug=True)
