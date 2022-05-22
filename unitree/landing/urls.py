from django.urls import path
from landing.views import Index, Navbar

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('navbar/', Navbar.as_view(), name='navbar'),
]
