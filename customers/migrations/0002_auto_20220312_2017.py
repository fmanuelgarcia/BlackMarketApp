# Generated by Django 3.1 on 2022-03-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='is_regular_client',
            field=models.BooleanField(default=1),
        ),
    ]