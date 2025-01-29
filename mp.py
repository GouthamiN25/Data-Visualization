GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# Function to fetch traffic data
def get_traffic(lat, lon):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={lat},{lon}&destination={lat},{lon}&traffic_model=best_guess&departure_time=now&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if "routes" in data and len(data["routes"]) > 0:
        congestion_level = data["routes"][0]["legs"][0]["duration_in_traffic"]["text"]
        return f"🚗 Traffic: {congestion_level}"
    return "Traffic data unavailable"
