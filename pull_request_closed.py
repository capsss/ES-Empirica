import requests

url_api = 'https://api.github.com/'
url_puls = 'repos/jquery/jquery/pulls'


class closed:
    def requisitar():
        response = requests.get(url_api + url_puls + '?state=closed')
        r = response.json()

        textos = []
        ids = []
        for item in r:
            textos.append(item["body"])
            ids.append(item['number'])
        return textos, ids

