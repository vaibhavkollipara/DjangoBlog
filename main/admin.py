from django.contrib import admin
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title' , 'timestamp' , 'updated']
    list_filter = ['title','timestamp','updated']

    class Meta:
        model = Post


admin.site.register(Post,PostModelAdmin)