from django.shortcuts import render, redirect
from Dojos_Ninja_app.models import Dojo, ninja
from .models import *

def index(request):
    context ={
        'dojos':Dojo.objects.all(),
        'ninjas':ninja.objects.all(),
        }
    
    return render(request,'index.html',context)

def addDojo(request):
    if request.method == 'POST':
        newDojo= Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state'],
        )
        newDojo.save()
    return redirect('/')

def addNinja(request):
    if request.method == 'POST':
        newNinja= ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id=Dojo.objects.get(id=request.POST['dojo'])
        )
        newNinja.save()
    return redirect('/')

def delete(request, _id):
    dojo = Dojo.objects.get(id=_id)
    dojo.delete()
    
    return redirect('/')

def count_ninjas(request, dojo_id):
    dojo = Dojo.objects.get(id = dojo_id)
    count = 0
    for ninja in dojo.ninjas:
        count +=1
    print(count)
    return redirect("/")