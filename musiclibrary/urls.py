from django.urls import path
from .views import home_view, artist_registration_view, create_post_view, \
                    artist_post_list_view, post_delete_view, user_post_list_view, edit_post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('register/artist/', artist_registration_view, name='artist_register'),
    path('createpost/', create_post_view, name='create_post'),
    path('artist/posts/list/', artist_post_list_view, name='artist_posts_list'),
    path('post/<int:id>/delete/', post_delete_view, name='delete_post'),
    path('post/<int:id>/edit/', edit_post_view, name='edit_post'),
    path('posts/list/', user_post_list_view, name='user_posts_list'),
    path(post)

]