from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtistRegisterFrom, CreatePostForm
from django.contrib.auth import get_user_model
from .models import ArtistModel, CreatePostModel

User = get_user_model()


def home_view(request):
    page_title = 'home'
    return render(request, template_name='home.html', context={
        'page_title': page_title
    })


@login_required
def artist_registration_view(request):
    page_title = 'register artist'
    form = ArtistRegisterFrom()

    try:
        x = ArtistModel.objects.get(user=request.user)
        is_artist = True
    except ArtistModel.DoesNotExist:
        is_artist = False

    if request.method == 'POST':
        form = ArtistRegisterFrom(request.POST)
        if form.is_valid():
            artist = ArtistModel(nickname=form.cleaned_data['nickname'], user=request.user)
            artist.save()
            return redirect('home')
    print(is_artist)
    return render(request, template_name='artist_registration.html', context={
        'form': form,
        'page_title': page_title,
        'is_artist': is_artist
    })


def create_post_view(request):
    page_title = 'Create Post'
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = CreatePostModel(title=form.cleaned_data['title'],
                                   text=form.cleaned_data['text'],
                                   artist=request.user.artist)
            post.save()
            return redirect('artist_posts_list')
    return render(request, template_name='post_create.html', context={
        'form': form,
        'page_title': page_title
    })


def artist_post_list_view(request):
    page_title = 'my posts'
    obj = CreatePostModel.objects.all()
    return render(request, template_name='artist_posts_list.html', context={
        'posts': obj,
        'page_title': page_title
    })

