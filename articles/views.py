from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from .import forms

from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")

def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save articles to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create.html', {'form':form})


@login_required(login_url="/accounts/login/")
def home_create(request):
    return render(request, 'articles/homepage.html')



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('article_test.html')
        info = Article.objects.all()
        data = {
             #'today': datetime.date.today(),
            'title': {{info.title}},
            'body':{{info.body}},
            'amount': 39.99,
#            'customer_name': 'Cooper Mann',
#            'order_id': 1233434,
        }
        html = template.render(data)
        data = render_to_pdf('article_test.html')
        return HttpResponse(html)