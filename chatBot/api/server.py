from flask import Flask, request

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json  # Parse JSON data from the request
    user_message = data.get("message", "")
    print(f"User said: {user_message}")  # Print the message to the console
    return '', 204  # Return a 204 No Content response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on localhost:5000
