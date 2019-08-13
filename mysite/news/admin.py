from django.contrib import admin
from .models import Articles


class ArticlesAdmin(admin.ModelAdmin):

    list_display = ['author', 'title', 'data']
    list_filter = ['data', 'title', 'author']
    search_fields = ['title']


    class Meta:
        model = Articles


admin.site.register(Articles, ArticlesAdmin)


