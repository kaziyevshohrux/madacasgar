import json
from django.http import HttpResponseServerError, JsonResponse
from django.shortcuts import redirect, render
from plan.models import Plan
from django.views.decorators.csrf import csrf_exempt
plan = Plan()
# plan view (contoller)

def get_home(request):
    try:
        print('\n get_home')
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


@csrf_exempt
def create_plan(request):
    try:
        print('\ncreate_plan')
        if request.method != "POST":
            raise ValueError('only POST request are allowed!')
        
        data = json.loads(request.body)
        print('request.body' , data)

        result = plan.create_plan(data)
        return JsonResponse({'status': 'succsess',  
                             'result': result},
                               status=200)
     
    except Exception as err:
        massage = str(err)
        return JsonResponse({'status': 'fail' ,
                             'massage': massage}, 
                             status=500)

@csrf_exempt
def update_plan(request):
    try:
        print('\nupdate_plan')
        
        if request.method != "POST":
            raise ValueError('only POST request are allowed!')
        
        data = json.loads(request.body)
        print('request.body' , data)

        result = plan.update_plan(data)
        
        return JsonResponse({'status': 'succsess',  
                             'result': result},
                               status=200)
     
    except Exception as err:
        massage = str(err)
        return JsonResponse({'status': 'fail' ,
                             'massage': massage}, 
                             status=500)
    

@csrf_exempt
def delete_plan(request):
    try:
        print('\ndelete_plan')
        
        if request.method != "POST":
            raise ValueError('allowed only post method')
        
        data = json.loads(request.body)
        print('request.body', data)

        result = plan.delete_plan(data)

        return JsonResponse({'status': 'succsess',  
                             'result': result},
                               status=200)
     
    except Exception as err:
        massage = str(err)
        return JsonResponse({'status': 'fail' ,
                             'massage': massage}, 
                             status=500)


@csrf_exempt
def delete_all_plans(request):
    try:
        print('\ndelete_all_plans')
        
        if request.method != "POST":
            raise ValueError('allowed only post method')
        
     
        result = plan.delete_all_plans()

        return JsonResponse({'status': 'succsess',  
                             'result': result},
                               status=200)
     
    except Exception as err:
        massage = str(err)
        return JsonResponse({'status': 'fail' ,
                             'massage': massage}, 
                             status=500)


