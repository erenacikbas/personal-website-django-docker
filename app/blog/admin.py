from django.contrib import admin
from .models import Post, PostComment, PostMeta, Category, PostCategory, Image
# Register your models here.
# sorl-thumbnail

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('authorId', 'title','content_summary','createdAt','updatedAt',)
    list_filter = ('title','createdAt','updatedAt',)
    ordering = ('createdAt',)

class PostCommentAdmin(admin.ModelAdmin):
    model = PostComment
    list_display = ('authorId','title', 'content')
    ordering = ('createdAt',)

class PostCategoryAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostMeta)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Image)