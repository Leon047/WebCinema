# Generated by Django 3.1.3 on 2020-11-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_shop', '0002_auto_20201110_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedescription',
            old_name='card_img',
            new_name='poster',
        ),
        migrations.RemoveField(
            model_name='moviedescription',
            name='card_title',
        ),
        migrations.AddField(
            model_name='moviedescription',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moviedescription',
            name='text',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='moviedescription',
            name='treiler',
            field=models.URLField(verbose_name='Treiler'),
        ),
    ]
