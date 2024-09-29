from django.shortcuts import render
from Blog.models import Post, Categoria

# Create your views here.
def blog(request):
    #listamos todos los posts y los almacenamos en una variable
    posts = Post.objects.all()

    #decimos que devuelva la plantilla y los posts
    return render(request, 'blog/blog.html', {'posts': posts})


def categoria(request, categoria_id):
    #filtramos las categorias por id
    categoria = Categoria.objects.get(id=categoria_id)
    #filtramos los posts por categoria
    posts = Post.objects.filter(categorias=categoria)
    #retornamos la categoria filtrada y los posts
    return render(request, 'blog/categoria.html', {'categoria': categoria,'posts': posts})