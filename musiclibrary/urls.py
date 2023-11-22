from django.urls import path
from .views import home_view, artist_registration_view, artist_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/artist/', artist_registration_view, name='artist_register'),
    path('artist/<int:id>/detail/', artist_detail_view, name='artist_detail')
]