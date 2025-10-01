# Import the application factory from your project package
from proyecto_empleados import create_app

# Create the Flask app using the factory function
app = create_app()

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Start the Flask development server with debug mode enabled
    # Debug mode reloads the server automatically on code changes and shows detailed errors
    app.run(debug=True)
