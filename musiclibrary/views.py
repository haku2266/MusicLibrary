from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArtistRegisterFrom, CreatePostForm
from django.contrib.auth import get_user_model
from .models import ArtistModel, CreatePostModel
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


# def custom_404(request, exception):
#     return render(request, '404.html', status=404)


def home_view(request):
    page_title = 'home'
    obj = CreatePostModel.objects.all().select_related('artist').select_related('artist__user')[:5]
    return render(request, template_name='home.html', context={
        'page_title': page_title,
        'posts': obj
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


@login_required
def create_post_view(request):
    try:
        if request.user.artist:
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
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={
            'error': 'You need to be artist to load this page'
        })


@login_required
def artist_post_list_view(request):
    try:
        if request.user.artist:
            page_title = 'my posts'
            obj = CreatePostModel.objects.all().filter(artist__user=request.user) \
                .select_related('artist') \
                .select_related('artist__user')
            return render(request, template_name='artist_posts_list.html', context={
                'posts': obj,
                'page_title': page_title
            })
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={
            'error': 'You need to be artist to load this page'})


@login_required
def post_delete_view(request, id):
    try:
        if request.user.artist:
            obj = CreatePostModel.objects.get(id=id)
            obj.delete()
            return redirect('artist_posts_list')
    except ObjectDoesNotExist:
        return render(request, template_name='universal_error.html', context={
            'error': 'You don\'t have permission to delete posts!'
        })


def user_post_list_view(request):
    page_title = 'posts'
    obj = CreatePostModel.objects.all().select_related('artist').select_related('artist__user')
    return render(request, template_name='user_posts_list.html', context={
        'page_title': page_title,
        'posts': obj
    })


@login_required
def edit_post_view(request, id):
    page_title = 'edit post'
    obj = CreatePostModel.objects.get(id=id)
    form = CreatePostForm(instance=obj)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('artist_posts_list')

    return render(request, template_name='post_edit.html', context={
        'form': form,
        'page_title': page_title
    })


def post_detail_view(request, id):
    try:
        obj = CreatePostModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return redirect('home')
    else:
        return render(template_name='post_detail', context={
            'post': obj
        })
