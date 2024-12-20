from flask import Flask

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def home():
    return 'Welcome to the Health Advice API!'

if __name__ == '__main__':
    app.run(debug=True)
