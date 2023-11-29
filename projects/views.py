from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


class PostDetailView(DetailView):
    model = Article
    template_name = 'projects/detail_view.html'
    context_object_name = 'article'

class PostUpdateView(UpdateView):
    model = Article
    template_name = 'projects/create_post.html'
    form_class = ArticleForm

class PostDeleteView(DeleteView):
    model = Article
    success_url = '/projects/'
    template_name = 'projects/delete_post.html'

def projects_home(request):
    posts = Article.objects.all()
    return render(request, 'projects/projects_home.html', {'posts': posts})

def create_post(request):
    error = ''

    if request.method == 'POST':
        if request.user.is_superuser:
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('projects_home')
            else:
                error = 'Форма некорректно заполнена.'
        else:
            error = 'Только админ может создавать и редактировать посты'

    #else:
    #    return redirect('projects_home')

    form = ArticleForm
    data = {
        'form' : form,
        'error' : error
    }

    return render(request, 'projects/create_post.html', data)


