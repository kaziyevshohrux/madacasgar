from django.urls import path

from . import views
 
urlpatterns = [
    path("", views.get_home, name="get_home")

]

# plan url 