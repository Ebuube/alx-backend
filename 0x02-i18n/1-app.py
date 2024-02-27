#!/usr/bin/env python3
"""Start a Flask web application to serve dynamic web page
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


# Config class for languages
class Config:
    LANGUAGES = ['en', 'fr']


# Instantiates Babel object
babel = Babel(app)

# Set up babel
app.config.from_object(Config)
babel.default_locale = 'en'
babel.timezone = 'UTC'


@app.route('/', strict_slashes=False)
def home():
    """Return a home page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5000)
