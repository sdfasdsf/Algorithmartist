# Generated by Django 4.2.8 on 2025-01-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0025_comment_total_commentlikes_count_comment_writer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="writer",
        ),
    ]
