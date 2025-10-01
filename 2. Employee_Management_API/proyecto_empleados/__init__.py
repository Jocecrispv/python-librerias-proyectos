# Import Flask framework
from flask import Flask
# Import the blueprint we defined for employee-related routes
from .routes import empleados_bp

# Factory function to create the Flask app
def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Register the "empleados" blueprint
    # All routes inside "empleados_bp" will be accessible under the "/api" prefix
    app.register_blueprint(empleados_bp, url_prefix='/api')

    # Return the configured Flask application
    return app
