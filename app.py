from nlp_helpers import *
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    
    return "Welcome to DeepFace"

@app.route("/get_sentiment_score", methods=["GET"])
def get_sentiment_score():
    """Return sentiment score (combination of text sentiment analysis and alwaysAI pose estimation)
    """

    # get arguments
    text_sample = request.args.get("text_sample")

    # get scores
    text_score = get_text_sentiment_score(text_sample)
    # pose_score = get_pose_sentiment_score()

    # combine scores
    score = text_score

    # prepare JSON response
    response = {
        "score": score
    }

    return response

# @app.route("/get_text_sentiment_score", methods=["GET"])
# def get_text_sentiment_score():
#     parser = argparse.ArgumentParser(
#         description=__doc__,
#         formatter_class=argparse.RawDescriptionHelpFormatter)
#     parser.add_argument(
#         'text_sample',
#         help='The text sample you\'d like to analyze.')
#     args = parser.parse_args()

#     score = analyze(args.text_sample)
#     response = {
#         "score": score
#     }
#     return response
