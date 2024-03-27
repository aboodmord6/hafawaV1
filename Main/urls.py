from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index' ), 
    path('profile', views.profile , name='profile'),
    path('order', views.order , name='order'),
    path('login', views.login , name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    
]









