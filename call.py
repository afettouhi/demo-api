import requests


def call_api(url):
    """
    Basic approach to call an api
    :param url: url of api
    :return: True if status code is 200, False otherwise
    """
    r = requests.get(url)
    if r.status_code == 200:
        return True
    return False
