#!/usr/bin/env python3
"""Start a Flask web application to serve dynamic web page
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel   # note the dash
from typing import Optional, Dict, Any


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> object:
    """Find a user and return them
    or None
    """
    return users.get(user_id, None)


@app.before_request
def before_request():
    """Handle specific tasks like getting user
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
    except TypeError:
        pass
    print("User id is: {}".format(user_id))
    user = get_user(user_id)

    # Set the user as a Global
    g.user = user


@app.route('/')
def home() -> str:
    """Return a home page
    """
    return render_template('5-index.html')


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
