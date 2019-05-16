from django.shortcuts import render

from .forms import ArticleCreateForm



def article_create_view(request):
    '''
    Create a single article
    '''
    form = ArticleCreateForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
            

    context = {
        "form":form
    }
    template_name = 'blog/blog_create.html'
    return render(request,template_name,context)