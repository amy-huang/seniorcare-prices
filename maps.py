import googlemaps
import time
from dotenv import load_dotenv
import os
load_dotenv()  # Load variables from .env file

# Replace with your actual API key
API_KEY = os.getenv('MAPS_API_KEY')

# Initialize the client
gmaps = googlemaps.Client(key=API_KEY)

# Define the search parameters
query = "assisted living"
location = "98103"  # Seattle ZIP code
radius = 5 * 1609.34  # 5 miles in meters

# Perform a text search
places_result = gmaps.places(query=query, location=location, radius=radius)

# Function to retrieve all pages of results
def get_all_places(results):
    places = results['results']
    while 'next_page_token' in results:
        next_page_token = results['next_page_token']
        # Wait for the next page token to become valid
        time.sleep(2)
        results = gmaps.places(query=query, location=location, radius=radius, page_token=next_page_token)
        places.extend(results['results'])
    return places

# Get all places
all_places = get_all_places(places_result)

# Print the names and addresses of the facilities
for place in all_places:
    name = place['name']
    address = place['formatted_address']
    print(f"Name: {name}, Address: {address}")

# If you want to save the results to a file
with open('assisted_living_facilities.txt', 'w') as file:
    for place in all_places:
        name = place['name']
        address = place['formatted_address']
        file.write(f"Name: {name}, Address: {address}\n")
