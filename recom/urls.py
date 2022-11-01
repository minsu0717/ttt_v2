from django.urls import path, URLPattern

from recom.views import MovieList
from recom.views import MovieInfo
from recom.views import MovieSearch
from recom.views import UserRegister
from recom.views import UserLogin


urlpatterns = [
    path('movielist/',MovieList.as_view()),
    path('5/<int:movie_id>/',MovieInfo.as_view()),
    path('1/',MovieSearch.as_view()),
    path('regis',UserRegister.as_view()),
    path('2',UserLogin.as_view()),
]
