# Generated by Django 3.1 on 2020-09-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0050_auto_20200909_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='class10answer',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='commerceanswer',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scienceanswer',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
