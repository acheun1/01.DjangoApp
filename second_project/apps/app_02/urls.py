from django.conf.urls import url
from . import views

#app_02
urlpatterns = [
    url(r'^$', views.new, name="new" )
]