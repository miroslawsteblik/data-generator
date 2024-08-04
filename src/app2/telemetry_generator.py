import logging
import random
import time
import requests

logging.basicConfig(level=logging.DEBUG)

def generate_telemetry_data():
    """Generate random telemetry data."""
    data = {
        'timestamp': time.time(),
        'ambient_temperature_celsius': random.uniform(20.0, 30.0),
        'pressure_atm': random.uniform(1.0, 2.0),
        'ambient_humidity_percent': random.uniform(30.0, 50.0),
        'vehicle_speed_kph': random.uniform(0, 120),
        'fuel_level_percent': random.uniform(0, 100),
        'engine_temperature_celsius': random.uniform(70, 100),
        'gps_coordinates': {
            'latitude': random.uniform(-90.0, 90.0),
            'longitude': random.uniform(-180.0, 180.0)
        },
        'battery_voltage': random.uniform(11.0, 13.0)
    }
    logging.debug(f"Generated telemetry data: {data}")
    return data

def populate_telemetry_data():
    """Populate telemetry data at regular intervals."""
    while True:
        data = generate_telemetry_data()
        try:
            response = requests.post('http://flask_server:5000/api/telemetry', json=data)
            logging.debug(f"Generated telemetry data: {data}, Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error sending telemetry data: {e}")
        time.sleep(30)

if __name__ == '__main__':
    populate_telemetry_data()