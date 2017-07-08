from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^index/$', views.Index, name='index'),
    url(r'^about/$', views.About, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^link/$', views.Link, name='link'),
    url(r'^message/$', views.Message, name='message'),
    url(r'^article/(?P<pk>\d+)$', views.Articles, name='article'),
    url(r'^get_comment/$', views.GetComment, name='get_comment'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<name>.*?)$', views.tag, name='tag'),
    url(r'.*?$', views.Index, name='index'),
]
