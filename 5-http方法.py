from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET'])
def login():
    
    if request.method == 'POST':
        return 'POST method'
    elif request.method == 'GET':
        return 'GET method'
    else:
        return 'Invalid method'
    
@app.get('/login/v1')
def login_get():
    return 'GET method'

@app.post('/login/v1')
def login_post():
    return 'POST method'
    
if __name__ == '__main__':
    app.run(debug=True)
