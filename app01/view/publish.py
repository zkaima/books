from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from app01 import models


# 出版社页面
def publish_list(request):
    publishs = models.Publish.objects.all()
    return render(request, 'publish_list.html', {'publishs':publishs})


# 新增出版社
def add_publish(request):
    if request.method == 'GET':
        return render(request, 'add_publish.html')
    else:
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        res = models.Publish.objects.create(name=name, addr=addr, email=email)
        return redirect('/publish_list/')


# 编辑出版社
def update_publish(request):
    if request.method == 'GET':
        publish_id = request.GET.get('id')
        publish = models.Publish.objects.get(pk=publish_id)
        return render(request, 'update_publish.html', {'publish':publish})
    else:
        publish_id = request.GET.get('id')
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        publish_id = models.Publish.objects.filter(pk=publish_id)
        res = publish_id.update(name=name, addr=addr, email=email)
        return redirect('/publish_list/')