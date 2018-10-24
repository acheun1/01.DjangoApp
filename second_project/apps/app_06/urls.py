from django.conf.urls import url
from . import views

#app_06
urlpatterns = [
    url(r'^(?P<number>\d+)', views.delete, name="delete" )
]