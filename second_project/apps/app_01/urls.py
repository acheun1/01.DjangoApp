from django.conf.urls import url
from . import views

#app_01
urlpatterns = [
    url(r'^$', views.index, name="index" )
]
