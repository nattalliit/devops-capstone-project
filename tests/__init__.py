import sys
from flask import Flask
from service import config
from flask_cors import CORS
from service.common import log_handlers
from flask_talisman import Talisman

#Create Flask application
app = Flask(__name__)
app.config.from_object(config)
talisman = Talisman(app)
from flask_cors import CORS
CORS(app)
