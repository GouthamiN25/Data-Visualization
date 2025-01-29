import folium
import requests

# OpenWeather API Key
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

# Define locations with coordinates
locations = [
    {"name": "New York, NY", "lat": 40.7128, "lon": -74.0060},
    {"name": "Los Angeles, CA", "lat": 34.0522, "lon": -118.2437},
    {"name": "Chicago, IL", "lat": 41.8781, "lon": -87.6298},
    {"name": "Houston, TX", "lat": 29.7604, "lon": -95.3698},
    {"name": "San Francisco, CA", "lat": 37.7749, "lon": -122.4194}
]

# Create a map centered at USA
usa_map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Function to fetch weather data
def get_weather(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        return f"🌡️ Temp: {temperature}°C, {weather_desc}"
    return "Weather data unavailable"

# Add markers with weather info
for location in locations:
    weather_info = get_weather(location["lat"], location["lon"])
    folium.Marker(
        location=[location["lat"], location["lon"]],
        popup=f"{location['name']}<br>{weather_info}",
        tooltip=location["name"],
        icon=folium.Icon(color="blue", icon="cloud")
    ).add_to(usa_map)

# Save the map
usa_map.save("usa_map_weather.html")
print("Map saved as 'usa_map_weather.html'. Open it in your browser.")
