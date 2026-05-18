from django.urls import path

from . import views
# traditional API
 
urlpatterns = [
    # traditional API
    path("", views.get_home, name="get_home"),
    path('create-goal', views.create_goal, name='create_goal'),

    # REST API 
    path('create-plan', views.create_plan, name='create_plan'),
    path('update-plan', views.update_plan, name='update_plan'),
    path('delete-plan', views.delete_plan, name='delete_plan')

]

# plan url ``