from flask import Flask, request, jsonify, render_template, jsonify

app = Flask(__name__)

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@app.route('/list')
def get_list():
    return ['apple', 'banana', 'orange']

@app.route('/json')
def get_json():
    return jsonify({'name': 'John', 'age': 30})


if __name__ == '__main__':
    app.run(debug=True)