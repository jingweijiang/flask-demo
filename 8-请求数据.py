from calendar import c
from os import error
from flask import Flask, request, jsonify, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # username = request.form.get('username')
        # password = request.form.get('password')
        
        username = request.json.get('username')
        password = request.json.get('password')
        if username == 'admin' and password == '123456':
            return jsonify({'code': 0,'msg': '登录成功'})
        else:
            return jsonify({'code': 1,'msg': '用户名或密码错误'})
    
    elif request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        if username == 'admin' and password == '123456':
            return jsonify({'code': 0,'msg': '登录成功'})
        else:
            return jsonify({'code': 1,'msg': '用户名或密码错误'})
    else:
        return jsonify({'code': 2,'msg': '请求错误'})
    
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files.get('file')
    if file:
        file.save('upload/' + secure_filename(file.filename))
        return jsonify({'code': 0,'msg': '上传成功'})
    else:
        return jsonify({'code': 1,'msg': '上传失败'})


@app.route('/set_cookie')
def set_cookie():
    resp = make_response("set_cookie action success")
    resp.set_cookie('username', 'admin')
    return resp

@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('username')
    if cookie:
        return jsonify({'code': 0,'msg': '获取成功', 'data': {'username': cookie}})
    else:
        return jsonify({'code': 1,'msg': '获取失败'})

@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response("delete_cookie action success")
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)