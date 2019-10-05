from django.shortcuts import render

# Create your views here.
def homepage (request):

    render(request,'homepage.html', {})

    
