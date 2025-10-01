import requests

def obtener_chiste(idioma: str) -> dict:
    """
    Gets a joke from the JokeAPI.
    
    Parameters:
        idioma (str): Language code ("es" for Spanish, "en" for English).
    
    Returns:
        dict: JSON response containing the joke, 
              or None if the request fails.
    """
    # Base URL of the JokeAPI
    url = "https://v2.jokeapi.dev/joke/Any"
    
    # Parameters for the API request
    # "lang" specifies the language of the joke
    # "type=twopart" means we request jokes with "setup" and "delivery" parts
    params = {
        "lang": idioma,
        "type": "twopart"
    }
    
    # Send a GET request to the API with the parameters
    response = requests.get(url, params=params)
    
    # If the response is successful (status 200), return the JSON data
    # Otherwise, return None to indicate failure
    return response.json() if response.status_code == 200 else None
