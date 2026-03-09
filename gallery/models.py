from django.db import models
from django.contrib.auth.models import User


class Gallery(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    is_public = models.BooleanField(default=True)

    password = models.CharField(max_length=100, blank=True)

    allow_download = models.BooleanField(default=True)

    allow_comment = models.BooleanField(default=True)

    allow_like = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="gallery_images")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery.title
    
class Like(models.Model):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('image', 'user')
        
class Comment(models.Model):

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
    
class Activity(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    action = models.CharField(max_length=50)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action}"