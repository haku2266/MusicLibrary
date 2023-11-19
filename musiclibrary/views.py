from django.shortcuts import render, redirect
from .forms import ConsumerForm
from django.contrib.auth import get_user_model

User = get_user_model()


def home_view(request):
    return render(request, template_name='home.html')


def consumer_create_view(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            x = form.save()
            x.save()
            return redirect('home')

    return render(request, template_name='consumercreate.html', context={
    })
