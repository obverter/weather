import requests

# Make a GET request to the Tempest API endpoint for your station
response = requests.get("https://api.tempestwx.com/v2/station/92258/")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    weather_data = response.json()

    # Print the current temperature
    print("Temperature:", weather_data["temperature"])
else:
    # Print an error message if the request was not successful
    print("Request failed with status code:", response.status_code)
