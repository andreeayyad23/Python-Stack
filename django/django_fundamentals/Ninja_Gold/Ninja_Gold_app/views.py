from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activity'],
        }
    return render(request, 'index.html', context)

def process(request):
    if request.POST['location'] == 'Farm' or request.POST['location'] == 'Cave' or request.POST['location'] == 'House':
        earned = random.randint(10,20)
    if request.POST['location'] == "Quest":
        earned = random.randint(-100,50)

    request.session['gold'] = request.session['gold'] + earned 

    time= strftime("%d %B, %Y %H:%M %p", gmtime())

    if earned < 0:
        message = 'You failed a '+ request.POST['location'] + ', and lost ' + str(earned*-1) + ' Gold... Ouch! (' +   (str(time))+")"
    else:
        message = 'You entered a '+ request.POST['location'] + ', and earned ' +  str(earned) + ' gold   (' +   (str(time))+")"

    request.session['activity'].append(message)

    return redirect('/') 

def reset(request):
    del  request.session['gold']
    del request.session['activity']
    return redirect('/')