from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from posts.models import CreatePostModel
from .forms import ArtistRegisterFrom
from django.contrib.auth import get_user_model
from .models import ArtistModel
from siteuser.forms import LoginForm
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)


def home_view(request):
    page_title = 'home'
    posts_obj = CreatePostModel.objects.all().select_related('artist').select_related('artist__user')[:3]
    return render(request, template_name='home.html', context={
        'page_title': page_title,
        'posts': posts_obj,
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


def artist_detail_view(request, id):
    page_title = 'artist'
    obj = ArtistModel.objects.prefetch_related('songs_by_artist').prefetch_related('albums_by_artist')\
        .prefetch_related('posts').select_related('user').get(id=id)
    for i in obj.albums_by_artist.all():
        print(i.liked_albums.all())
    return render(request, template_name='artist_detail.html', context={
        'artist': obj,
        'page_title': page_title
    })
