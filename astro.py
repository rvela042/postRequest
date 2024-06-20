import requests

# URL for the API request
url = 'http://api.open-notify.org/astros.json'

# Sending the GET request to the URL
response = requests.get(url)

# Printing the status code of the response
print(response.status_code)

# Parsing the JSON response to extract the list of people
data = response.json()
people = data['people']

# Printing the names of the first five astronauts in the list
for person in people[:5]:
    print(person['name'])
