from django.urls import path
from .views import contact_view, home, portfolio_details
from . import views

urlpatterns = [
    path('', home, name='home'), 
    path('contact/', contact_view, name='contact'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
]
