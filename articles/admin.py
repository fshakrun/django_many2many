from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            cl_data = form.cleaned_data
            if cl_data != {}:
                if cl_data['is_main']:
                    count += 1
        if count > 1:
            raise ValidationError('Может быть только 1 главный тег')
        elif count == 0:
            raise ValidationError('Выберите 1 главный тег')

        return super().clean()


class ArticleTagsInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text']
    list_filter = ['title']
    inlines = [ArticleTagsInline]
