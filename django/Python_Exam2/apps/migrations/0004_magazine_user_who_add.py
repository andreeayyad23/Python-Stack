# Generated by Django 2.2.4 on 2024-06-07 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_remove_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='user_who_add',
            field=models.ManyToManyField(related_name='added_magazines', to='apps.User'),
        ),
    ]
