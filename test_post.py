import requests

# Define the URL for the POST request
url = 'https://httpbin.org/post'

# Perform the POST request
response = requests.post(url)

# Print the response in JSON format
print(response.json())
