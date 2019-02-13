import requests

# Star Wars API - Investigation (https://swapi.co)
base_url = "https://swapi.co/api/"

# 10000 API requests per day (from SWAPI docs https://swapi.co/documentation under "Rate Limiting")
# TODO: If we're hosting this as a website, we need to work around this:
# Options: 
# - Caching the data, only request every X hours
# - Since it's limited by IP Address, we can request directly to the SWAPI from the browser in Javascript

# Search API Feature
# TODO: Extra Feature: Search functionality? For the user.

# Can request the schema of any resource, TODO: what are our resources?
schema_url = "{}/schema"

# Extra Feature: Wookie Mode? Make all requests with `?format=wookiee`

# Discovery - Get the endpoints for all resources
all_resources = requests.get(base_url)

# Get All People Data
people = requests.get(all_resources.json()["people"])