from django.contrib.auth.decorators import login_required

from .models import *

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from .forms import *

@login_required(login_url='login')
def home(request):
    user = request.user
    p = get_object_or_404(profile, user=user)
    po = post.objects.select_related('users').all()
    return render(request, 'index.html',{'p' : p,'po':po})
@login_required(login_url='login')
def upload(request):
    user = request.user
    p = get_object_or_404(profile,user=user)
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption')
        obj = post.objects.create(users=p,image=image,caption=caption)
        obj.save()
        return redirect('home')
    else:
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = usercreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            pro=profile.objects.create(user=user,userid=user.id)
            pro.save()
            return redirect('login')
        else:

            print(form.errors)
            return render(request, 'signup.html', {'form': form})
    else:
        form = usercreation()
        return render(request, 'signup.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        form = authentication(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(request, username=username, password=password)

            if user is not None:
                 login(request,user)
                 return redirect('home')

            else:
                 messages.error(request,'enter correct details')
                 return render(request,'signin.html', {'form': form})
        else:
            messages.error(request, 'enter correct details')
            return render(request, 'signin.html', {'form': form})
    else:
        form = authentication
        return render(request,'signin.html',{'form': form})
@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('login')


@login_required
def settings(request):
    user = request.user
    p = profile.objects.filter(user=user).first()
    if request.method == 'POST':
        if 'profimg' in request.FILES:
            print("Received image:", request.FILES['profimg'])
            p.profimg = request.FILES['profimg']
        else:
            print("No image file received in request.FILES")

        p.bio = request.POST.get('bio', '')
        p.loc = request.POST.get('location', '')
        p.working = request.POST.get('working', '')  # Added this line to save 'working' field
        p.save()
        return redirect('home')
    return render(request, 'setting.html', {'p': p})
