from django.shortcuts import render
from .models import Post
# Create your views here.
def board_main(request):
    Postlist = Post.objects.all()
    return render(request, 'board.html', {'postlist':Postlist})