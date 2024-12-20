from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask app!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Run the app on port 5001