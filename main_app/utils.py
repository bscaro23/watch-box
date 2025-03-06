import requests
from django.conf import settings

def search_film(title=None, imdb_id=None, year=None):
    """
    Searches for a film or TV show using the OMDB API.

    :param title: The movie or TV show title (optional).
    :param imdb_id: The IMDb ID (optional).
    :param year: The release year (optional).
    :return: JSON response with movie details or an error message.
    """
    base_url = "http://www.omdbapi.com/?"
    api_key = getattr(settings, "OMDB_API_KEY", None)  

    if not api_key:
        return {"error": "OMDB API Key is missing. Check your settings."}

    if not title and not imdb_id:
        return {"error": "Please provide a title or IMDb ID."}

   
    url = f"{base_url}"
    if imdb_id:
        url += f"i={imdb_id}"
    elif title:
        url += f"t={title}"
        if year:
            url += f"&y={year}"
    url += f"&apikey={api_key}"
    

    try:
        response = requests.get(url)  
        response.raise_for_status()  

        data = response.json()
        if data.get("Response") == "True":
            return data  
        else:
            return {"error": data.get("Error", "Movie/TV show not found")}

    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}


