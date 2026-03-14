from django.shortcuts import render

from articles.models import Article


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
