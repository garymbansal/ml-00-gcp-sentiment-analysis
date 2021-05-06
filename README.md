# gcp-sentiment-analysis
This repository is to share code of Sentiment Analysis demonstration done on google cloud

### Account Setup
Signup on https://console.cloud.google.com with your google account for a free trial credit.

### Environment Setup
- Login with your google account on google cloud console
- Enable the Cloud Natural Language API
- Activate Cloud Shell
- Create a demo directory		 
	 - ```mkdir gcpdemo```
	 
- Create Service account 
	- ```gcloud iam service-accounts create gcpdemo-account --display-name "Demo Account"```
	
- Create authentication keys
	- ```gcloud iam service-accounts keys create gcpdemokey.json --iam-account=gcpdemo-account@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com```
		
	- Setup IAM role
    - ```gcloud projects add-iam-policy-binding $DEVSHELL_PROJECT_ID --member serviceAccount:gcpdemo-account@$DEVSHELL_PROJECT_ID.iam.gserviceaccount.com --role roles/owner```
  
  - Set environment variable for default authentication
    - ```export GOOGLE_APPLICATION_CREDENTIALS=gcpdemokey.json```
  
	### Set the code
  
	- Open nano editor
		- ```nano demo.py```
		
	- Copy/paste the code from the file code01.py
	  ```from google.cloud import language_v1
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
    ```
  - Run the file:
	  - ```python3 demo.py "I am not happy today though I love to code today."```
		
	- Make another file 
	  - ```nano sentiment_analysis.py```
	  
	- Copy/paste the code from the file code02.py
    ```
    import argparse

    from google.cloud import language_v1



    def print_result(annotations):
        score = annotations.document_sentiment.score
        magnitude = annotations.document_sentiment.magnitude

        for index, sentence in enumerate(annotations.sentences):
            sentence_sentiment = sentence.sentiment.score
            print(
                "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
            )

        print(
            "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
        )
        return 0




    def analyze(movie_review_filename):
        """Run a sentiment analysis request on text within a passed filename."""
        client = language_v1.LanguageServiceClient()

        with open(movie_review_filename, "r") as review_file:
            # Instantiates a plain text document.
            content = review_file.read()

        document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
        annotations = client.analyze_sentiment(request={'document': document})

        # Print the results
        print_result(annotations)




    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument(
            "movie_review_filename",
            help="The filename of the movie review you'd like to analyze.",
        )
        args = parser.parse_args()

        analyze(args.movie_review_filename)
    ```
	- Download the samples from Google Cloud Storage
    - ```gsutil cp gs://cloud-samples-tests/natural-language/sentiment-samples.tgz .```
		
	- Unzip those samples, which will create a "reviews" folder
		- ```gunzip sentiment-samples.tgz```
		- ```tar -xvf sentiment-samples.tar```
	- Run the code 
		- ```python3 sentiment_analysis.py reviews/bladerunner-pos.txt```
