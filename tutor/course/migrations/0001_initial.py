<<<<<<< HEAD
# Generated by Django 3.0.5 on 2020-06-09 19:41
=======
# Generated by Django 3.0.5 on 2020-06-02 18:30
>>>>>>> ft-student-take-course

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=15, unique=True)),
=======
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
                ('content', models.FileField(upload_to='')),
>>>>>>> ft-student-take-course
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
<<<<<<< HEAD
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Grade')),
=======
                ('grade', models.IntegerField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
>>>>>>> ft-student-take-course
            ],
            options={
                'ordering': ('-created',),
            },
        ),
<<<<<<< HEAD
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(max_length=50)),
                ('content', models.FileField(blank=True, upload_to='')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
=======
>>>>>>> ft-student-take-course
    ]
