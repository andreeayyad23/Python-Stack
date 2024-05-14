from django.shortcuts import render,redirect
from .models import Users
def index(request):
    data={
        "users": Users.objects.all()
    }
    return render(request, 'index.html',data)

def create(request):
    if request.method == 'POST':
        adduser= Users.objects.create(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email_address=request.POST['email'],
            age=request.POST['age'],
        )
        adduser.save()
    return redirect('/')