from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Article
def index(request):
    context = {'boldmessage':'Welcome!!'}
    return render(request, 'rango/index.html', context)

def about(request):
    return HttpResponse("Here is about page!")

def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {}
        context['article_obj']= article #article_obj对应了html中的{{article_obj}}
        return render(request, "article_detail.html", context )
    except Article.DoesNotExist:
        raise Http404("not exist")
  #  return HttpResponse("<h2>文章标题 :%s</h2> <br>文章内容： %s" % (article.title, article.content))
def article_list(request):
      articles= Article.objects.filter(is_deleted=False)
      context = {}
      context['articles'] = articles
      return render(request, "article_list.html", context)





