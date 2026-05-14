from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from plan.models import Plan
from django.views.decorators.csrf import csrf_exempt
plan = Plan()
# plan view (contoller)

def get_home(request):
    try:
        print('\n get_home')
        #view model
        plans = plan.get_home()
        return render(request, "home.html", {"plans": plans}, status=200 )
    except Exception as err:
        print('Error get_home' ,err)
        return HttpResponseServerError('Something wrong')

@csrf_exempt
def create_goal(request):
    try:
        print('\ncreate_goal')
        if request.method != "POST":
            raise ValueError('only POST request are allowed!')
        content = request.POST.get("content")
        plan.create_goal(content)
        return redirect("/")
    except Exception as err:
        print('Error create_goal' ,err)
        return HttpResponseServerError('creation is fail')
