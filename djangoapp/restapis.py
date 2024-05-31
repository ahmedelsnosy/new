# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    url = backend_url + endpoint
    try:
        response = requests.get(url, params=kwargs)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during GET request to {url}: {e}")
        return None

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()  # Assuming the response is a JSON object with sentiment analysis results
    except requests.exceptions.RequestException as e:
        print(f"Error during sentiment analysis request to {request_url}: {e}")
        return None


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    url = backend_url + "insert_review"
    try:
        response = requests.post(url, json=data_dict)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request to {url}: {e}")
        return None

