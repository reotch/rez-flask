from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'richard'}
    return render_template('index.html', title="Richard Sandrok—Software Developmer", user=user)