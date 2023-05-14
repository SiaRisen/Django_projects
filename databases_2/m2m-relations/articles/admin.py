from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                count += 1
        if count == 0:
            raise ValidationError('Укажите основной раздел')
        if count > 1:
            raise ValidationError('Только один раздел является основным!')

        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    extra = 1
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleTagInline,
    ]
    list_display = ['id', 'title', 'published_at']
    list_filter = ['title', 'published_at']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
