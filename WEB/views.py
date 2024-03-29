from django.shortcuts import render
from django.views.decorators.cache import never_cache


def index(request):
    return render(request,'login/login.html')

def success(request):
    return render(request, 'success.html')

@never_cache
def contact(request):
    return render(request, 'contact.html')

def search_main(request):
    return render(request, 'search.html')

@never_cache
def about(request):
    return render(request,'about.html')

def save_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES.get('audio')
        if audio_file:
            with open('path/to/save/recording.webm', 'wb') as f:
                for chunk in audio_file.chunks():
                    f.write(chunk)