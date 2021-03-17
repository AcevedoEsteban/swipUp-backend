from flask import Flask
# routes

from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# register the blueprints

if __name__ == "__main__":
    app.run(debug=True)
