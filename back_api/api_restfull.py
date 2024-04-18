from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
from urllib.parse import unquote
from weather_api import get_current_weather, get_hourly_forecast, get_daily_forecast, weather_data_model
from model_api import run_model

#SI ERREUR VOICI LE COMMANDE : pip install scikit-learn==1.2.2 
api_key = 'a1b1045de421855d4d44bb2b53d4da8f'

app = Flask(__name__)
#Allow all link CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/current_weather')
def current_weather():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_current_weather(lat, lon, api_key)
    return jsonify(data)

@app.route('/api/hourly_forecast')
def hourly_forecast():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_hourly_forecast(lat, lon, api_key)
    return jsonify(data)

@app.route('/api/daily_forecast')
def daily_forecast():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    data = get_daily_forecast(lat, lon, api_key)
    return jsonify(data)

@app.route('/api/complete_weather')
def complete_weather():
    global api_key
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if lat is None or lon is None:
        return jsonify({"error": "Les paramètres de latitude (lat) et de longitude (lon) doivent être fournis."}), 400
    current_weather_data = get_current_weather(lat, lon, api_key)
    hourly_forecast_data = get_hourly_forecast(lat, lon, api_key)
    daily_forecast_data = get_daily_forecast(lat, lon, api_key)
    model_response = run_model(weather_data_model(lat, lon, api_key))
    return jsonify({
        "current_weather": current_weather_data,
        "hourly_forecast": hourly_forecast_data,
        "daily_forecast": daily_forecast_data,
        "model_response": model_response
    })


@app.route('/api/universities')
def get_universities():
    db = os.getcwd() + '\\back_api\\campus.sqlite'
    if os.path.exists(db):
        conn = sqlite3.connect(db)
        cursor = conn.cursor()

        try:
            # Retrieve data from SQLite database
            cursor.execute("SELECT * FROM Universite")
            universities = cursor.fetchall()

            conn.close()

            # Convert data to JSON format
            university_list = []
            for university in universities:
                university_dict = {
                    'id': university[0],
                    'name': university[1],
                    # Add other fields as needed
                }
                university_list.append(university_dict)

            return jsonify(university_list)

        except sqlite3.Error as e:
            return jsonify({'error': str(e)}), 500
        
    else:
        return jsonify({'error': "nul"}), 500

@app.route('/api/implantations', methods=['GET'])
def get_implantations():
    db = os.getcwd() + '\\back_api\\campus.sqlite'
    if os.path.exists(db):
        try:
            # Extract the etablissement_siege from the request query
            etablissement_siege = request.args.get('etablissement_siege')

            # Check if the etablissement_siege parameter is provided
            if not etablissement_siege:
                return jsonify({'error': 'Etablissement_siege parameter is missing'}), 400

            
            # Connect to SQLite database
            conn = sqlite3.connect(db)
            cursor = conn.cursor()

            # Construct the SQL query to fetch the code_universite based on the provided etablissement_siege
            query_get_code_universite = f"""
                SELECT code_universite
                FROM Universite
                WHERE etablissement_siege = \'{etablissement_siege}\'
            """

            cursor.execute(query_get_code_universite)
            universities = cursor.fetchall()

            # Close database connection
            conn.close()

            code_universite = universities[0][0] if universities else None

            # If code_universite is not found, return an empty array
            if not code_universite:
                return jsonify([])

            # Connect to SQLite database again
            conn = sqlite3.connect(db)
            cursor = conn.cursor()

            # Construct the SQL query to fetch implantations based on the code_universite
            query_get_implantations = f"""
                SELECT *
                FROM Implantations
                WHERE code_universite = '{code_universite}'
            """

            cursor.execute(query_get_implantations)
            implantations = cursor.fetchall()

            campus_list = []
            for campus in implantations:
                campus_dict = {
                    'nom': campus[0],
                    'latitude': campus[1],
                    'longitude': campus[2],
                    'id_campus': campus[3],
                    'id_universite': campus[4],
                }
                campus_list.append(campus_dict)
            
            conn.close()

            return jsonify(campus_list)

        except Exception as e:
            print(f"Error fetching implantations: {e}")
            return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/campus_localisation', methods=['GET'])
def get_campus_localisation():
    db = os.getcwd() + '\\back_api\\campus.sqlite'
    if os.path.exists(db):
        try:
            # Extract the etablissement_siege from the request query
            campus = request.args.get('campus')
            campus = unquote(campus)

            # Check if the etablissement_siege parameter is provided
            if not campus:
                return jsonify({'error': 'Campus parameter is missing'}), 400

            
            # Connect to SQLite database
            conn = sqlite3.connect(db)
            cursor = conn.cursor()

            query_get_localisation = f"SELECT latitude,longitude FROM Implantations WHERE nom_implantation=\"{campus}\""

            print(query_get_localisation)


            cursor.execute(query_get_localisation)
            localisation_campus = cursor.fetchall()

            campus_list = []
            for campus in localisation_campus:
                campus_dict = {
                    'latitude': campus[0],
                    'longitude': campus[1],
                }
                campus_list.append(campus_dict)

            # Close database connection
            conn.close()

            return jsonify(campus_list)

        except Exception as e:
            # Handle any errors
            print(f"Error fetching implantations: {e}")
            return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True)