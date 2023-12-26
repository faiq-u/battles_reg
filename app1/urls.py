from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('reg/',views.reg,name='reg'),
    path('view/',views.view,name='view'),
    path('own',views.own,name='own'),
]
