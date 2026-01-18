from flask import Flask
from flask_cors import CORS
from routes.tax import tax_bp

def create_app():
    app = Flask(__name__)

    # allow React (localhost:3000) to call Flask (localhost:8000)
    CORS(app)

    # register API routes
    app.register_blueprint(tax_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000)
