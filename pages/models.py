from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(help_text="Markdown format is to be used.")
    date_published = models.DateTimeField(auto_now_add=True)

