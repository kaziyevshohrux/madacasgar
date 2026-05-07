from django.http import HttpResponseServerError
from django.shortcuts import render

# tour contoller 


def get_tour(request):
    try:
        print('\n get_tour')
        #tour model 

        return render(request, "tour.html", status=200 )
    except Exception as err:
        print('Error get_tour' ,err)
        return HttpResponseServerError('Something went wrong')

