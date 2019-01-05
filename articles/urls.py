from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from .import views
from .views import GeneratePdf

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
    url(r'^home/$', views.home_create, name="home"),
    url(r'^pdf/$', views.GeneratePdf.as_view(), name="pdf"),
]

