# Generated by Django 3.0.5 on 2020-06-09 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('educationlevel', models.CharField(max_length=20)),
            ],
        ),
    ]
