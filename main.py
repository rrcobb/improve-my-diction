"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
from flask import render_template
from flask import request
from translate import translate

app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def show_index():
    #return "Hello"
    return render_template('index.html', submitted = False)

@app.route('/', methods=['POST'])
def display_translation():
    original_text = request.form['text_to_translate']
    new_text = translate(original_text)
    return render_template('index.html', submitted = True, translated_text = new_text)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
