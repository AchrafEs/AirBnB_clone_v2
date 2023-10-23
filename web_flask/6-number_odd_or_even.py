#!/usr/bin/python3
"""Starts a Flask web app."""

from flask import Flask, request, render_template

app = Flask(__name__)


def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays C followed by the value of <text>."""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ displays 'Python' followed by the value of <text>
    replaces any underscores in <text> with slashes.
    """
    formatted_text = text.replace('_', ' ')
    return "Python {}".format(formatted_text)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ displays an html page only if <n> is an integer
    states whether 'n' is odd or even in the body.
    """
    # check if n is an integer
    if isinstance(n, int):
        even_or_odd = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html',
                               n=n, even_or_odd=even_or_odd)
    else:
        return "Invalid input. Please provide an integer."


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ displays <n is a number> only if n is an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ displays an HTML page only if 'n' is an integer """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
