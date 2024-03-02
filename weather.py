import requests
from requests.exceptions import RequestException
from time import sleep

# Function to fetch weather forecast from OpenWeatherMap API with error handling and retry mechanism
def get_weather_forecast(api_key, lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,current&appid={api_key}&units=metric"
    max_retries = 1
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise error for non-200 status codes
            data = response.json()
            return data
        except RequestException as e:
            print(f"Error fetching weather data: {e}")
            retries += 1
            print(f"Retrying ({retries}/{max_retries})...")
            sleep(2 ** retries)  # Exponential backoff for retry delay

    print("Failed to retrieve weather forecast data. Please check your API key and coordinates.")
    return None

# Function to analyze weather forecast and provide recommendations
def analyze_weather_forecast(weather_data):
    if weather_data:
        # Sample recommendation: Check for rain forecast in the next 3 days
        rainy_days = sum(1 for day in weather_data.get("daily", [])[:3] if "rain" in day.get("weather", []))
        if rainy_days > 0:
            print(f"Attention: {rainy_days} days of rain forecasted in the next 3 days. Consider adjusting irrigation schedule.")
        else:
            print("No rain forecasted in the next 3 days.")
    else:
        print("Weather forecast data not available.")

# Main function
def main():
    # OpenWeatherMap API key (replace with your own API key)
    api_key = "0552d7afc32073a0a66c195e55019e1b"

    # Coordinates of the farm location (replace with actual coordinates)
    lat = 33.1
    lon = 34.0

    # Fetch weather forecast with error handling and retry mechanism
    weather_data = get_weather_forecast(api_key, lat, lon)
    analyze_weather_forecast(weather_data)

if __name__ == "__main__":
    main()
