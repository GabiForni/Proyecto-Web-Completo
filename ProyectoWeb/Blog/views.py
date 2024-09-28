from django.shortcuts import render
from Blog.models import Post

# Create your views here.
def blog(request):
    #cargamos los posts en una variable
    posts = Post.objects.all()

    #decimos que devuelva la plantilla y los posts
    return render(request, 'blog/blog.html', {'posts': posts})