# Generated by Django 3.1 on 2020-08-28 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0035_auto_20200828_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class10answers',
            name='image1',
            field=models.ImageField(blank=True, upload_to='answersClass10'),
        ),
        migrations.AlterField(
            model_name='class10answers',
            name='image2',
            field=models.ImageField(blank=True, upload_to='answersClass10'),
        ),
    ]
