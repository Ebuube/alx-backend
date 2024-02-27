#!/usr/bin/python3
"""Start a Flask web application to server dynamic web page
"""
from flask import Flask, render_template


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/', strict_slashes=False)
def home():
    """Return a home page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5000)
