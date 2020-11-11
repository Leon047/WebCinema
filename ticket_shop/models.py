from django.db import models


class MovieDescription(models.Model):
    time_date = models.DateTimeField(auto_now_add=True, db_index=True)
    poster = models.ImageField(upload_to = 'movie/%Y/%m/%d', verbose_name='Movie image')
    title = models.CharField(max_length=50, db_index=True, verbose_name='Title' )

    treiler = models.URLField(verbose_name='Treiler')
    text = models.TextField(verbose_name='Description')
    additional_photo = models.ImageField(upload_to = 'movie/%Y/%m/%d', verbose_name='Additional image')

    def __str__(self):
        return self.title
