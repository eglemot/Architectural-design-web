from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('floor-plans/', views.plan_list, name='plan_list'),
    path('plan_details/<int:plan_id>/', views.plan_detail, name='plan_detail'),
    path('contacts/', views.ContactView.as_view(), name='contact'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('affiliate-disclosure/', views.affiliate_disclosure, name='affiliate_disclosure'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
]