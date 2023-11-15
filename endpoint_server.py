from flask import Flask, request, jsonify, make_response
from get_weather_data import get_weather_data
from format_json_response import format_json_response
from format_xml_response import format_xml_response

app = Flask(__name__)


@app.route('/getCurrentWeather', methods=['POST'])
def get_current_weather():
    request_data = request.get_json()
    if not request_data:
        return make_response(jsonify({'error': 'Missing required fields in the request body.'}), 400)
    city = request_data.get('city')
    output_format = request_data.get('output_format')
      
    weather_data = get_weather_data(city)
    if not weather_data:
        return make_response(jsonify({'error': 'Unable to fetch weather data.'}), 500)
    if output_format == 'json':
        response_data = format_json_response(weather_data)
        return make_response(response_data, 200)
    elif output_format == 'xml':
        response_data = format_xml_response(weather_data)
        return make_response(response_data, 200)
    else:
        return make_response(jsonify({'error': 'Invalid output format specified.'}), 400)


if __name__ == '__main__':
    app.run(debug=True)

