from django.http import HttpResponseServerError
from django.shortcuts import render

# plan view (contoller)

def get_home(request):
    try:
        print('get_home')
        #view
        data = "MIT"
        return render(request, "home.html", {"plans": data}, status=200 )
    except Exception as err:
        print('Error get_home' ,err)
        return HttpResponseServerError('Something wrong')
