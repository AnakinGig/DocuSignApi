from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from .docusign_api import docusign_bp
from .swagger_setup import init_swagger
import os

def create_app():
  app = Flask(__name__)

  app.config["INTERNAL_API_BASE_URL"] = os.environ.get("INTERNAL_API_BASE_URL", "http://localhost:5001")
  app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB
  
  app.register_blueprint(docusign_bp, url_prefix="/api")
  init_swagger(app)
  
  @app.route('/')
  def helloWord():
    return "Hello World!\n", 200

  return app