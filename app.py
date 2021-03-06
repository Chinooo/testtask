from flask import Flask, request, jsonify
from json import dumps
import socket

app = Flask(__name__)

@app.route('/hello/<username>')
def hello_username(username):
    hostname = socket.gethostname()
    op = 'Hello %s from %s' % (username, hostname)
    result = {'message': op}
    return jsonify(result)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
