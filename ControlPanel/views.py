from django.http import HttpResponse
from django.shortcuts import redirect, render
from Main.models import AppAssets, MyUser
from visitor.models import PR_Request, PR_profile
from event.models import Event
from django.core.paginator import Paginator
from .deco import only_admin
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from webpush import send_user_notification
from django.db.models import Sum
@only_admin
def dashboard(request):
    profiles = PR_profile.objects.all().filter(user__is_active=1).count()
    requests = PR_Request.objects.all().count()
    events = Event.objects.all().count()
    requestList = PR_Request.objects.filter(isApproved=-1)[0:5:1]
    profileList = PR_profile.objects.filter(user__is_active=0).order_by('-user__date_created')[0:3:1]
    eventsList = Event.objects.all().filter(Q(date__gte=timezone.now()))[0:5:1]

    context = {
        "profiles": profiles,
        "requests": requests,
        "events": events,
        "requestList": requestList,
        "profileList": profileList,
        "eventsList": eventsList,
    }
    return render(request, "ControlPanel/pages/dashboard.html", context)


@only_admin
def orderManager(request):
    if request.method == "POST":
        if "clear" in request.POST:
            if "search" in request.session:
                del request.session["search"]
            if "typeF" in request.session:
                del request.session["typeF"]
            if "date" in request.session:
                del request.session["date"]
            if "status" in request.session:
                del request.session["status"]
            if "can_clear" in request.session:
                del request.session["can_clear"]
        else:
            # Store filters in session
            request.session["search"] = request.POST.get("search")
            request.session["typeF"] = request.POST.get("typeF")
            request.session["date"] = request.POST.get("date")
            request.session["status"] = request.POST.get("status")
            request.session["can_clear"] = True

    # Retrieve filters from session
    if request.session.get("search") is not None:
        search = request.session.get("search")
    else:
        search = ""
    typeF = request.session.get("typeF")
    if request.session.get("date") is not None:
        date = request.session.get("date")
    else:
        date = ""
    status = request.session.get("status")
    can = request.session.get("can_clear")

    orders = PR_Request.objects.all()

    if search is not None:
        if typeF == "FN":
            user = MyUser.objects.filter(first_name__icontains=search)
            orders = orders.filter(requester__in=user)
        elif typeF == "LN":
            user = MyUser.objects.filter(last_name__icontains=search)
            orders = orders.filter(requester__in=user)
        elif typeF == "email":
            user = MyUser.objects.filter(email__icontains=search)
            orders = orders.filter(requester__in=user)
        elif typeF == "hotel":
            orders = orders.filter(hotelName__icontains=search)
        

    if date is not None:
        orders = orders.filter(createDate__icontains=date)

    if status is not None and status != "2":
        orders = orders.filter(isApproved=int(status))
    
    if request.user_agent.is_mobile:
        orders = Paginator(orders, 5)
    else:
        orders = Paginator(orders, 10)
    
    page = request.GET.get("page")
    orders = orders.get_page(page)

    context = {
        "o": orders,
        "typeF": typeF,
        "date": date,
        "search": search,
        "status": status,
        "can_clear": can,
    }
    return render(request, "ControlPanel/pages/orderManager.html", context)


@only_admin
def eventManager(request):
    if request.method == "POST":
        if "clear" in request.POST:
            if "search" in request.session:
                del request.session["search"]
            if "typeF" in request.session:
                del request.session["typeF"]
            if "date" in request.session:
                del request.session["date"]
            if "can_clear" in request.session:
                del request.session["can_clear"]
        else:
            # Store filters in session
            request.session["search"] = request.POST.get("search")
            request.session["typeF"] = request.POST.get("typeF")
            request.session["date"] = request.POST.get("date")
            request.session["can_clear"] = True

    events = Event.objects.all()

    if request.session.get("search") is not None:
        search = request.session.get("search")
    else:
        search = ""
    if request.session.get("date") is not None:
        date = request.session.get("date")
        events = events.filter(date__icontains=date)
    else:
        date = timezone.now()
    can = request.session.get("can_clear")
    if search is not None:
        events = events.filter(name__icontains=search)
    
    if request.user_agent.is_mobile:
        events = Paginator(events, 5)
    else:
        events = Paginator(events, 10)
    page = request.GET.get("page")
    events = events.get_page(page)
    past_events = Event.objects.filter(Q(date__lt=timezone.now())).count()
    future_events = Event.objects.filter(Q(date__gte=timezone.now())).count()
    total_participants = PR_Request.objects.filter(isApproved=1, event__date__lt=timezone.now()).aggregate(Sum('numberOfGuests'))['numberOfGuests__sum'] or 0
    
    context = {
        "e": events,
        "date": date,
        "search": search,
        "can_clear": can,
        "a": past_events,
        "b": future_events,
        "c": total_participants,
    }
    return render(request, "ControlPanel/pages/eventManager.html", context)


