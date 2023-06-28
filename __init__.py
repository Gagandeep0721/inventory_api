from flask import Flask
from config import Config
from .site.routes import site


app = Flask(__name__) #simple route on the homepage
#@app.route("/")
#def hello_world():
 #   return "<p>Hello, World!</p>"

app.register_blueprint(site)

app.config.from_object(Config)