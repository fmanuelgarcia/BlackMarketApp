# Generated by Django 3.1 on 2022-03-23 04:48

import customers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=9, validators=[customers.models.phone_validate])),
                ('direction', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=255)),
                ('is_regular_client', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'customers',
                'ordering': ('-created',),
            },
        ),
    ]