@only_admin
def createEvent(request):
    if request.method == "POST":
        e = Event.objects.create(
            name=request.POST.get("name"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            maxcap=request.POST.get("maxcap"),
            image=request.FILES.get("image"),
        )
        return redirect("eventManager")
    return render(request, "ControlPanel/pages/create/createEvent.html")


@only_admin
def deleteEvent(request, pk):
    e = Event.objects.get(id=pk)
    e.delete()
    return redirect("eventManager")


@only_admin
def appManager(request):
    return render(request, "ControlPanel/pages/appManager.html")


@only_admin
def viewreq(request, pk):
    r = PR_Request.objects.get(id=pk)
    context = {
        "r": r,
    }
    return render(request, "ControlPanel/pages/viewpages/viewreq.html", context)


@only_admin
def putNotes(request, pk):
    if request.method == "POST":
        r = PR_Request.objects.get(id=pk)
        if not request.POST.get("notes") == "":
            r.notes = request.POST.get("notes")
        else:
            r.notes = "لايوجد ملاحظات"
        r.save()
        return HttpResponse(status=204)


@only_admin
def acceptreq(request, pk):
    r = PR_Request.objects.get(id=pk)
    user = MyUser.objects.get(id=r.requester.id)
    r.isApproved = 1
    r.save()
    if r.notes == "لايوجد ملاحظات":
        r.notes = "يرجى التواصل معنا للمزيد من التفاصيل"
    payload = {"head": "Hafawa", "body": " تم قبول طلبك" + "\n" + r.notes}
    send_user_notification(user=user , payload = payload, ttl = 1000)
    return redirect("dashboard")


@only_admin
def rejectreq(request, pk):
    r = PR_Request.objects.get(id=pk)
    user = MyUser.objects.get(id=r.requester.id)
    r.isApproved = 0
    if r.notes == "لايوجد ملاحظات":
        r.notes = "يرجى التواصل معنا للمزيد من التفاصيل"
    payload = {"head": "Hafawa", "body": "تم رفض طلبك" + "\n" + r.notes}
    send_user_notification(user=user , payload = payload, ttl = 1000)
    r.save()
    return redirect("dashboard")


@only_admin
def viewEvent(request, pk):
    e = Event.objects.get(id=pk)
    context = {
        "e": e,
    }
    return render(request, "ControlPanel/pages/viewpages/viewEvent.html", context)


@only_admin
def editEvent(request, pk):
    e = Event.objects.get(id=pk)
    context = {
        "e": e,
    }
    if request.method == "POST":
        e.name = request.POST.get("name")
        e.date = request.POST.get("date")
        e.time = request.POST.get("time")
        e.maxcap = request.POST.get("maxcap")
        if request.FILES.get("image") != None:
            e.image = request.FILES.get("image")
        e.save()
        return redirect("eventManager")
    return render(request, "ControlPanel/pages/update/editEvent.html", context)


@only_admin
def accountManager(request):

    # Apply filters
    if request.method == "POST":
        if "clear" in request.POST:
            if "search" in request.session:
                del request.session["search"]
            if "typeF" in request.session:
                del request.session["typeF"]
            if "can_clear" in request.session:
                del request.session["can_clear"]
        else:

            request.session["search"] = request.POST.get("search")
            request.session["typeF"] = request.POST.get("typeF")
            request.session["can_clear"] = True

    profiles = PR_profile.objects.filter(user__is_admin=0)

    if request.session.get("search") is not None:
        search = request.session.get("search")
    else:
        search = ""
    can = request.session.get("can_clear")
    # Apply search
    if search is not None:
        if request.session.get("typeF") == "FN":
            profiles = profiles.filter(user__first_name__icontains=search)
        elif request.session.get("typeF") == "LN":
            profiles = profiles.filter(user__last_name__icontains=search)
        elif request.session.get("typeF") == "email":
            profiles = profiles.filter(user__email__icontains=search)
    # Pagination
    if request.user_agent.is_mobile:
        paginator = Paginator(profiles, 5)
    else:
        paginator = Paginator(profiles, 10)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "p": page_obj,
        "can_clear": can,
        "search": search,
    }
    return render(request, "ControlPanel/pages/accountManager.html", context)


@only_admin
def acceptAcc(request, pk):
    p = MyUser.objects.get(id=pk)
    p.is_active = 1
    p.save()
    return redirect("accountManager")


@only_admin
def viewProfile(request, pk):
    userO = MyUser.objects.get(id=pk)
    p = PR_profile.objects.get(user=userO)
    context = {
        "Profile": p,
    }
    return render(request, "ControlPanel/pages/viewpages/viewProfile.html", context)


@only_admin
def deleteAccount(request, pk):
    user = MyUser.objects.get(id=pk)
    user.is_active = False
    user.save()
    return redirect("accountManager")



def addadsPic(request):
    a = AppAssets.objects.get(id=1)
    if request.method == "POST":
        a.img = request.FILES.get("image")
        a.save()
        return redirect("appManager")
    if request.htmx:
        a.img = None
        a.save()
        return redirect("appManager")