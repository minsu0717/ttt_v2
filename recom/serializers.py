from dataclasses import fields
from rest_framework import serializers
from .models import Favorite, Movie2,User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie2
        fields=('poster',)
        
class MovieInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie2
        fields = ('id','title','short_description','genre_ids','release_year','urls','poster','provider')
        
class MovieSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie2
        fields = ('title','release_year','urls','poster','provider')

class UserId(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)
        
class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class MovieIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie2
        fields = ('id',)
        
class AddFavoriteSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    favorite_id = serializers.IntegerField(source='id')
    
    class Meta:
        model = Favorite
        fields = ('favorite_id','movie_id','user_id','poster')
    def get_poster(self,obj):
        return obj.movie.poster