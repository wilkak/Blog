
from flask import Flask
app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'dfgehgedhfghdg'
DATABASE = 'database.db'
import FlaskWebProject1.views
