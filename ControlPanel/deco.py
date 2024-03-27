from django.http import HttpResponse



def only_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_admin and request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse("404 Not Found", status=404)
    return wrapper