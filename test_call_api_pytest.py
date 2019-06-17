import responses

from call import call_api


@responses.activate
def test_call_api_500():
    url = 'http://globomantics.com/api'
    responses.add(responses.GET, url, status=500)
    result = call_api(url)
    assert result is False
