# Generated by Django 3.1 on 2020-08-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200819_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetail',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.DeleteModel(
            name='ProfilePic',
        ),
    ]
