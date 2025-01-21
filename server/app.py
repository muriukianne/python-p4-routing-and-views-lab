#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'  


@app.route('/count/<int:parameter>')
def count(parameter):
    print('\n'.join(str(p) for p in range(parameter)) + '\n')
    return '\n'.join(str(p) for p in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<operation>/<int:num2>')   
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '/' or operation == 'div': 
        if num2 != 0:
            return str(num1 / num2)
        else:
            return 'Cannot divide by zero!'
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Error: Invalid operation'




if __name__ == '__main__':
    app.run(port=5555, debug=True)
