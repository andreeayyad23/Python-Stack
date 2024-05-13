from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []

    context = {
        'gold': request.session['gold'],
        'activities': request.session['activity'],
        }
    return render(request, 'index.html', context)

def process(request):
    if 'farm' in request.POST:
        Location = 'Farm'
        earned = random.randint(10,20)
    if 'cave' in request.POST:
        Location = 'Cave'
        earned = random.randint(10,20)
    if 'house' in request.POST:
        Location = 'House'
        earned = random.randint(10,20)
    if 'quest' in request.POST:
        Location = "Quest"
        earned = random.randint(-100,50)

    request.session['gold'] = request.session['gold'] + earned 

    time= strftime("%d %B, %Y %H:%M %p", gmtime())

    if earned < 0:
        message = 'You failed a '+ Location + ', and lost ' + str(earned*-1) + ' Gold... Ouch! (' +   (str(time))+")"
    else:
        message = 'You entered a '+ Location + ', and earned ' +  str(earned) + ' gold   (' +   (str(time))+")"

    request.session['activity'].append(message)

    return redirect('/') 

def reset(request):
    del  request.session['gold']
    del request.session['activity']
    return redirect('/')