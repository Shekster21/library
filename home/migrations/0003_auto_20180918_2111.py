# Generated by Django 2.0.5 on 2018-09-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180918_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='BookNumber',
            field=models.IntegerField(unique=True),
        ),
    ]
