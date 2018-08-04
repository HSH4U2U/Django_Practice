from django.contrib import admin
from .models import Post, Comment


# Register your models here.
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']
    actions = ['make_published']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = '글자수'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request,'{}건의 포스팅을 Published 상태로 변경'.format(updated_count))



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
