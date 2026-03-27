from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Gallery(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200,blank=False,null=False)

    slug = models.SlugField(unique=True)

    is_public = models.BooleanField(default=True)

    # password = models.IntegerField(max_length=8, min_length=4, blank=True)
    password = models.CharField(
       max_length=8,
        blank=True,
        validators=[
                MinLengthValidator(4)
            ]
        )

    allow_download = models.BooleanField(default=True)

    allow_comment = models.BooleanField(default=True)

    allow_like = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):

    gallery = models.ForeignKey(Gallery, null=False,blank=False, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="gallery_images" ,null=False,blank=False,)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery.title
    
class Like(models.Model):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('image', 'user')
        
class Comment(models.Model):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    text = models.TextField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
    
class Activity(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    action = models.CharField(max_length=50)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action}"