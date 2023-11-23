from flask import Flask

app = Flask(__name__)

# Configuration settings, database connections, and other setup can be done here.

# Import your routes
from app.routes.task_routes import *

if __name__ == "__main__":
    # Run the application
    app.run(debug=True)
