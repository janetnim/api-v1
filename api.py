from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/login', methods=['POST'])


if __name__ == '__main__':
	app.run(debug = True)
