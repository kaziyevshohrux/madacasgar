from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

# sport contoller 


def get_portfolio(request):
    try:
        print('\n get_portfolio')
        #portfolio model 

        return render(request, "portfolio.html", status=200 )
    except Exception as err:
        print('Error get_portfolio' ,err)
        return HttpResponseServerError('Something went wrong')


def say_hello(request):
    try:
        print('\n say_hello')
        return HttpResponse('<h1>Hello, World! from authors</h1>')
        #portfolio model 

    except Exception as err:
        print('Error say_hello' ,err)
        return HttpResponseServerError('Something went wrong')

def get_advice(request):
    try:
        print('\n get_advice')
        return HttpResponse('<h1>do wanna get advice</h1>')
        #portfolio model 

        
    except Exception as err:
        print('Error get_advice' ,err)
        return HttpResponseServerError('Something went wrong')
