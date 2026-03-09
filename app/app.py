import os
from flask import Flask, jsonify

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "hostname": os.environ.get('HOSTNAME', 'unknown')
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
