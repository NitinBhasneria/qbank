# Generated by Django 3.1 on 2020-08-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0029_solvedquest'),
    ]

    operations = [
        migrations.AddField(
            model_name='solvedquest',
            name='yearsub',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]