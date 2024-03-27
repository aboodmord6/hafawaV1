from django.http import HttpResponse
from django.shortcuts import render, redirect
from Main.models import MyUser
from visitor.models import PR_Request
from event.models import Event
from django.db import models
from django.contrib import messages
from .forms import ProfileForm
from .models import PR_profile
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def view_Req(request, pk):
    if request.user_agent.is_mobile:
        template = "MainApp/mobile/pages/viewReq.html"
    else:
        template = "MainApp/App/pages/viewReq.html"
    data = PR_Request.objects.filter(requester=request.user, id=pk)
    return render(request, template, {"d": data})


def updateProfile(request, pk):
    profile = PR_profile.objects.get(user=request.user)
    userd =  MyUser.objects.get(id=request.user.id)
    if request.method == "POST":
        fn = request.POST.get("FN").strip()
        ln = request.POST.get("LN").strip()
        cp = request.POST.get("CP").strip()
        ph = request.POST.get("PH").strip()
        cph = request.POST.get("CPH").strip()
        phh = request.POST.get("PHH").strip()
        profile_pic = request.FILES.get("pfp")  # Get the uploaded profile picture file
        if profile_pic:
            profile.personalPhoto = profile_pic  # Save the profile picture to the profile object
        userd.first_name = fn
        userd.last_name = ln
        userd.cp = cp
        userd.phone = ph
        profile.homephone = phh
        profile.cp = cph
        profile.save()
        userd.save()
        return redirect("index")
    context = {"Profile": profile}
    if request.user_agent.is_mobile:
        return render(request, "MainApp/mobile/pages/updateProfile.html", context)
    return render(request, "MainApp/App/components/updateProfile.html", context)
    
    
        


def create_Req(request):
    if request.method == "POST":
        if Event.objects.get(id=request.POST.get("8")).maxcap >= int(request.POST.get("3")) + Event.objects.get(id=request.POST.get("8")).realAttendee():
            PR_Request.objects.create(
                requester=request.user,
                numberOfGuests=request.POST.get("3"),
                hotelName=request.POST.get("2"),
                hotelLocation=request.POST.get("5"),
                nationaltyOfvisitors=request.POST.get("6"),
                event=Event.objects.get(id=request.POST.get("8")),
            )
            
        else:
            messages.error(request, "عدد الحاضرين اكبر من العدد المسموح به")
            return redirect("order")
    messages.success(request, "تم ارسال الطلب ")
    return redirect("order")


def delete_Req(request, pk):
    data = PR_Request.objects.get(id=pk)
    data.delete()
    resp = HttpResponse(status=200)
    resp["HX-Refresh"] = "True"
    return resp



