# Generated by Django 3.0.5 on 2020-06-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20200602_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade_name',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]