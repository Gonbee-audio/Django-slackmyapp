from django.shortcuts import render, redirect
from .models import UserCreate
from .forms import ChatTextModel
from django.utils import timezone
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def SignUpView(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        try:
            User.objects.get(username=username1)
            return render(request, 'signup.html', {'error':'この名前は使えません'})
        except:
            user = User.objects.create_user(username1, '', password1)
            return render(request, 'signup.html', {})
    return render(request, 'signup.html', {})

def Login(request):
    if request.method == 'POST':
        LoginUsername = request.POST['username']
        PasswordUsername = request.POST['password']
        user = authenticate(username=LoginUsername, password=PasswordUsername)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            return render(request, 'registration/login.html', {'LoginError':'ログインに失敗しました'})
    return render(request, 'registration/login.html', {})

def ChatModel(request):
    object = UserCreate.objects.all()
    return render(request, 'chatpage/chat.html', {'object':object})

def SendChatModel(request):
    if request.method == POST:
        usertext = UserText()
        usertext.text = form.cleaned_data['text']
        usertext.username = form.cleaned_data['username']
        usertext.images = form.cleaned_data['images']
        usertext.good = form.cleaned_data['good']

        UserText.objects.create(
            text=usertext.text,
            images=usertext.images,
            good=usertext.good,
            username=usertext.username,
        )
        return render(request, 'chatpage/chat.html', {})
    return render(request, 'chatpage/chat.html', {})

    
