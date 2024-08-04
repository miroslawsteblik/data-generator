import logging
from flask import Flask, render_template, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


# List to store telemetry data
telemetry_data_list = []

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/api/telemetry', methods=['GET', 'POST'])
def api_telemetry():
    if request.method == 'GET':
        return jsonify(telemetry_data_list), 200
    elif request.method == 'POST':
        telemetry_data = request.get_json()
        if not telemetry_data:
            return jsonify({"error": "No data provided."}), 400
        telemetry_data_list.append(telemetry_data)
        return jsonify({'status': 'Telemetry data created'}), 200

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Telemetry Server API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)



# http://localhost:5000
# http://127.0.0.1:5000/api/telemetry
# http://localhost:5000/swagger
