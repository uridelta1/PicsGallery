from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Gallery, Image,Activity,Comment
import uuid


@login_required
def my_galleries(request):
    galleries = Gallery.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, "my_galleries.html", {"galleries": galleries})


@login_required
def delete_gallery(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id, owner=request.user)
    if request.method == "POST":
        gallery.delete()
    return redirect('my_galleries')


@login_required
def upload_gallery(request):

    if request.method == "POST":

        title = request.POST['title']
        is_public = request.POST.get('is_public')
        password = request.POST.get('password')

        allow_download = request.POST.get('allow_download')
        allow_comment = request.POST.get('allow_comment')
        allow_like = request.POST.get('allow_like')

        slug = uuid.uuid4().hex[:10]

        gallery = Gallery.objects.create(

            owner=request.user,
            title=title,
            slug=slug,
            is_public=True if is_public else False,
            password=password,
            allow_download=True if allow_download else False,
            allow_comment=True if allow_comment else False,
            allow_like=True if allow_like else False

        )

        images = request.FILES.getlist('images')

        for img in images:

            Image.objects.create(

                gallery=gallery,
                image=img

            )

        return render(request, "share_success.html", {"gallery": gallery})

    return render(request, "upload.html")

from django.shortcuts import get_object_or_404

@login_required
def view_gallery(request, slug):

    gallery = get_object_or_404(Gallery, slug=slug)

    images = Image.objects.filter(gallery=gallery)

    return render(request, "view_gallery.html", {

        "gallery": gallery,
        "images": images

    })

from django.shortcuts import render, redirect
from .models import Gallery

@login_required
def enter_gallery(request):

    if request.method == "POST":

        slug = request.POST['slug']
        password = request.POST.get('password')

        try:
            gallery = Gallery.objects.get(slug=slug)

            # Check password if gallery is private
            if gallery.password:
                if password != gallery.password:
                    return render(request, "enter_gallery.html", {
                        "error": "Wrong Password"
                    })

            return redirect(f"/gallery/{slug}/")

        except Gallery.DoesNotExist:
            return render(request, "enter_gallery.html", {
                "error": "Gallery not found"
            })

    return render(request, "enter_gallery.html")

from django.http import JsonResponse
from .models import Like, Image

@login_required
def like_image(request, image_id):

    if not request.user.is_authenticated:
        return JsonResponse({"error": "login required"})

    image = Image.objects.get(id=image_id)

    like, created = Like.objects.get_or_create(
        image=image,
        user=request.user
    )

    if created:

        Activity.objects.create(
            user=request.user,
            action="liked",
            image=image
        )

        liked = True

    else:
        like.delete()
        liked = False

    total_likes = Like.objects.filter(image=image).count()

    return JsonResponse({
        "liked": liked,
        "total_likes": total_likes
    })

@csrf_exempt
@login_required
def add_comment(request, image_id):

    if request.method == "POST":

        if not request.user.is_authenticated:
            return JsonResponse({"error": "login required"})

        text = request.POST.get("text")

        image = Image.objects.get(id=image_id)

        comment = Comment.objects.create(
            image=image,
            user=request.user,
            text=text
        )

        Activity.objects.create(
            user=request.user,
            action="commented",
            image=image
        )

        return JsonResponse({
            "user": comment.user.username,
            "text": comment.text
        })

