from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie2,User,Favorite
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import MovieInfoSerializer, MovieSearchSerializer, MovieSerializer
from rest_framework.response import Response

# Create your views here.

def userregister(request):
    pass

def userlogin(request):
    pass

def userlogout(request):
    #jwt_required
    pass

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

def addfavorite(request):
    #jwt_required
    pass

def favoritelist(request):
    #jwt_required
    pass

def deletefavorite(request):
    #jwt_required
    pass


