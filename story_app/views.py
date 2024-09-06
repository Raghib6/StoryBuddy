from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.db.models import F  
from .models import Story
from .forms import UserSignUpForm,StoryForm
from .decorators import unauthenticated_user


def story_list(request):
    user = request.user
    stories = Story.objects.filter(parent=None)
    return render(request, 'index.html', {'user':user,'stories': stories})


def story_details(request, id=None):
    user = request.user
    story = Story.objects.get(id=id)
    checked = False
    if story.author == user:
        checked = True
    if user != story.author:
        story.views = F('views') + 1
        story.save()
    story = Story.objects.get(id=id)
    branches = Story.objects.filter(parent=story)
    context = {'id':story.id,'story': story,'branches':branches,'checked':checked}
    return render(request, 'story-details.html', context)



@unauthenticated_user
def signup(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Congratulations! Your account creation successfull'
            )
            return redirect('login')
    return render(request, 'signup.html', {'form': form})


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Invalid Login credential')
            return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('login')

@login_required(login_url='login')
def create_story(request):
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            story = form.save()
            return redirect('story_details',id=story.id)
    else:
        form = StoryForm()

    return render(request, 'create-story.html', {'form': form})

@login_required(login_url='login')
def add_branch(request, id=None):
    story = Story.objects.get(id=id)
    user = request.user
    if story.author == user:
        if request.method == 'POST':
            form = StoryForm(request.POST)
            if form.is_valid():
                branch = form.save(commit=False)
                branch.parent = story
                branch.author = request.user
                branch.save()
                return redirect('story_details', id=id)
        else:
            form = StoryForm()
    else:
        return redirect('story_details',id=story.id)
    return render(request, 'create-story.html', {'form': form,'branch':True})

@login_required(login_url='login')
def author_profile(request):
    author = request.user
    stories = author.stories.all()
    total_stories = stories.count()
    context = {'author':author,'stories':stories,'total_stories':total_stories}
    return render(request, 'author-details.html', context)