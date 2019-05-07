import json
from requests.auth import HTTPDigestAuth
import requests


api_token = 'token'
api_url_base = 'https://api.digitalocean.com/v2/'
api_url = "https://jsonplaceholder.typicode.com/posts?userId=1"

#headers = {'Content-Type':'application/json', 'Authorization':'Bearer {0}'.format(api_token)}

def get_caption():
    #api_url = '{0}account'.format(api_url_base)
    response = requests.get(api_url)

    if response.status_code == 200:
        account_info =  json.loads(response.content.decode('utf-8'))
    else:
        account_info = None
    #*****************
    if account_info is not None:
        print("Here is your info: ")
        for a in account_info:
            print(a["title"])
    





