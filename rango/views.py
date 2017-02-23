from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango says hello to the world")

def about(request):
    return HttpResponse("Rango says here is the about page")

def indexHtml(request):
    #Construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage':"I am bold font from the context"}

    #return a rendered response to send to the client
    #we make use of the shortcut function to make our lives easier
    #Note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html',context_dict)