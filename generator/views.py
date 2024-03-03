from django.shortcuts import render
from django.http import HttpResponse # mene add ki, nahi  toh exceptional error de raha tha
import random # This alow us to create some rendomness
# Create your views here.
# khud se create kiya
def home(request):      # request is a parameter here
    # return HttpResponse('I am Batman')

    # 'render' is function from django that allows you to pass back a template
    # that turns into an HttpResponse
    # return render(request, 'generator/home.html') #  this is pulling the html file frome "home.html"
    return render(request, 'generator/home.html') # This dictionary is pass forward to "home.html" file

# def eggs(request):
#     return HttpResponse("Eggs are so tasty")

def about(request):
    return render(request,'generator/about.html')


def password(request): # this "request" parameter contains the data

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

     # We use this data to manipuliate the length. Isliye html file mai "select=length" kiya tha
    length =int(request.GET.get('length',12)) # 12 is a default value here
    thePassword = ''

    for x in range(length):
        thePassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password':thePassword})
