from ast import Pass
import json
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from recom.aa import check_password
from .models import Movie2,User,Favorite
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import AddFavoriteSerializer, MovieInfoSerializer, MovieSearchSerializer, MovieSerializer, UserId, UserloginSerializer
from rest_framework.response import Response

from django.core.validators import validate_email
from django.core.exceptions  import ValidationError

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


import jwt

from django.db.utils import IntegrityError

from django.db.models import FilteredRelation

from django.db.models import F
# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        data = json.loads(request.body)
        
        try:
            validate_email(data['email'])
        
        except ValidationError:
            return Response({'error':'이메일 주소가 잘못되었습니다.'},status=400)
        
        if len(data['password']) < 4 or len(data['password']) > 10 :
            return Response({'error' : '비밀번호 길이를 확인하세요'},status=400)
        
        hashed_password=PasswordHasher().hash(data['password'])
        
        try:
            User.objects.create(
                email = data['email'],
                name = data['name'],
                password = hashed_password
            ).save()
        
        except IntegrityError:
            return Response({'error' : '이미 존재하는 회원입니다.'},status=400)
        
        user = User.objects.filter(email = data['email'])
        serializer=UserId(user)
        user_id = serializer.data
        
        SECRET = 'secret'
        
        access_token = jwt.encode({'id':user_id},SECRET,algorithm='HS256')
        
        return Response({'result':'회원가입 완료','access_token':access_token})
         
        
class UserLogin(APIView):
    def post(self,request):
        data = json.loads(request.body)
        
        email=data['email']
        
        user=User.objects.filter(email=email)
        serializer = UserloginSerializer(user,many=True)
        user_lg = serializer.data
        output_dict = json.loads(json.dumps(user_lg))
        
        if len(user_lg) == 0:
            return Response({'error' : '회원가입 되어있지 않은 사람입니다.'},status=400)
        
        try :
            if check_password(output_dict[0]['password'],data['password']):
                user_id=output_dict[0]['id']
        except VerifyMismatchError:
            return Response({'error':'비밀번호가 다릅니다.'},status=400)
        
        
        SECRET = 'secret'
        
        access_token = jwt.encode({'id':user_id},SECRET,algorithm='HS256')
        
        return Response({'result' : '로그인이 되었습니다.', 'access_token':access_token})
        
        

class UserLogout(APIView):
    def post(self,request):
        access_token=request.headers.get('Authorization',None)
        if access_token is not None:
            response = Response()
            
            response.delete_cookie('jwt')
            
            response.data={
                'result':'로그아웃 되었습니다.'
            }
            
            return response
        

class MovieList(APIView):
    def get(self,request):
        provider = request.GET['provider']
        
        if provider == '넷플릭스':
            movie=Movie2.objects.filter(provider='넷플릭스')
            serializer=MovieSerializer(movie,many=True)
            movie_list=serializer.data

            return Response({'count':len(movie_list),'movie_list':movie_list})
        
        elif provider == '왓챠':
            movie=Movie2.objects.filter(provider='왓챠')
            serializer=MovieSerializer(movie,many=True)
            movie_list=serializer.data

            return Response({'count':len(movie_list),'movie_list':movie_list})
        
        elif provider == '웨이브':
            movie=Movie2.objects.filter(provider='웨이브')
            serializer=MovieSerializer(movie,many=True)
            movie_list=serializer.data

            return Response({'count':len(movie_list),'movie_list':movie_list})
            
        elif provider == 'prv':
            movie=Movie2.objects.filter(provider='prv')
            serializer=MovieSerializer(movie,many=True)
            movie_list=serializer.data

            return Response({'count':len(movie_list),'movie_list':movie_list})
        
        elif provider == 'dnp':
            movie=Movie2.objects.filter(provider='dnp')
            serializer=MovieSerializer(movie,many=True)
            movie_list=serializer.data

            return Response({'count':len(movie_list),'movie_list':movie_list})

class MovieSearch(APIView):
    def get(self,request):
        offset = request.GET['offset']
        limit = request.GET['limit']
        keyword = request.GET['keyword']
        
        m_s=Movie2.objects.filter(title__icontains=keyword)[int(offset):int(limit)]
        serializer=MovieSearchSerializer(m_s,many=True)
        movie_search = serializer.data
        
        return  Response({'count':len(movie_search),'result':movie_search})

class MovieInfo(APIView):
    def get(self,request,movie_id):
        movie_info = Movie2.objects.filter(id=movie_id)
        serializer=MovieInfoSerializer(movie_info,many=True)
        movie_info_2=serializer.data[0]
        
        return JsonResponse({'영화정보':movie_info_2})

class Addfavorite(APIView):
    def post(self,request,movie_id):
        access_token=request.headers.get('Authorization',None)
        
        SECRET = 'secret'
        
        payload=jwt.decode(access_token,SECRET,algorithms='HS256')
        
        user_id=payload.get('id',None)
        
        try:
            Favorite.objects.create(user_id= user_id, movie_id = movie_id)
        except IntegrityError:
            return Response({'이미 이 영화는 즐겨찾기 하였습니다.'})
        return Response({'result':'추가완료'})
        
        

class Favoritelist(APIView):
    def get(self,request):
        access_token=request.headers.get('Authorization',None)
        
        SECRET = 'secret'
        
        payload=jwt.decode(access_token,SECRET,algorithms='HS256')
        
        user_id=payload.get('id',None)
        
        offset = request.GET['offset']
        limit = request.GET['limit']
        
        m_f= Favorite.objects.annotate(favorite_id=F('id')).select_related('movie').select_related('user').filter(user_id=user_id)[int(offset):int(limit)]
        serializer = AddFavoriteSerializer(m_f,many=True)
        return Response({'count':len(serializer.data),'result':serializer.data})

class Deletefavorite(APIView):
    def delete(self,request , movie_id):
        access_token=request.headers.get('Authorization',None)
        
        SECRET = 'secret'
        
        payload=jwt.decode(access_token,SECRET,algorithms='HS256')
        
        user_id=payload.get('id',None)
        
        model=Favorite.objects.filter(movie_id=movie_id,user_id=user_id)
        model.delete()
        return Response({'result':'삭제'})


