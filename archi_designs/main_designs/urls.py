from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('plan_list/', views.plan_list, name='plan_list'),
    path('plan_detail/<int:plan_id>/', views.plan_detail, name='plan_detail'),
]