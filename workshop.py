import os

from flask import Flask
from flask import session, render_template, request, flash

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Bonjour chef"

@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash("wrong passwd")
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
