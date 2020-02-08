from django.contrib import admin
from .models import Article, Category, Page

# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content','is_deleted', 'author','create_time','last_updated_time')
    ordering = ('id',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Page)


# Register your models here.



