from django.conf.urls import url, include
from .views import home, profile_list, profile
from django.urls import path, include, re_path


app_name = "TweetWiz"
urlpatterns = [
    path("", home, name="home"),
    path("profile_list/", profile_list, name = "profile_list"),
    path("profile/<int:pk>", profile, name = "profile"),
    
    url(r'^accounts/', include("django.contrib.auth.urls")),
    
    
]