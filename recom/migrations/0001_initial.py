# Generated by Django 4.1.2 on 2022-10-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "favorite", "managed": False,},
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "short_description",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                ("genre_ids", models.CharField(blank=True, max_length=200, null=True)),
                ("release_year", models.IntegerField(blank=True, null=True)),
                (
                    "urls",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "poster",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "provider",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "movie", "managed": False,},
        ),
        migrations.CreateModel(
            name="Movie2",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "short_description",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                ("genre_ids", models.CharField(blank=True, max_length=200, null=True)),
                ("release_year", models.IntegerField(blank=True, null=True)),
                (
                    "urls",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "poster",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "provider",
                    models.CharField(
                        blank=True,
                        db_collation="utf8mb4_0900_ai_ci",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(blank=True, null=True)),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "movie_2", "managed": False,},
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=45, unique=True)),
                ("name", models.CharField(max_length=10)),
                ("password", models.CharField(max_length=256, unique=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "user", "managed": False,},
        ),
    ]
