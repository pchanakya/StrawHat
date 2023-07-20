import datetime
from markupsafe import escape
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/characters/')
def characters():
    return render_template('characters.html')
@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
@app.route('/add/<int:n1>/<int:n2>/')
def add(n1,n2):
    return '<h1>{}</h2>'.format(n1+n2)
@app.route('/users/<int:user_id>/')
def greet(user_id):
    users = ['Ashley', 'Nelson' , 'Harry']
    try:
        return '<h3>Hi {}</h3>'.format(users[user_id])
    except IndexError:
        abort(404)