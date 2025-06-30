from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from frontend

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    return jsonify({
        'message': f'Received: {first_name} {last_name}'
    })

if __name__ == '__main__':
    app.run(port=5000)
