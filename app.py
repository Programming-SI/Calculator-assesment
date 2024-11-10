"""SIMPLE CALCULATOR ASSESSMENT."""

from flask import Flask, request

app = Flask(__name__)

"""Calculate"""
@app.route('/calculate')
def calculate():
    """Function calculating."""
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)
    op = request.args.get('op', type=str)


    if arg1 and arg2 and op:

        arg1 = int(arg1)
        arg2 = int(arg2)

        if op == 'sum':
            result = arg1 + arg2

        return f'{arg1} {op} {arg2} = {result}'


    app.run()
