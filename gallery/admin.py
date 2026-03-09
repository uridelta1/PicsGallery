from django.contrib import admin
from .models import Gallery, Image, Like, Comment,Activity

admin.site.register(Gallery)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Activity)