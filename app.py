from flask import Flask
from config import DevelopmentConfig  # or TestingConfig / ProductionConfig based on your needs

app = Flask(__name__)  # Initialize Flask app
app.config.from_object(DevelopmentConfig)  # Load configuration from the DevelopmentConfig class

@app.route('/')
def home():
    return f"Running in {app.config['DEBUG']} mode!"  # Output the current mode (True for Development)

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
