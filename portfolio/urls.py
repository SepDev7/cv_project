from django.urls import path
from .views import contact_view, home
import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_view, name='contact'),
]
