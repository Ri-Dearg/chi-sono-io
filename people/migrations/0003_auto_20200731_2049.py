# Generated by Django 3.0.8 on 2020-07-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20200731_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pattern1_bg',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='person',
            name='pattern2_bg',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AddField(
            model_name='person',
            name='pattern3_bg',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='person',
            name='pattern1',
            field=models.ImageField(default='', upload_to='patterns'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pattern2',
            field=models.ImageField(default='', upload_to='patterns'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pattern3',
            field=models.ImageField(default='', upload_to='patterns'),
        ),
    ]
