from flask import Flask, app, redirect, url_for, request, render_template, flash, session, abort, jsonify



app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/redirect')
def redirect_to_index():
    return redirect(url_for('index'))   


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)