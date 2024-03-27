from django.http import HttpResponse
from django.shortcuts import render, redirect
from visitor.models import PR_Request
from event.models import Event
from django.contrib.auth import login as auth_login, logout, authenticate
from django.utils import timezone
from django.db.models import Q
import re
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from .models import MyUser
from visitor.models import PR_profile
from django.contrib import messages
from .models import AppAssets
from webpush.models import PushInformation

@login_required()
def index(request):
    data = PR_Request.objects.filter(requester=request.user)[0:4:1]
    events = Event.objects.filter(Q(date__gte=timezone.now())).order_by('date')[:4:1]
    
    if request.user.is_admin:
        return redirect("dashboard")
    if request.user_agent.is_mobile:
        return render(request, "MainApp/mobile/index.html", {"E": events, "R": data ,"ads": AppAssets.objects.get(id=1)})
    return render(request, "MainApp/App/index.html", {"E": events, "R": data })


# ------------------------mobile------------------------
@login_required()
def profile(request):
    p = PR_profile.objects.get(user=request.user)
    sub = False
    if PushInformation.objects.filter(user=request.user).exists():
        sub = True	
    if request.user_agent.is_mobile:
        return render(request, "MainApp/mobile/pages/profile.html", {"Profile": p ,     "sub": sub})
    return render(request, "MainApp/App/pages/profile.html", {"Profile": p , "sub": sub})


@login_required()
def order(request):
    events = Event.objects.filter(Q(date__gte=timezone.now()))[0:8:1]
    data = PR_Request.objects.filter(requester=request.user)
    
    if request.user_agent.is_mobile:
        data = data[0:10:1]
        return render(
            request, "MainApp/mobile/pages/orders.html", {"E": events, "R": data }
        )
    return render(request, "MainApp/App/pages/orders.html", {"E": events, "R": data })




def login(request):
    if request.method == "POST":
        username = request.POST.get("phone").lower()
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.user.is_admin:
                return redirect("dashboard")
            return redirect("index")
        else:
            if MyUser.objects.filter(email=username).exists():
                user = MyUser.objects.get(email=username)
                if not user.is_active:
                    messages.error(request, " يرجى تفعيل الحساب الخاص بك")
                    return render(request, "auth/login.html")
            messages.error(request, "البريد الالكتروني او كلمة المرور غير صحيحة")
            return render(request, "auth/login.html")
    return render(request, "auth/login.html")


def checkPhone(p):
    if p[0] == "0":
        p = p[1:]
    return p


def register(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username").lower()
        phone = checkPhone(request.POST.get("phone"))
        cp = request.POST.get("countryCode").replace("+", "")
        nation = request.POST.get("nation")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if not MyUser.objects.filter(email=username).exists():
            if password1 == password2:
                user = MyUser(
                    email=username,
                    first_name=fname,
                    last_name=lname,
                    phone=phone,
                    cp=cp,
                    is_active=False,
                )
                user.set_password(password1)
                user.save()
                PR_profile.objects.create(
                    user=user,
                    nationalty=nation,
                )
                return redirect("login")
            else:
                messages.error(request, "كلمة المرور غير متطابقة")
                return render(request, "auth/registration.html")
        else:
            messages.error(request, "حساب موجود بالفعل")
            return render(request, "auth/registration.html")
    return render(request, "auth/registration.html")


def logout_view(request):
    logout(request)
    return redirect("login")
