Main entry point for Google Cloud App Engine
This file is required for App Engine to recognize the application
"""

from flask_app import app

if __name__ == '__main__':
    app.run()
