import jwt
import json
import unittest

from django.test   import Client, TestCase
from user.models   import User, SocialPlatform
from unittest.mock import patch, MagicMock

class KakaoSignInTest(TestCase):

    def setUp(self):
        SocialPlatform.objects.create(platform_name='kakao')

    def tearDown(self):
        SocialPlatform.objects.get(platform_name='kakao').delete()        
    
    @patch('user.views.requests')
    def test_kakao_sign_in(self, mocked_request):
        c = Client()

        class FakeResponse:
            def json(self):
                return {
                    "id" : 12345,
                    "properties" : {"nickname": "test_user"},
                    "kakao_account": {"email":"test@gmail.com"}
                }

        mocked_request.get = MagicMock(return_value = FakeResponse())
        header = {'HTTP_Authorization':'fake_token.1234'}
        response = c.get('/user/kakao-login', content_type='applications/json', **header)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
