from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
