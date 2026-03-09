from django.urls import path
from . import views

urlpatterns = [

    path('upload/', views.upload_gallery, name="upload"),
    path('view/', views.enter_gallery, name="enter_gallery"),
    path('my/', views.my_galleries, name="my_galleries"),
    path('delete/<int:gallery_id>/', views.delete_gallery, name="delete_gallery"),
    path('like/<int:image_id>/', views.like_image, name="like_image"),
    path('comment/<int:image_id>/', views.add_comment, name="add_comment"),
    path('<slug:slug>/', views.view_gallery, name="view_gallery"),

]