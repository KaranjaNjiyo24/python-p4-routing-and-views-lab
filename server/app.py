#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join([str(i) for i in range(parameter)] + [''])

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = float(num1)
    num2 = float(num2)

    operations = {
        '+': lambda x,y: x+y,
        '-': lambda x,y: x-y,
        '*': lambda x,y: x*y,
        'div': lambda x,y: x/y,
        '%': lambda x,y: x % y
    }

    result = operations[operation](num1, num2)

    if operation == 'div':
        return f'{result:.1f}'

    if result.is_integer():
        return str(int(result))
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
