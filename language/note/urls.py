from django.conf.urls import url
from note import views
urlpatterns = [
    url(r'^$', views.note, name='note'),
    url(r'^MyNotesOnline$', views.MyNotesOnline, name='MyNotesOnline'),
]