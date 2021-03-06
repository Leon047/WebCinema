# Generated by Django 3.1.3 on 2020-11-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchNowCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('card_img', models.ImageField(upload_to='movie/%Y/%m/%d', verbose_name='Movie image')),
                ('card_title', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WatchSoonCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('card_img', models.ImageField(upload_to='movie/%Y/%m/%d', verbose_name='Movie image')),
                ('card_title', models.CharField(db_index=True, max_length=50)),
                ('release', models.CharField(max_length=50)),
            ],
        ),
    ]
