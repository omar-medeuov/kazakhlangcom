from django.shortcuts import render
from django.template.response import TemplateResponse

from .models import Article

def article_view(request, article_url):

    article = Article.objects.get(title=article_url)

    return TemplateResponse(request, "pages/article.html", context={
        "article": article,
    })