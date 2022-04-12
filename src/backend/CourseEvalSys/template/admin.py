from django.contrib import admin

# Register your models here.
from template import models
admin.site.register(models.Users)
admin.site.register(models.Courses)
admin.site.register(models.Comments)
admin.site.register(models.CommentsLikeStatus)
