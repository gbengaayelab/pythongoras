from datetime import datetime

from django.db import models


class TutorialsCategory(models.Model):
    tutorial_category = models.CharField(max_length=255)
    tutorial_summary = models.CharField(max_length=255)
    category_link = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=255)
    tutorial_category = models.ForeignKey(TutorialsCategory, default=1, verbose_name='Category', on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=255, default=1)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.tutorial_series


class Tutorials(models.Model):
    tutorial_title = models.CharField(max_length=255)
    tutorial_content = models.TextField()
    tutorial_published_date = models.DateTimeField("Date Published", default=datetime.now())
    tutorial_image_desc = models.URLField(max_length=255)
    tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name='Series', on_delete=models.SET_DEFAULT)
    tutorial_link = models.CharField(max_length=255, default=1)

    class Meta:
        verbose_name_plural = 'Tutorials'

    def __str__(self):
        return self.tutorial_title
