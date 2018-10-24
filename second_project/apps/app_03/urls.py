from django.conf.urls import url
from . import views

#app_03
urlpatterns = [
    url(r'^$', views.create, name="create" )
]