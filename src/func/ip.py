
import requests
def get_ip()->str:
    return requests.get('https://checkip.amazonaws.com').text.strip()
    
