import requests

# URL for the Coindesk API to get current Bitcoin price
url = "https://api.coindesk.com/v1/bpi/currentprice.json"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the JSON data
    print(data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
