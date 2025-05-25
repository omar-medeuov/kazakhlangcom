from django.shortcuts import render
from django.template.response import TemplateResponse

import markdown

from .models import Article

def article_view(request, article_url):

    article = Article.objects.get(title=article_url)

    markdown_content = markdown.markdown(article.content, extensions=['extra', 'codehilite'])

    return TemplateResponse(request, "pages/article.html", context={
        "article": article,
        "markdown_content": markdown_content,
    })