from django.urls import path
from . import views
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.loginview,name='login'),
    path('setting/', views.settings,name='setting'),
    path('signout/', views.logoutview,name='logout'),
    path('upload/',views.upload, name='upload')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)