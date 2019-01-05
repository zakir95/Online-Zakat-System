from django.conf.urls import url
from . import views

app_name = 'formzakat'



urlpatterns = [
    url(r'^$', views.formzakat_list, name="list"),
    url(r'^apply/$', views.apply_zakat, name="apply"),
    url(r'^document/$', views.doc_zakat, name="document"),
    url(r'^family/$', views.family_info, name="family"),
    url(r'^confirm/$', views.confirm_zakat, name="confirm"),
    url(r'^thanks/$', views.thanks, name="thanks"),
#    url(r'^doktest/$', views.dok_zakat, name="doktest"),
#    url(r'^agree/$', views.agree_info, name="agree"),
#    url(r'^generate/pdf/$', views.generate_pdf, name='generate_pdf'),

]