from google.protobuf.json_format import MessageToDict, MessageToJson
import json

# Google Cloud imports
import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(text_sample):
    """Run a sentiment analysis request on a text sample."""
    client = language.LanguageServiceClient()
    # text_sample = "I want to kill everyone :("
    
    document = types.Document(
        content=text_sample,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    
    response_dict = MessageToDict(annotations)
    response_json_str = MessageToJson(annotations)
    response_json = json.loads(response_json_str)
    # print(response_json)
    score = response_json["documentSentiment"]["score"]

    return score

def get_text_sentiment_score(text_sample):
    score = analyze(text_sample)
    return score