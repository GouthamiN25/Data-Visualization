import folium

# Define a list of locations (Name, Latitude, Longitude)
locations = [
    {"name": "New York, NY", "lat": 40.7128, "lon": -74.0060},
    {"name": "Los Angeles, CA", "lat": 34.0522, "lon": -118.2437},
    {"name": "Chicago, IL", "lat": 41.8781, "lon": -87.6298},
    {"name": "Houston, TX", "lat": 29.7604, "lon": -95.3698},
    {"name": "San Francisco, CA", "lat": 37.7749, "lon": -122.4194}
]

# Create a map centered at an average location
usa_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add each location to the map
for location in locations:
    folium.Marker(
        location=[location["lat"], location["lon"]],
        popup=location["name"],
        tooltip=location["name"]
    ).add_to(usa_map)

# Save the map to an HTML file
usa_map.save("usa_map.html")
print("Map has been saved as 'usa_map.html'. Open this file in your browser to view the map.")
