from nlp_helpers import *
from flask import Flask, request

# Google Cloud imports
from google.cloud import firestore


# Firestore imports
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

###############################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
# cred = credentials.Certificate('path/to/serviceAccount.json')
# firebase_admin.initialize_app(cred)

# db = firestore.client()

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })

# users_ref = db.collection(u'users')
# docs = users_ref.stream()
# print("HELLO", flush=True)
# for doc in docs:
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))
###############################################

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

@app.route("/get_emotion_trend", methods=["GET"])
def get_emotion_trend():
    """Return True if user's emotional state is better than before. Else, return False.
    """

    prev_state_score = float(request.args.get("prev_state_score"))
    curr_state_score = float(request.args.get("curr_state_score"))

    # calculate trend
    if curr_state_score - prev_state_score > 0:
        trend = True
    else:
        trend = False

    response = {
        "trend": trend
    }
    return response


# def quickstart_add_data_one():
#     db = firestore.Client()

#     doc_ref = db.collection(u'users').document(u'alovelace')
#     doc_ref.set({
#         u'first': u'Ada',
#         u'last': u'Lovelace',
#         u'born': 1815
#     })


# if __name__ == "__main__":
    
    # # Use the application default credentials
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(cred, {
    # 'projectId': project_id,
    # })

    # # Project ID is determined by the GCLOUD_PROJECT environment variable
    # db = firestore.Client()
    # doc_ref = db.collection(u'users').document(u'alovelace')
    # doc_ref.set({
    #     u'first': u'Ada',
    #     u'last': u'Lovelace',
    #     u'born': 1815
    # })

    # doc_ref = db.collection(u'users').document(u'aturing')
    # doc_ref.set({
    #     u'first': u'Alan',
    #     u'middle': u'Mathison',
    #     u'last': u'Turing',
    #     u'born': 1912
    # })

    # users_ref = db.collection(u'users')
    # docs = users_ref.stream()
    # print("HELLO")
    # for doc in docs:
    #     print(u'{} => {}'.format(doc.id, doc.to_dict()))