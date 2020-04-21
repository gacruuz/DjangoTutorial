from django.contrib import admin
from .models import Post, Comment, PostLike, PostDisLike


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(PostDisLike)
