from django.urls import path
from .views import home_view, consumer_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/listener', consumer_create_view, name='consumer')
]