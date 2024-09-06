from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.story_list,name='home'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create-story/", views.create_story, name="create_story"),
    path('story-details/<int:id>/',views.story_details,name='story_details'),
    path('add-branch/<int:id>',views.add_branch,name='add_branch'),
    path('author-profile/',views.author_profile,name='author_profile'),
]