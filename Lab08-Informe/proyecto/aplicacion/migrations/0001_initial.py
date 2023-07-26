# Generated by Django 4.2.2 on 2023-07-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=150)),
                ('isPremium', models.BooleanField(default=False)),
            ],
        ),
    ]
