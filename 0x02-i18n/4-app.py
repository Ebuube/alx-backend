#!/usr/bin/env python3
"""Start a Flask web application to serve dynamic web page
"""
from flask import Flask, render_template, request
from flask_babel import Babel   # note the dash
from typing import Optional


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False


# Config class for languages
class Config:
    """For the configuration of Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiates Babel object
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home() -> str:
    """Return a home page
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """Get the locale for a given web page
    """
    # Check if locale parameter is in request url
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # resort to the default behaviour
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5000)
