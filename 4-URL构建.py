from flask import Flask, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/user/<username>')
def profile(username):
    return 'profile page for user %s' % username


with app.test_request_context():
    print(url_for('index')) # /
    print(url_for('login')) # /login
    print(url_for('login', next='/'))   # /login?next=/
    print(url_for('profile', username='jingwei.jiang')) # /user/jingwei.jiang