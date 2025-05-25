from django.urls import path

from .views import article_view

urlpatterns = [
    path("<str:article_url>/", article_view, name="article-view"),

]