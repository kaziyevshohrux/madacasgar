from django.urls import path

from . import views

# tour urls

urlpatterns = [
    path("", views.get_tour, name="get_tour")
]