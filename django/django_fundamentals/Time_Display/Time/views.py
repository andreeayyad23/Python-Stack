from django.shortcuts import render
from time import gmtime, strftime

def Hours(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime())
       
    }
    return render(request,'index.html', context)