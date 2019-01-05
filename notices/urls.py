from django.conf.urls import url
from . import views

app_name = 'notices'

urlpatterns = [
    url(r'^$', views.notice_app, name="note"),
#    url(r'^note/$', views.notice_app, name="note"),
#    url(r'^document/$', views.doc_zakat, name="document"),
#    url(r'^family/$', views.family_info, name="family"),

]