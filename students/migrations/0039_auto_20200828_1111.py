# Generated by Django 3.1 on 2020-08-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0038_auto_20200828_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersClass10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=50000, null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('image2', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'answers_class10',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Class10Answers',
        ),
    ]
