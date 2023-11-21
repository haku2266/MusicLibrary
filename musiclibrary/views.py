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
                artist = ArtistModel(nickname=form.cleaned_data['nickname'], user=request.user)
                artist.save()
                return redirect('home')
        return render(request, template_name='artist_registration.html', context={
            'form': form,
            'page_title': page_title,
        })
