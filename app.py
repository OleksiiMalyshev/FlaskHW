from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return 'Hello world'


@app.route('/<a>/<b>/div')
def division(a, b):
    sign = '/'
    answer = int(a) // int(b)
    return render_template('answer.html', a=a, b=b, sign=sign, answer=answer)


@app.route('/<a>/<b>/mult')
def multiply(a, b):
    sign = '*'
    answer = int(a) * int(b)
    return render_template('answer.html', a=a, b=b, sign=sign, answer=answer)


@app.route('/<a>/<b>/plus')
def plus(a, b):
    sign = '+'
    answer = int(a) + int(b)
    return render_template('answer.html', a=a, b=b, sign=sign, answer=answer)


@app.route('/<a>/<b>/minus')
def minus(a, b):
    sign = '-'
    answer = int(a) - int(b)
    return render_template('answer.html', a=a, b=b, sign=sign, answer=answer)


app.run(host='0.0.0.0', port=8080, debug=True)
