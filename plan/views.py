from django.http import HttpResponseServerError
from django.shortcuts import render
from plan.models import Plan
plan = Plan()
# plan view (contoller)

def get_home(request):
    try:
        print('\n get_home')
        #view model
        plan.get_home()
        
        return render(request, "home.html", {}, status=200 )
    except Exception as err:
        print('Error get_home' ,err)
        return HttpResponseServerError('Something wrong')
