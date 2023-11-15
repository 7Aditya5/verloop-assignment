from flask import jsonify

def format_json_response(data):


    filtered_data = {
        "Weather":str(int(data["current"]["temp_c"]))+" C",
        "Latitude":str(data["location"]["lat"]),
        "Longitude":str(data["location"]["lon"]),
        "City": data["location"]["name"]+" "+data["location"]["country"]
	}
    return jsonify(filtered_data)