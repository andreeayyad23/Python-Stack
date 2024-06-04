# Generated by Django 2.2.4 on 2024-05-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_Actor_app', '0002_auto_20240518_0908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='actor',
            name='Category',
        ),
        migrations.AddField(
            model_name='actor',
            name='category',
            field=models.ManyToManyField(related_name='actors', to='Movie_Actor_app.Movie'),
        ),
    ]
