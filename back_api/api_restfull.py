from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_api import get_current_weather, get_hourly_forecast, get_daily_forecast, weather_data_model

api_key = 'a1b1045de421855d4d44bb2b53d4da8f'

app = Flask(__name__)
CORS(app)

@app.route('/current_weather')
def current_weather():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_current_weather(lat, lon, api_key)
    return jsonify(data)

@app.route('/hourly_forecast')
def hourly_forecast():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_hourly_forecast(lat, lon, api_key)
    return jsonify(data)

@app.route('/daily_forecast')
def daily_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_daily_forecast(lat, lon, api_key)
    return jsonify(data)

@app.route('/complete_weather')
def complete_weather():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    current_weather_data = get_current_weather(lat, lon, api_key)
    hourly_forecast_data = get_hourly_forecast(lat, lon, api_key)
    daily_forecast_data = get_daily_forecast(lat, lon, api_key)
    model_data = weather_data_model(lat, lon, api_key)
    return jsonify({
        "current_weather": current_weather_data,
        "hourly_forecast": hourly_forecast_data,
        "daily_forecast": daily_forecast_data,
        "model_data": model_data
    })

if __name__ == '__main__':
    app.run(debug=True)