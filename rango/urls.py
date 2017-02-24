from rango import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^indexHtml/$', views.indexHtml, name='indexHtml'),
    url(r'^indexCategory/$', views.indexCategory, name='indexCategory'),
]