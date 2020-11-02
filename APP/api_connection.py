import requests

def get_response(**dict):

    url = dict.get("url")
    host = dict.get("host")
    key = dict.get("key")
    querystring = dict.get("querystring")

    headers = {
        'x-rapidapi-host': host,
        'x-rapidapi-key': key
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response