from django.urls import path

from . import views

# sport url

urlpatterns = [
    path("", views.get_sport, name="get_sport")
]