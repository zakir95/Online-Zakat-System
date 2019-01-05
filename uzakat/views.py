from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

#def homepage(request):
   # return HttpResponse('homepage')
#    return render(request,'homepage.html')

def home(request):
   # return HttpResponse('about')
     return render(request,'home.html')

#def thanks(request):
#    return render(request,'thank_you.html')

