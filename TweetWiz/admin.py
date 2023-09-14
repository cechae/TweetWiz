from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group #fetch the built-in User model from
from .models import Profile, Tweet # importing a model class defined within the same Django app/package/module.


class ProfileInline(admin.StackedInline):
    model = Profile
    
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Tweet)
admin.site.register(Profile)