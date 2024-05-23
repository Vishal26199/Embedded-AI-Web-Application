
import requests

def sentiment_analyzer(text_to_analyse):

    """
    this function is to analyze text for sentiment analysis
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post( url, json = myobj, headers = header )

    return response.text