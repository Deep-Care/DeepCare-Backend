from nlp_helpers import *
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    
    return "Welcome to DeepFace"

@app.route("/get_text_sentiment_score", methods=["GET"])
def get_text_sentiment_score():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'text_sample',
        help='The text sample you\'d like to analyze.')
    args = parser.parse_args()

    score = analyze(args.text_sample)
    response = {
        "score": score
    }
    return response
