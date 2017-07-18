from django.conf.urls import url
from . import views           # This line is new!

#models -- views -- templates

urlpatterns = [
  url(r'^$', views.index),
  url(r'^surveys/process$', views.process),
  url(r'^result$', views.result),     # This line has changed!
 ]