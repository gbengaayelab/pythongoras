from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse

from .forms import NewUserForm
from .models import Tutorials, TutorialSeries, TutorialsCategory


def single_slug(request, single_slug):
    categories = [c.category_link for c in TutorialsCategory.objects.all()]
    if single_slug in categories:
        # This next Line of code is referencing Tutorial_series model of the attribute Tutorial_category Foreign Keys and reference the category link in the Tutorial Category
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_link=single_slug)
        # This next line of code matches the tutorials in the matching series together
        series_url = {}
        for matching in matching_series.all():
            first_part = Tutorials.objects.filter(tutorial_series__tutorial_series=matching.tutorial_series).earliest('tutorial_published_date')
            series_url[matching] = first_part

        return render(request=request,
                      template_name='main/category.html',
                      context={'first_part': series_url})

    tutorials = [t.tutorial_link for t in Tutorials.objects.all()]
    if single_slug in tutorials:
        return HttpResponse(f'{single_slug} is in tutorial')

    return HttpResponse(f'{single_slug} does not correspond to any path')


def index(request):
    categories = TutorialsCategory.objects.all()
    return render(request=request,
                  template_name='main/categories.html',
                  context={'categories': categories})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account Created:{username}')
            login(request, user)
            messages.info(request, f'You are now logged in:{username}')
            return redirect('main:index')
        else:
            for error_message in form.error_messages:
                messages.error(request, f'{error_message}: {form.error_messages[error_message]}')

    form = NewUserForm
    return render(request,
                  'main/register.html',
                  context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged Out!')
    return redirect('main:index')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in:{username}')
                return redirect('main:index')
            else:
                messages.error(request, "Invalid username or password")
        messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  'main/login.html',
                  {'form': form})
