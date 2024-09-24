# Navigation App

A Flask-based web application that provides directions using the Google Maps API. Users can input their starting point and destination to receive a detailed route on a map.

## Features

- User-friendly interface for inputting start and end locations.
- Autocomplete functionality for locations using Google Places API.
- Displays the driving route on an interactive map.

## Technologies Used

- Flask
- Google Maps API
- Docker
- HTML, CSS, JavaScript

## Side Note
If you run the app with Docker, first build the dockerfile with "docker build -t image_name ." and run it with "docker run -p 5000:5000 --env-file .env image_name". 
The app will only be accessible on http://localhost:5000/. Use http://127.0.0.1:5000/ if you do not use Docker.
