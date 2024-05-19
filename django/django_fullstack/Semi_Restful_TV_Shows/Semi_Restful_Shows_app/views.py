from django.shortcuts import render, redirect
from .models import *

def index(request):
    return redirect('/shows')

def showsAll(request):
    data={
        'shows':Show.objects.all(),
    }
    return render(request, 'read_all.html', data)

def go_create(request):
    return render(request, 'create.html')

def create_show (request):
    if request.method=="POST":
        newShow= Show.objects.create(
            title= request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        newShow.save()
        return redirect(f'/shows/{newShow.id}')
    return redirect('/')

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
        edit_show= Show.objects.get(id=_id)
        edit_show.title= request.POST['title']
        edit_show.network=request.POST['network']
        edit_show.release_date=request.POST['release_date']
        edit_show.description=request.POST['description']
        edit_show.save()
    return redirect(f'/shows/{_id}')


def delete_show(request, _id):
    show = Show.objects.get(id=_id)
    show.delete()
    return redirect('/')