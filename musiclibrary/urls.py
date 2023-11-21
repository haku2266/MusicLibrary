from django.urls import path
from .views import home_view, artist_registration_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/artist/', artist_registration_view, name='artist_register'),
]