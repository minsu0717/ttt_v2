from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    movie = models.ForeignKey('Movie2', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite'
        unique_together = (('user', 'movie'),)


class Movie(models.Model):
    title = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    short_description = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    genre_ids = models.CharField(max_length=200, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    urls = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    poster = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    provider = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class Movie2(models.Model):
    title = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    short_description = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    genre_ids = models.CharField(max_length=200, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    urls = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    poster = models.CharField(max_length=1000, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    provider = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_2'


class User(models.Model):
    email = models.CharField(unique=True, max_length=45)
    name = models.CharField(max_length=10)
    password = models.CharField(unique=True, max_length=256)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        
    def __str__(self):
        return self.name
