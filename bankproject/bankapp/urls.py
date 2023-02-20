from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home' ),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('buttonpage/',views.buttonpage,name='buttonpage'),
    path("accountopening/",views.accountopening,name='accountopening'),
    path('document/',views.document,name='document'),
    path('trivandram/',views.trivandram,name='trivandram'),
    path('kollam/',views.kollam,name='kollam'),
    path('pathanamthitta/',views.pathanamthitta,name='pathanamthitta'),
    path('eranakulam/',views.eranakulam,name='eranakulam'),
    path('palakkad/',views.palakkad,name='palakkad'),
    path('logout/',views.logout,name='logout'),

]