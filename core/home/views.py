from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
def home(request):


    peoples = [
        {'name': "abhijeet sing",
         'age': 34,
         },
         {'name': "Rohan sharma",
         'age': 14,
         }
         ,
         {'name': "hemanshu",
         'age': 19,
         }
    ] 
    return render(request,'index.html',context={'peoples':peoples})

def sucess_page(request):
    return HttpResponse('<h1>hey this is sucess page <h1>')

def add(request):
    m = int (input('enter num1 '))
    n = int (input ('enter num2 '))
    return HttpResponse(n+m)