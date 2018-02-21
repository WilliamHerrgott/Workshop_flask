import os

from flask import Flask
from flask import session, render_template, request, flash, abort

from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Bonjour chef <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def login():

    POST_USERNAME = str(request.form['username'])
    POST_PASSWD = str(request.form['password'])

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWD]))
    result = query.first()

    if result:
        session['logged_in'] = True
    else:
        flash("wrong passwd")
    return home()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
