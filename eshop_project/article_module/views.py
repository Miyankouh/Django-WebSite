from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView 
from article_module.models import Article


# class ArticleView(View):
    # def get(self, request):
        # articles = Article.objects.filter(is_active=True)
        # context = {
            # 'articles': articles
        # }
        # return render(request, 'article_module/articles_page.html', context)


class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'article_module/articles_page.html'
