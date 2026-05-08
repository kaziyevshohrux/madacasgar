from django.urls import path

from . import views

# sport url

urlpatterns = [
    path("", views.get_portfolio, name="get_portfolio"),
    path("say", views.say_hello, name="get_hello"),
    path("advice", views.get_advice, name="get_advice")
]