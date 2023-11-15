from key import key
import requests

def get_weather_data(city):
   
    apiKey = key 
    querystring = {"q":city}

    url = f'https://weatherapi-com.p.rapidapi.com/current.json'
    headers = {
	"X-RapidAPI-Key": apiKey, 
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
    response =  requests.get(url, headers=headers,params=querystring)

    if response.status_code == 200:
        return response.json()
    return None