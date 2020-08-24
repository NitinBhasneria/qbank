# Generated by Django 3.1 on 2020-08-18 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syllabus', models.CharField(max_length=10)),
                ('classes', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.CharField(blank=True, max_length=25)),
                ('subject2', models.CharField(blank=True, max_length=25)),
                ('subject3', models.CharField(blank=True, max_length=25)),
                ('subject4', models.CharField(blank=True, max_length=25)),
                ('subject5', models.CharField(blank=True, max_length=25)),
                ('subject6', models.CharField(blank=True, max_length=25)),
                ('syllabus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='students.syllabus')),
            ],
        ),
    ]