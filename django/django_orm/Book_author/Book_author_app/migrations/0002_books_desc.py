# Generated by Django 2.2.4 on 2024-05-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_author_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='desc',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
