from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from app01 import models


# 作者页面
def author_list(request):
    authors = models.Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


# 新增作者
def add_author(request):
    if request.method == 'GET':
        return render(request, 'add_author.html', locals())
    else:
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        res = models.Author.objects.create(name=name, sex=sex)
        return redirect('/author_list/')


# 编辑作者
def update_author(request):
    if request.method == 'GET':
        author_id = request.GET.get('id')
        author = models.Author.objects.get(pk=author_id)
        return render(request, 'update_author.html', {'author':author})
    else:
        author_id = request.GET.get('id')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        aothor_id = models.Author.objects.filter(pk=author_id)
        res = aothor_id.update(name=name, sex=sex)
        return redirect('/author_list/')