from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from gallery.models import Activity
from .models import User, EmailOTP
from .utils import send_otp_email


# def signup_view(request):

#     if request.method == "POST":

#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         return redirect('login')

#     return render(request, "signup.html")

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

                # ✅ Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, "login.html", {
                "error": "Email already registered"
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )

        otp_obj = EmailOTP.objects.create(user=user)
        otp = otp_obj.generate_otp()
        otp_obj.otp = otp
        otp_obj.save()

        send_otp_email(email, otp)

        return redirect(f"/verify/{user.id}")

    return render(request, "signup.html")


def verify_otp(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        otp = request.POST.get("otp")
        otp_obj = EmailOTP.objects.filter(user=user).last()

        if otp_obj and otp_obj.otp == otp:
            user.is_active = True
            user.is_verified = True
            user.save()
            return redirect("login")
        else:
            return render(request, "verify.html", {"error": "Invalid OTP"})

    return render(request, "verify.html")



# def login_view(request):

#     if request.method == "POST":

#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect('dashboard')

#     return render(request, "login.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


# def login_view(request):
#     if request.method == "POST":
#         identifier = request.POST.get('username')  # email OR username
#         password = request.POST.get('password')

#         user = None

#         # 🔥 Check if input is email or username
#         if "@" in identifier:
#             try:
#                 user_obj = User.objects.get(email=identifier)
#                 user = authenticate(request, username=user_obj.username, password=password)
#             except User.DoesNotExist:
#                 user = None
#         else:
#             user = authenticate(request, username=identifier, password=password)

#         if user:
#             if user.is_verified:
#                 login(request, user)
#                 return redirect('dashboard')
#             else:
#                 return render(request, "login.html", {
#                     "error": "Please verify your email first"
#                 })
#         else:
#             return render(request, "login.html", {
#                 "error": "Invalid email/username or password"
#             })

#     return render(request, "login.html")

def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get('username')  # email or username
        password = request.POST.get('password')

        user = None

        # ✅ If email login
        if "@" in identifier:
            user = authenticate(request, username=identifier, password=password)

        # ✅ If username login
        else:
            try:
                user_obj = User.objects.get(username=identifier)
                user = authenticate(request, username=user_obj.email, password=password)
            except User.DoesNotExist:
                user = None

        print("USER:", user)  # debug

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, "login.html", {
                    "error": "Account not verified"
                })
        else:
            return render(request, "login.html", {
                "error": "Invalid credentials"
            })

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