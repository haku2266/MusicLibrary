from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from siteuser.models import CustomUserModel
from posts.models import CreatePostModel
from .forms import ArtistRegisterFrom
from django.contrib.auth import get_user_model
from .models import ArtistModel, AlbumModel, LikedContentModel, SongModel, FollowModel
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)


def home_view(request):
    page_title = 'home'
    posts_obj = CreatePostModel.objects.all().select_related('artist').select_related('artist__user')[:3]
    artist_obj = ArtistModel.objects.all()[:5].select_related('user')
    albums = AlbumModel.objects.all().select_related('artist').select_related('artist__user').prefetch_related(
        'liked_albums')
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
def user_profile_page_view(request):
    obj = CustomUserModel.objects.prefetch_related('followings_of_user__artists__user').get(id=request.user.id)
    return render(request, template_name='user_profile_page.html', context={
        'user': obj
    })


def artist_detail_view(request, id):
    page_title = 'artist'
    obj = ArtistModel.objects.prefetch_related('songs_by_artist').prefetch_related('albums_by_artist') \
        .prefetch_related('posts').select_related('user__liked_content').prefetch_related(
        'songs_by_artist__liked_songs').get(id=id)

    return render(request, template_name='artist_detail.html', context={
        'artist': obj,
        'page_title': page_title,
    })


def all_artists_view(request):
    page_title = 'all artists'
    obj = ArtistModel.objects.all().select_related('user')
    return render(request, template_name='all_artists.html', context={
        'artists': obj,
        'page_title': page_title
    })


def all_albums_view(request, id):
    page_title = 'all albums'
    obj = AlbumModel.objects.select_related('artist'). \
        filter(artist__user_id=id)

    return render(request, template_name='all_albums.html', context={
        'albums': obj,
        'page_title': page_title
    })


def artist_album_detail_view(request, id):
    page_title = 'album'
    obj = AlbumModel.objects.select_related('artist').select_related('artist__user'). \
        get(id=id)

    return render(request, template_name='album_detail.html', context={
        'album': obj,
        'page_title': page_title
    })


def song_detail_view(request, id):
    obj = SongModel.objects.select_related('album__artist') \
        .select_related('album').get(id=id)

    return render(request, template_name='song_detail.html', context={
        'song': obj
    })


@login_required
def follow_artist_view(request, id):
    try:
        obj = ArtistModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={'error': 'Artist does not exist'})

    else:
        try:
            if request.user.followings_of_user:
                if request.user.followings_of_user.artists.all():
                    for i in request.user.followings_of_user.artists.all():
                        if obj == i:
                            request.user.followings_of_user.artists.remove(obj)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    request.user.followings_of_user.artists.add(obj)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                x = request.user.followings_of_user
                x.artists.add(obj)
                x.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except ObjectDoesNotExist:
            x = FollowModel()
            x.user = request.user
            x.save()
            x.artists.add(obj)
            x.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def like_song_view(request, id):
    try:
        obj = SongModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={'error': 'Single does not exist'})
    else:
        try:
            if request.user.liked_content:
                if request.user.liked_content.songs.all():
                    for i in request.user.liked_content.songs.all():
                        if obj == i:
                            request.user.liked_content.songs.remove(obj)
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    request.user.liked_content.songs.add(obj)
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                else:
                    x = request.user.liked_content
                    x.songs.add(obj)
                    x.save()
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except ObjectDoesNotExist:
            x = LikedContentModel()
            x.user = request.user
            x.save()
            x.songs.add(obj)
            x.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def like_album_view(request, id):
    try:
        obj = AlbumModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={'error': 'Album does not exist'})
    else:
        try:
            if request.user.liked_content:
                if request.user.liked_content.albums.all():
                    for i in request.user.liked_content.albums.all():
                        if obj == i:
                            request.user.liked_content.albums.remove(obj)
                            return redirect('album_detail', id=id)

                    request.user.liked_content.albums.add(obj)
                    return redirect('album_detail', id=id)

                else:
                    x = request.user.liked_content
                    x.albums.add(obj)
                    x.save()
                    return redirect('album_detail', id=id)

        except ObjectDoesNotExist:
            x = LikedContentModel()
            x.user = request.user
            x.save()
            x.albums.add(obj)
            x.save()
            return redirect('album_detail', id=id)


def add_album(request):
    ...
