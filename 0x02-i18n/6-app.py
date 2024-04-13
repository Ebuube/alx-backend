#!/usr/bin/env python3
"""Start a Flask web application to serve dynamic web page
"""
from flask import Flask, render_template, request, g
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


def get_user_preferred_locale() -> str:
    """Return user's choice locale
    """
    if hasattr(g, 'user') and g.user and 'locale' in g.user:
        user_locale = g.user['locale']
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return ''


@app.before_request
def before_request():
    """Handle specific tasks like getting user
    """
    user_id = request.args.get('login_as')
    try:
        user_id = int(user_id)
    except TypeError:
        pass
    user = get_user(user_id)

    # Set the user as a Global
    g.user = user


@app.route('/')
def home() -> str:
    """Return a home page
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """Get the locale for a given web page
    """
    # Check if locale parameter is in request url
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Locale from user settings
    user_pref_locale = get_user_preferred_locale()
    if user_pref_locale and user_pref_locale in app.config['LANGUAGES']:
        return user_pref_locale

    # 3. Locale from request header
    header_locale = request.accept_languages.best_match(
            app.config['LANGUAGES'])
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale

    # resort to the default behaviour
    return babel.default_locale


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5000)
