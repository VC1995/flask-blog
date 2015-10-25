#blog.py - controller

from flask import Flask, render_template, request, session, flash, \
redirect, url_for, g
import sqlite3
from functools import wraps

# configuration
DATABASE= 'blog.db'
USERNAME= 'admin'
PASSWORD= 'password'
SECRET_KEY= 'rM\xb1\xdc\x12o\xd6i\xff+9$T\x8e\xec\x00\x13\x82.*\x16TG\xbc'

app= Flask(__name__)

app.config.from_object(__name__)

def login_required(test) :
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'logged_in' in session :
            return test(*args,**kwargs)
        else :
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap

@app.route("/", methods=['GET','POST'])
def login() :
    error= None
    if request.method == 'POST' :
        if request.form['username'] != app.config['USERNAME'] or \
        request.form['password'] != app.config['PASSWORD'] :
            error= "Invalid credentials."
        else :
            session['logged_in']= True
            return redirect(url_for('main'))
    return render_template('login.html', error= error)

@app.route("/main")
@login_required
def main():
    return render_template('main.html')

@app.route("/logout")
@login_required
def logout() :
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug=True)