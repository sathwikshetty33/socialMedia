from django.contrib import admin
from .models import profile, post, Follower

admin.site.register(profile)
admin.site.register(post)
admin.site.register(Follower)
