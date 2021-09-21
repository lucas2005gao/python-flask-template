from flask import Flask, render_template
from flask_cors import CORS
from routes.api import api_blueprint

app = Flask(__name__)
CORS(app)

# Registering routes
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()

