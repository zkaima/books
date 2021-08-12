"""ce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01.view import views, book, author, publish

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^delete_list/(?P<id>\d+)', views.delete_list),
    url(r'^book_list/', book.book_list),
    url(r'^add_book/', book.add_book),
    url(r'^update_book/', book.update_book),
    url(r'^author_list/', author.author_list),
    url(r'^add_author/', author.add_author),
    url(r'^update_author/', author.update_author),
    url(r'^publish_list/', publish.publish_list),
    url(r'^add_publish/', publish.add_publish),
    url(r'^update_publish/', publish.update_publish),
]
