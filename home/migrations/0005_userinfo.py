# Generated by Django 2.0.5 on 2018-09-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180918_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdmissionNumber', models.IntegerField(unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=50)),
            ],
        ),
    ]