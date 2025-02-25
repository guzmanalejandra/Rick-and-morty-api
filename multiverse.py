import requests
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import random

# Function to get all locations from the Rick and Morty API
def get_locations():
    locations = []
    url = "https://rickandmortyapi.com/api/location"

    while url:
        response = requests.get(url)
        data = response.json()
        locations.extend(data['results'])
        url = data['info']['next']

    return locations

# Function to get characters from a location
def get_characters(character_urls):
    characters = []
    for url in character_urls:
        response = requests.get(url)
        if response.status_code == 200:
            character_data = response.json()
            characters.append(character_data['name'])
    return characters

# Generate fictional coordinates for the locations
def assign_fictional_coordinates(locations):
    for location in locations:
        location['latitude'] = random.uniform(-90, 90)
        location['longitude'] = random.uniform(-180, 180)
    return locations

# Create a dynamic map with the locations and characters
def create_map(locations):
    map_center = [0, 0]
    multiverse_map = folium.Map(location=map_center, zoom_start=2)
    marker_cluster = MarkerCluster().add_to(multiverse_map)

    for location in locations:
        characters = get_characters(location['residents'])
        popup_content = f"<strong>{location['name']}</strong><br>Type: {location['type']}<br>Dimension: {location['dimension']}<br>Characters: {', '.join(characters) if characters else 'None'}"
        folium.Marker(
            location=[location['latitude'], location['longitude']],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    return multiverse_map

# Main execution
if __name__ == "__main__":
    print("Fetching locations...")
    locations = get_locations()
    print(f"Fetched {len(locations)} locations.")

    print("Assigning fictional coordinates...")
    locations_with_coords = assign_fictional_coordinates(locations)

    print("Creating the map...")
    multiverse_map = create_map(locations_with_coords)

    # Save the map to an HTML file
    multiverse_map.save("multiverse_map.html")
    print("Map has been saved as 'multiverse_map.html'.")
