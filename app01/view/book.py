from django.shortcuts import render,redirect

# Create your views here.
from app01 import models


def book_list(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books':books})


# book 新增
def add_book(request):
    if request.method == 'GET':
        authors = models.Author.objects.all()
        publishs = models.Publish.objects.all()
        return render(request, 'add_book.html', locals())
    else:
        authors = request.POST.getlist('authors')
        name = request.POST.get('name')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')
        res = models.Book.objects.create(name=name, price=price, pub_date=pub_date, publish_id=publish)
        res.authors.add(*authors)
        return redirect('/book_list/')


# 编辑图书
def update_book(request):
    if request.method == 'GET':
        # 把这本书取出来，需要书的id号
        book_id=request.GET.get('id')
        book=models.Book.objects.get(pk=book_id)
        authors=models.Author.objects.all()
        publishs=models.Publish.objects.all()
        return render(request, 'update_book.html', locals())
    else:
        # 几种方案
        # 第一种方案
        # book_id = request.POST.get('id')
        # 第二种方案
        book_id = request.GET.get('id')
        data = request.POST
        authors = request.POST.getlist('authors')
        name = request.POST.get('name')
        price = request.POST.get('price')
        pub_date = request.POST.get('pub_date')
        publish = request.POST.get('publish')

        book_queryset=models.Book.objects.filter(pk=book_id)
        res=book_queryset.update(name=name,price=price,pub_date=pub_date,publish_id=publish)
        book_queryset.first().authors.set(authors)
        return redirect('/book_list/')