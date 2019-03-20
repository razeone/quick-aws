from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route('/user', methods=['POST'])
def home():
    return jsonify(request.__dict__), 200


if __name__ == '__main__':
    app.run()


