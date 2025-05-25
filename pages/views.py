from django.shortcuts import render
from django.template.response import TemplateResponse


def article_view(request):
    return TemplateResponse(request, "pages/article.html")