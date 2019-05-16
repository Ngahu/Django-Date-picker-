from django.shortcuts import render

from .forms import ArticleCreateForm



def article_create_view(request):
    '''
    Create a single article
    '''
    form = ArticleCreateForm(request.POST or None)
    context = {
        "form":form
    }
    template_name = 'blog/blog_create.html'
    return render(request,template_name,context)