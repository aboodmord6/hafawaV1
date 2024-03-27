from django.urls import path
from . import views 


urlpatterns = [
    path('createReq', views.create_Req, name='createReq'),
    path('viewReq/<str:pk>/' , views.view_Req , name='viewReq'),
    path('deleteReq/<str:pk>/', views.delete_Req, name='deleteReq'),
    path('update/<str:pk>/', views.updateProfile, name='updateProfile'),
]