from unittest import TestCase

import responses

from call import call_api


class TestCallApi(TestCase):
    @responses.activate
    def test_call_api_500(self):
        url = 'http://globomantics.com/api'
        responses.add(responses.GET, url, status=500)
        result = call_api(url)
        self.assertFalse(result)

    @responses.activate
    def test_call_api_200(self):
        url = 'http://globomantics.com/api'
        responses.add(responses.GET, url, status=200)
        result = call_api(url)
        self.assertTrue(result)
