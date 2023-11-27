from django.urls import path
from .views import home_view, artist_registration_view, artist_detail_view, \
    artist_album_detail_view, like_song_view, song_detail_view, all_albums_view,\
    all_artists_view, user_profile_page_view, follow_artist_view, like_album_view,add_song_view


urlpatterns = [
    path('', home_view, name='home'),
    path('register/artist/', artist_registration_view, name='artist_register'),
    path('artist/<int:id>/detail/', artist_detail_view, name='artist_detail'),
    path('album/<int:id>/detail/', artist_album_detail_view, name='album_detail'),
    path('song/<int:id>/detail/', song_detail_view, name='song_detail'),
    path('all_albums/<int:id>/', all_albums_view, name='all_albums'),
    path('all_artists/', all_artists_view, name='all_artists'),
    path('follow/<int:id>/artist/', follow_artist_view, name='follow-artist'),
    path('like_song/<int:id>/', like_song_view, name='like_song'),
    path('like_album/<int:id>/', like_album_view, name='like_album'),
    path('user_profile', user_profile_page_view, name='user_profile'),
    path('add_song/', add_song_view, name='add_song')
]
