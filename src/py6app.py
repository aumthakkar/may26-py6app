from flask import Flask, jsonify
import time
import socket

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/api/v1/info')
def info():
    return jsonify({
       "time": time.ctime(),
       "host": socket.gethostname(),
        "env": "dev",
        "msg": "Hi Pranav, how are you man? :-)"
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
       "status": "up",

    })
    
if __name__ == '__main__':
    app.run("0.0.0.0")