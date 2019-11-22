import jwt
import json
import requests

from django.views import View
from django.http  import JsonResponse

from .models            import SocialPlatform, User
from wemarpple.settings import SECRET_KEY

class KakaoLoginView(View):

    def get(self, request):
        try:
            access_token = request.headers.get('Authorization', None)
            url          = 'https://kapi.kakao.com/v2/user/me'
            headers      = {
                            'Authorization': f'Bearer {access_token}',
                            'Content-type' : 'application/x-www-form-urlencoded; charset=utf-8'
                           }
            
            kakao_response = requests.get(url, headers = headers)
            kakao_response = kakao_response.json()
            kakao          = SocialPlatform.objects.get(platform_name='kakao')
            
            if User.objects.filter(social_platform = kakao, platform_id = kakao_response['id']).exists():

                user      = User.objects.get(social_platform = kakao, platform_id = kakao_response['id'])
                jwt_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                
                return JsonResponse(
                                {
                                    'id'       : f'{user.id}',
                                    'name'     : f'{user.name}',
                                    'jwt_token': f'{jwt_token}',
                                },status = 200)

            user = User.objects.create(
                                    platform_id     = kakao_response['id'],
                                    name            = kakao_response['properties']['nickname'],
                                    social_platform = kakao,
                                    email           = kakao_response['kakao_account'].get('email', None)
                                    )
           
            jwt_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')

            return JsonResponse(
                            {
                                'id'        : f'{user.id}',
                                'name'      : f'{user.name}',
                                'jwt_token' : f'{jwt_token}',
                            }, status = 200)
        except KeyError:
            return JsonResponse({'message':'WRONG_KEY'}, status = 400)
