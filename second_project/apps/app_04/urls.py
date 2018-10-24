from django.conf.urls import url
from . import views

#app_04
urlpatterns = [
    url(r'^(?P<number>\d+)', views.show, name="show" )
]