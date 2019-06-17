import responses

from call import call_api


@responses.activate
def test_call_api_500():
    url = 'http://globomantics.com/api'
    responses.add(responses.GET, url, status=500)
    result = call_api(url)
    assert result is False


@responses.activate
def test_call_api_200():
    url = 'http://globomantics.com/api'
    responses.add(responses.GET, url, status=200)
    result = call_api(url)
    assert result is True


@responses.activate
def test_call_api_404():
    url = 'http://globomantics.com/api'
    responses.add(responses.GET, url, status=404)
    result = call_api(url)
    assert result is False

