from dataclasses import fields
from rest_framework import serializers
from .models import Movie2

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