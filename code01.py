from google.cloud import language_v1
import sys

def print_result(annotations):
    score = annotations.document_sentiment.score

def analyze(mytext):    
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=mytext, type_=language_v1.Document.Type.PLAIN_TEXT)
    mysentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
    
    print("Sentiment score: {}".format(mysentiment.score))

if __name__ == "__main__":
    analyze(sys.argv[1])
