from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def index(request):
    return redirect('shows/')

def showsAll(request):
    context={
        'shows':Show.objects.all(),
    }
    return render(request, 'read_all.html', context)

def go_create(request):
    return render(request, 'create.html')

def create_show (request):
    if request.method=="POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            newShow= Show.objects.create(
                title= request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                description=request.POST['description']
            )
            newShow.save()
            messages.success(request, "Show successfully Added!")
            return redirect(f'/shows/{newShow.id}')
    return redirect('/shows/new')


def readOne(request, _id):
    context={
        'show':Show.objects.get(id=_id)
    } 
    return render(request,'read_one.html',context)

def go_edit(request,_id):
    context={
        'show': Show.objects.get(id=_id)
    }
    return render(request, 'update.html',context)

def edit_show(request,_id):
    if request.method=='POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0 :
            for key, value in errors.items():
                messages.error(request, value)

        else:
            edit_show= Show.objects.get(id=_id)
            edit_show.title= request.POST['title']
            edit_show.network=request.POST['network']
            edit_show.release_date=request.POST['release_date']
            edit_show.description=request.POST['description']
            edit_show.save()
            messages.success(request, "Show successfully Update!")
            return redirect(f'/shows/{_id}')
    return redirect(f'/shows/{_id}/edit')




def delete_show(request, _id):
    show = Show.objects.get(id=_id)
    show.delete()
    return redirect('/')