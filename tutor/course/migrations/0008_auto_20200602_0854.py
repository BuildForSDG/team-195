# Generated by Django 3.0.5 on 2020-06-02 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200602_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]