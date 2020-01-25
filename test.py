from flask import Flask,redirect,render_template,url_for,flash,jsonify
from login import *
import json
app = Flask(__name__)

@app.route('/login',methods = ['POST'])
def login():
    user = request.form.get('username')
    passw = request.form.get('password')
    club = request.form.get('club')
    c, priv = check_authentication(user,passw,club)
    return jsonify(username = user, password = passw, club = club, privilege = priv, check = c )

@app.route('/forgotpassword')
def forgot():








if __name__ == '__main__':
    app.run()
