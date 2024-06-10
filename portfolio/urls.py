from django.urls import path

from portfolio import views
from .views import contact_success

app_name = 'portfolio'
urlpatterns = [
    path("", views.home, name="home"),
    path('contact_success/', contact_success, name='contact_success'),
]