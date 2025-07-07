from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})  # Enable CORS for frontend requests

@app.route('/verify',methods=['GET'])
def verify():
    return jsonify({
        'status': 'verified',
        'redirect': '/VerifiedPage'
    })

if __name__ == '__main__':
    app.run(debug=True)
