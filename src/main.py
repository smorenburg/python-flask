import os

from flask import (Flask, request, jsonify)

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'}), 200


@app.route('/personal', methods=['POST'])
def hello():
    name = request.get_json()['name']

    return jsonify({'message': f'Hello {name}!'}), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
