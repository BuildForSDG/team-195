# Generated by Django 3.0.5 on 2020-05-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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