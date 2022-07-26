import requests


def get_html(url, params=None):
    r = requests.get(url, params=params)
    print(r.url)
    r.encoding = 'utf-8'
    return r
