from django.urls import path
from .views import contact_view, home, portfolio_details, portfolio_details_2

urlpatterns = [
    path('', home, name='home'), 
    path('contact/', contact_view, name='contact'),
    path('portfolio_details/', portfolio_details, name='portfolio_details'),
    path('portfolio_details_2/', portfolio_details_2, name='portfolio_details_2'),
]
