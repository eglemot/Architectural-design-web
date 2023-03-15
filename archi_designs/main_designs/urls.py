from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('plan_list', views.plan_list, name='plan_list'),
]