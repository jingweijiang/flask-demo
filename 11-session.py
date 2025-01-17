import re
from flask import session, Flask, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        app.logger.debug('A value for debugging')
        return 'Logged in as %s' % session['username']
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    
    return '''
        <form method="post">
            <p><input type="text" name="username"></p>
            <p><input type="submit" value="Login"></p>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':        
    app.run(debug=True)