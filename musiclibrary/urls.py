from django.urls import path
from .views import home_view, artist_registration_view, create_post_view, artist_post_list_view, post_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/artist/', artist_registration_view, name='artist_register'),
    path('createpost/', create_post_view, name='create_post'),
    path('posts_list/', artist_post_list_view, name='artist_posts_list'),
    path('post/<int:id>/delete/', post_delete_view, name='delete_post')

]