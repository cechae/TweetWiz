from django.conf.urls import url, include
from django.urls import path
from .views import home, profile_list, profile, register
from django.contrib.auth import views as auth_views


app_name = "TweetWiz"
urlpatterns = [
    url(r"profile_list/", profile_list, name = "profile_list"),
    url(r"profile/<int:pk>", profile, name = "profile"),
    
    url(r'^accounts/', include("django.contrib.auth.urls" )),
    url(r"^register/", register, name="register"),
    url(r"^", home, name="home"),
    
]