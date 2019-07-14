import requests
from auth import c_id, token

# url_api = 'https://api.github.com/'
# url_puls = 'repos/jquery/jquery/pulls/'

url_api = 'https://api.github.com/'
url_puls = 'repos/jquery/jquery/pulls/'

# url_api = 'https://api.github.com/'
# url_puls = 'repos/angular/angular.js/pulls/'

numero_pull = '3501'

class especifico:
    def requisitar(n_pull = numero_pull):
        response = requests.get(url_api + url_puls + n_pull + '?client_id=' + c_id + '&client_secret=' + token)
        if response.status_code > 210:
            r = False
        else:
            r = response.json()
        return r