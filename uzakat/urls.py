"""uzakat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as account_views
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^notices/', include('notices.urls')),
    url(r'^formzakat/', include('formzakat.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^home/$', views.home, name="home"),
    #url(r'^thanks/$', views.thanks, name="thanks"),
    url(r'^$', account_views.login_view, name="login"),
    #url(r'^$',views.homepage),

]

#urlpatterns +=staticfiles_urlpatterns()
#urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns += [
#        url(r'^media/(?P<path>.*)$', serve, {
#            'document_root': settings.MEDIA_ROOT,
#        }),
#    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

