import requests

# Define the URL for the sentiment analysis API
url = 'http://text-processing.com/api/sentiment/'

# Get text input from the user
text = input("Enter text for sentiment analysis: ")

# Create the data dictionary to send with the POST request
myobj = {'text': text}

# Perform the POST request
response = requests.post(url, data=myobj)

# Print the response in JSON format
print(response.json())
