from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route('/projects/')
def project():
    return "This is the project page"

@app.route('/about')
def about():
    return "This is the about page"

