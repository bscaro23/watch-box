import requests
from django.conf import settings

def search_film(title):
    """
    Searches for a film using the OMDB API.
    
    :param title: The movie title.
    :return: JSON response with movie details or an error.
    """
    base_url = "http://www.omdbapi.com/"
    api_key = settings.OMDB_API_KEY  # Store API key in settings.py

    params = {"t": title, "apikey": api_key}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data.get("Response") == "True":
            return data 
        else:
            return None  
    
    except requests.exceptions.RequestException as e:
        return None 

