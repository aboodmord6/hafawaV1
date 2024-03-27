from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('orderManager/', views.orderManager, name='orderManager'),
    path('accountManager/', views.accountManager, name='accountManager'),
    path('eventManager/', views.eventManager, name='eventManager'),
    path('appManager/', views.appManager, name='appManager'),
]


urlCRUD = [
    #orderManager
    path('viewR/<str:pk>/', views.viewreq, name='viewreq'),
    path('acceptR/<str:pk>/', views.acceptreq, name='acceptreq'),
    path('rejectR/<str:pk>/', views.rejectreq, name='rejectreq'),
    path('putNotes/<str:pk>/', views.putNotes, name='note'),

    #eventManager
    path('viewEvent/<str:pk>/', views.viewEvent, name='viewEvent'),
    path('createEvent/', views.createEvent, name='createEvent'),
    path('editEvent/<str:pk>/', views.editEvent, name='editEvent'),
    path('deleteEvent/<str:pk>/', views.deleteEvent, name='deleteEvent'),

    #accountManager
    path('acceptAccount/<str:pk>/', views.acceptAcc, name='acceptAccount'),
    path('viewProfile/<str:pk>/',views.viewProfile, name='userProfile'),
    path("deleteAccount/<str:pk>/", views.deleteAccount, name="deleteAccount"),

    #appManager
    path('App/', views.addadsPic, name='addPic'),
    
]

urlpatterns += urlCRUD