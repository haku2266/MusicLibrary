from django.urls import path
from .views import create_post_view, \
                    artist_post_list_view, post_delete_view, user_post_list_view, edit_post_view,\
                    post_detail_view

urlpatterns = [
    path('createpost/', create_post_view, name='create_post'),
    path('artist/list/', artist_post_list_view, name='artist_posts_list'),
    path('<int:id>/delete/', post_delete_view, name='delete_post'),
    path('<int:id>/edit/', edit_post_view, name='edit_post'),
    path('user/<int:id>/list/', user_post_list_view, name='user_posts_list'),
    path('<int:id>/detail/', post_detail_view, name='post_detail'),
]