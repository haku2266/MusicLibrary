from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.models import CreatePostModel
from .forms import ArtistRegisterFrom
from django.contrib.auth import get_user_model
from .models import ArtistModel, AlbumModel, LikedContentModel, SongModel, PlaylistModel
from siteuser.forms import LoginForm
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)


def home_view(request):
    page_title = 'home'
    posts_obj = CreatePostModel.objects.all().select_related('artist').select_related('artist__user')[:3]
    artist_obj = ArtistModel.objects.all()[:4]
    albums = AlbumModel.objects.all()
    return render(request, template_name='home.html', context={
        'page_title': page_title,
        'posts': posts_obj,
        'artists': artist_obj,
        'albums': albums
    })


@login_required
def artist_registration_view(request):
    try:
        if request.user.artist:
            return render(request, template_name='universal_error.html', context={
                'error': 'You are already an artist'
            })
    except ObjectDoesNotExist:
        page_title = 'register artist'
        form = ArtistRegisterFrom()

        if request.method == 'POST':
            form = ArtistRegisterFrom(request.POST)
            if form.is_valid():
                if form.cleaned_data['nickname']:
                    artist = ArtistModel(nickname=form.cleaned_data['nickname'], user=request.user)
                else:
                    artist = ArtistModel(nickname=f'{request.user.first_name} {request.user.last_name}',
                                         user=request.user)
                artist.save()
                return redirect('home')
        return render(request, template_name='artist_registration.html', context={
            'form': form,
            'page_title': page_title,
        })


@login_required
def artist_profile_page_view(request):
    try:
        if request.user.artist:
            page_title = 'my profile'
            obj = ArtistModel.objects.prefetch_related('songs_by_artist').prefetch_related('albums_by_artist') \
                .prefetch_related('posts').select_related('user').get(id=request.user.id)

            return render(request, template_name='artist_profile_page.html', context={
                'artist': obj,
                'page_title': page_title
            })
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={
            'error': 'You are not an artist'
        })


@login_required
def user_profile_page_view(request):
    return render(request, template_name='user_profile_page.html')


def artist_detail_view(request, id):
    page_title = 'artist'
    obj = ArtistModel.objects.prefetch_related('songs_by_artist').prefetch_related('albums_by_artist') \
        .prefetch_related('posts').select_related('user').get(id=id)

    return render(request, template_name='artist_detail.html', context={
        'artist': obj,
        'page_title': page_title
    })


def all_artists_view(request):
    page_title = 'all artists'
    obj = ArtistModel.objects.all()
    return render(request, template_name='all_artists.html', context={
        'artists': obj,
        'page_title': page_title
    })


def all_albums_view(request, id):
    page_title = 'all albums'
    obj = AlbumModel.objects.filter(artist__user_id=id)

    return render(request, template_name='all_albums.html', context={
        'albums': obj,
        'page_title': page_title
    })


def artist_album_detail_view(request, id):
    page_title = 'album'
    obj = AlbumModel.objects.get(id=id)

    return render(request, template_name='album_detail.html', context={
        'album': obj,
        'page_title': page_title
    })


def song_detail_view(request, id):
    obj = SongModel.objects.get(id=id)
    return render(request, template_name='song_detail.html', context={
        'song': obj
    })


@login_required
def like_song_view(request, id):
    try:
        obj = SongModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={'error': 'This does not exist'})
    else:
        try:
            if request.user.liked_content:
                if request.user.liked_content.songs.all():
                    for i in request.user.liked_content.songs.all():
                        if obj == i:
                            request.user.liked_content.songs.remove(obj)
                            return redirect('album_detail', id=obj.album.id)

                    request.user.liked_content.songs.add(obj)
                    return redirect('album_detail', id=obj.album.id)

                else:
                    x = request.user.liked_content
                    x.songs.add(obj)
                    x.save()
                    return redirect('album_detail', id=obj.album.id)

        except ObjectDoesNotExist:
            x = LikedContentModel()
            x.user = request.user
            x.save()
            x.songs.add(obj)
            x.save()
            return redirect('album_detail', id=obj.album.id)


def add_album(request):
    ...





















# def add_playlist(request):


# ------------------------------------------------------------------------------

# RIGHT AFTER PLAYLIST


# def add_song_view(request, id):
#     play = PlaylistModel.objects.get(title='before-you-leave')
#     try:
#         obj = SongModel.objects.get(id=id)
#     except ObjectDoesNotExist:
#         return redirect('album_detail')
#     else:
#         if request.user.playlists_of_user.all():
#             for i in request.user.playlists_of_user.all():
#                 if i == play:
#                     for song in i.songs.all():
#                         if obj == song:
#                             play.songs.remove(obj)
#                             return redirect('album_detail', id=obj.album.id)
#                     play.songs.add(obj)
