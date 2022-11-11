from django.urls import path, URLPattern

from recom.views import MovieList
from recom.views import MovieInfo
from recom.views import MovieSearch
from recom.views import UserRegister
from recom.views import UserLogin
from recom.views import UserLogout
from recom.views import Addfavorite 
from recom.views import Deletefavorite
from recom.views import Favoritelist


urlpatterns = [
    path('movielist/',MovieList.as_view()),
    path('5/<int:movie_id>/',MovieInfo.as_view()),
    path('1/',MovieSearch.as_view()),
    path('regis',UserRegister.as_view()),
    path('2',UserLogin.as_view()),
    path('logout/',UserLogout.as_view()),
    path('f_add/<int:movie_id>',Addfavorite.as_view()),
    path('f_list/',Favoritelist.as_view()),
    path('f_del/<int:movie_id>',Deletefavorite.as_view()),
]
