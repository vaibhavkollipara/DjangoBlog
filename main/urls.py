from django.conf.urls import url
from . import views

app_name="main"

urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^details/(?P<slug>[a-zA-Z0-9-]+)/$', views.detail, name="detail"),
    url(r'^newpost/$', views.new_post , name="newpost"),
    url(r'^update/(?P<slug>[a-zA-Z0-9-]+)/$', views.update_post, name="update"),
    url(r'^delete/(?P<slug>[a-zA-Z0-9-]+)/$',views.delete_post , name="delete")
]
