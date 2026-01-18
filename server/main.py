from flask import Flask
from routes.tax import tax_bp
import os

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, "templates"),
        static_folder=os.path.join(base_dir, "static")
    )

    app.config["SECRET_KEY"] = "1234"

    app.register_blueprint(tax_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=8000)
