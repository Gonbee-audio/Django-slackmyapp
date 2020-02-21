from django.shortcuts import render
from .models import Chat


def chat_text(request):
    posts = Chat.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'chatpage/chat.html', {})

# Create your views here.
