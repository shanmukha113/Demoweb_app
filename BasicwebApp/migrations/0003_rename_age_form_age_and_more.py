# Generated by Django 5.0.3 on 2024-03-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicwebApp', '0002_alter_form_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Date_of_Birth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Mail',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='form',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
