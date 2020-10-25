from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import Tutorials, TutorialSeries, TutorialsCategory


class TutorialsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title/Published Date', {'fields': ['tutorial_title', 'tutorial_published_date']}),
        ('Tutorial Content & Image Description', {'fields': ['tutorial_content', 'tutorial_image_desc']}),
        ('Tutorial Series', {'fields': ['tutorial_series']}),
        ('URL', {'fields': ['tutorial_link']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class TutorialSeriesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tutorial Series Title & Category', {'fields': ['tutorial_series', 'tutorial_category']}),
        ('Series Summary', {'fields': ['series_summary']})
    ]


class TutorialsCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tutorial Categories', {'fields': ['tutorial_category']}),
        ('Category Summary', {'fields': ['tutorial_summary']}),
        ('Category Slug', {'fields': ['category_link']})
    ]


admin.site.register(Tutorials, TutorialsAdmin)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)
admin.site.register(TutorialsCategory, TutorialsCategoryAdmin)
