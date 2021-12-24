from flask import Flask, jsonify, abort
import json

main = Flask(__name__)

@main.route("/hello")
def hello():
    abort(404, 'hello abort')
    return jsonify({'message': 'error code 404'})

@main.errorhandler(404)
def error_404(e):
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return jsonify({'message': 'internal server error', 'action': 'call me'}), 404

@main.route("/api/v1/hello")
def hello():
    return jsonify({
        "message": "Hello World!"
    })

if __name__ == "__main__":
    app.run()