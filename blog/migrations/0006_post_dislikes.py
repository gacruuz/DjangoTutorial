# Generated by Django 2.2.11 on 2020-04-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postdislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.BigIntegerField(default=0),
        ),
    ]
