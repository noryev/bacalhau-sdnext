from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SDNEXT_URL = "http://localhost:7860"  # Adjust if your SDNext is running on a different port

@app.route('/process', methods=['POST'])
def process_image():
    data = request.json
    # Forward the request to SDNext
    response = requests.post(f"{SDNEXT_URL}/api/predict", json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)