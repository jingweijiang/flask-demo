
from flask import Flask, request, jsonify
from markupsafe import escape

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
   return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/score/<float:score>')
def show_score(score):
    return f'Score {score}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'


@app.route('/uuid/<uuid:uuid>')
def show_uuid(uuid):
    return f'UUID {escape(uuid)}'

if __name__ == '__main__':
        app.run(debug=True)