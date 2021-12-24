from flask import Flask, jsonify, abort
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    theme = application.config['THEME']
    return flask.render_template('index.html', theme=theme, flask_debug=application.debug)

@app.route("/hello")
def hello():
    abort(404, 'hello abort')
    return jsonify({'message': 'error code 404'})

@app.errorhandler(404)
def error_404(e):
    print('httpステータス:{}, メッセージ:{}, 詳細:{}'.format(e.code, e.name, e.description))
    return jsonify({'message': 'internal server error', 'action': 'call me'}), 404

@app.route("/api/v1/hello")
def hello():
    return jsonify({
        "message": "Hello World!"
    })

if __name__ == "__main__":
    app.run()