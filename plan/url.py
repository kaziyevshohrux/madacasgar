from django.urls import path

from . import views
# traditional API
 
urlpatterns = [
    path("", views.get_home, name="get_home"),
    path('create-goal', views.create_goal, name='create_goal')

]

# plan url 