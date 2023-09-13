from django.shortcuts import render, redirect
from .models import Tweet, Profile
from .forms import TweetForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect("TweetWiz:home")
        followed_tweets = Tweet.objects.filter(
            user__profile__in = request.user.profile.follows.all()
        ).order_by("-created_at")
        
        return render(request, "TweetWiz/dashboard.html", {"form": form, "tweets":followed_tweets})
    else:
        return render(request, "TweetWiz/dashboard.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "TweetWiz/profile_list.html", {"profiles":profiles})

def profile(request, pk):
    if not hasattr(request.user, "profile"):
        newprofile = Profile(user=request.user)
        newprofile.save()
    
   
    profile = Profile.objects.get(pk=pk)
    # request.user.profile = logged-in user.
    # profile = OTHER user.
    if request.method == "POST":
        curr_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            curr_user_profile.follows.add(profile)
        elif action == "unfollow":
            curr_user_profile.follows.remove(profile)
        curr_user_profile.save()
    return render(request, "TweetWiz/profile.html", {"profile":profile})

