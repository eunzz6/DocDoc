from django.shortcuts import redirect, render
from .models import Post
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
import os


@login_required(login_url='/')
def board(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts  
    }
    return render(request, 'board.html', context)


@login_required(login_url='/')
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'detail.html', context)


@login_required(login_url='/')
def new(request):
    return render(request, 'new.html')


@login_required(login_url='/')
def create(request):
    author = request.POST['author']
    subject = request.POST['subject']
    body = request.POST['body']
    
    if 'file' in request.FILES:  # 파일이 업로드되었는지 확인
        file = request.FILES['file']
    else:
        file = None
    
    post = Post(author=author, subject=subject, body=body, file=file, createDate=timezone.now())
    post.save()
    return redirect('board:detail', pk=post.pk)


@login_required(login_url='/')
def remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('board:board')
    return render(request, 'remove.html', {'post': post})


@login_required(login_url='/')
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        author = request.POST['author']
        subject = request.POST['subject']
        body = request.POST['body']
        
        if 'file' in request.FILES:  # 파일이 업로드되었는지 확인
            file = request.FILES['file']
        else:
            file = post.file  # 기존 파일 유지
        
        # 필요한 필드들을 업데이트
        post.author = author
        post.subject = subject
        post.body = body
        post.file = file
        post.save()
        return redirect('board:detail', pk=post.pk)

    context = {
        'post': post
    }
    return render(request, 'update.html', context)

@login_required(login_url='/')
def download_file(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.file:
        file_path = os.path.join('media', os.path.basename(post.file.name))
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404("The requested file does not exist.")
