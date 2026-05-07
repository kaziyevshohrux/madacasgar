from django.http import HttpResponseServerError
from django.shortcuts import render

# sport contoller 


def get_sport(request):
    try:
        print('\n get_sport')
        #sport model 

        return render(request, "sport.html", status=200 )
    except Exception as err:
        print('Error get_sport' ,err)
        return HttpResponseServerError('Something went wrong')
