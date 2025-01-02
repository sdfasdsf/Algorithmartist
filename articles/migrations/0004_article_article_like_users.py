# Generated by Django 4.2.8 on 2024-12-26 07:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0003_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="article_like_users",
            field=models.ManyToManyField(
                related_name="like_articles", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
