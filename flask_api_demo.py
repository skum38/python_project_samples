from flask import Flask, jsonify
import requests



app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_bangalore_weather():
    try:
        # Using Open-Meteo free API (no API key required)
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 12.9716,
            "longitude": 77.5946,
            "current": "temperature_2m,weather_code,wind_speed_10m",
            "timezone": "Asia/Kolkata"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather_data = {
            "city": "Bangalore",
            "temperature": data["current"]["temperature_2m"],
            "weather_code": data["current"]["weather_code"],
            "wind_speed": data["current"]["wind_speed_10m"],
            "timezone": data["timezone"]
        }
        
        return jsonify(weather_data), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Use /weather endpoint to get Bangalore weather"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)