from django.shortcuts import render,redirect

# Create your views here.
from app01 import models


# 主页面
def index(request):
    return render(request, 'index.html')


# 各个页面删除
def delete_list(request, id):
    res = models.Book.objects.filter(pk=id).delete()
    authors = models.Author.objects.filter(pk=id).delete()
    publishs = models.Publish.objects.filter(pk=id).delete()
    return redirect('/book_list/')











