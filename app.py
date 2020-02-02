from flask import Flask
from speech_to_text import *
app = Flask(__name__)

@app.route("/")
def hello():

    return "Hello Chuthyias"
