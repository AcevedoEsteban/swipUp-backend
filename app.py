from flask import Flask
# routes
from routes import indexRoute
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# register the blueprints
app.register_blueprint(indexRoute)

if __name__ == "__main__":
    app.run(debug=True)
