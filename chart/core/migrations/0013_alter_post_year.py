# Generated by Django 4.0 on 2022-04-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_post_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
