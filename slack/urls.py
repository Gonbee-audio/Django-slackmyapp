from rest_framework import routers
from django.urls import path
from .views import SignUpView, Login, ChatModel, SendChatModel


urlpatterns = [
    path('', ChatModel, name="chat"),
    path('', SendChatModel, name='send'),
    path('create/', SignUpView, name="create"),
    path('login/', Login, name="login")
]

