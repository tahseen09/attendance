# Generated by Django 2.2 on 2019-04-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='roll',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
