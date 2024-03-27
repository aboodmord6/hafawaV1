from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from django.contrib.auth.models import Group
from webpush.models import *



admin.site.register(SubscriptionInfo)



class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []
    list_display = ["email", "is_admin" ,"is_visitor" ,"is_driver" ,"is_active"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password" ,"is_active"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2" , "is_visitor" ,"is_driver"],
            },
        ),
    ]
    
    





admin.site.register(MyUser , UserAdmin)
admin.site.register(AppAssets)



