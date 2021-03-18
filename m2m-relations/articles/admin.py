from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Tag, ArtickeTag

class TagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count > 1:
            raise ValidationError('Может быть только один главный тэг')
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()

class TagInLine(admin.TabularInline):
    model = Tag.article.through
    formset = TagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInLine]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

