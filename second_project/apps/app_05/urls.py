from django.conf.urls import url
from . import views

#app_05
urlpatterns = [
    url(r'^(?P<number>\d+)', views.edit, name="edit" )
]