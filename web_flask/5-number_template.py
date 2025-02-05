#!/usr/bin/python3
""" A python script that starts a web application
With listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a given string"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return a given string"""
    return f'C {text.replace("_"," ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Return a given string"""
    return f'Python {text.replace("_"," ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a given string with a placeholder of integer (n)"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    """Display render HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
