from flask import Flask, request, jsonify
from db import save_profile

app = Flask(__name__)

@app.route('/api/profile', methods=['POST'])
def profile():
    data = request.get_json()
    save_profile(data)
    return jsonify({'message': 'Profile saved successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)
