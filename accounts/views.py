from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gallery.models import Activity


def signup_view(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, "signup.html")

def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, "login.html")

def logout_view(request):

    logout(request)
    return redirect('login')


@login_required
def dashboard(request):

    return render(request, "dashboard.html")

@login_required
def activity_feed(request):

    activities = Activity.objects.filter(
        image__gallery__owner=request.user
    ).order_by('-created_at')

    return render(request, "activity.html", {
        "activities": activities
    })