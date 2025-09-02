from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources="*")  # Enable CORS for frontend requests

@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

@app.route('/verify',methods=['GET'])
def verify():
    return jsonify({
        'status': 'verified',
        'redirect': '/VerifiedPage'
    })

if __name__ == '__main__':
    app.run(debug=True)
