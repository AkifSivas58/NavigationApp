from flask import Flask, request, render_template
from dotenv import dotenv_values
import requests

app = Flask(__name__)

env_vars = dotenv_values()
GOOGLE_MAPS_API_KEY = env_vars.get("GOOGLE_MAPS_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/route', methods=['POST'])
def get_route():
    start = request.form['start']
    end = request.form['end']
    
    response = requests.get(
        'https://maps.googleapis.com/maps/api/directions/json',
        params={
            'origin': start,
            'destination': end,
            'key': GOOGLE_MAPS_API_KEY
        }
    )
    directions = response.json()
    return render_template('index.html', directions=directions, api_key=GOOGLE_MAPS_API_KEY)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
