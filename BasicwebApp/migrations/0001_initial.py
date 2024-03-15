# Generated by Django 5.0.3 on 2024-03-15 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Mail', models.EmailField(max_length=254)),
                ('Age', models.TextField()),
                ('Date_of_Birth', models.DateField(default=datetime.date(2024, 3, 15))),
            ],
        ),
    ]
