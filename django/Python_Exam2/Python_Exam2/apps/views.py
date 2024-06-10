from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Magazine
import bcrypt

def index(request):
    return render(request, "Login.html")

def registration(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(
                firstname=request.POST['firstname'],
                lastname=request.POST['lastname'],
                email=request.POST['email'],
                password=hashed_pw
            )
            request.session['user_id'] = newUser.id
            return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            log_user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = log_user.id
            return redirect('/dashboard')
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'magazines': Magazine.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "dashboard.html", context)

def go_create(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'magazines': Magazine.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'create_magazine.html', context)

def add_magazine(request):
    if request.method == 'POST':
        errors = Magazine.objects.magazine_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/magazines/new')
        else:
            this_user= User.objects.get(id=request.session['user_id'])
            magazine=Magazine.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                uploaded_py = this_user
            )
            magazine.user_who_add.add(this_user)
            # this_user.liked_books.add(this_book)
            magazine.save()
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')
    
def info_magazine(request, _id):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user':User.objects.get(id=request.session['user_id']),
        'magazine':Magazine.objects.get(id = _id)
    }
    return render (request, "details.html", context)

def edit(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'magazines': Magazine.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, "update.html", context)

def edit_user(request):
    if request.method == 'POST':
        errors = User.objects.update_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/user/account')
        else:
            this_user = User.objects.get(id=request.session['user_id'])

            this_user.firstname = request.POST['firstname']
            this_user.lastname = request.POST['lastname']
            this_user.email = request.POST['email']

            this_user.save()

            messages.success(request, "User successfully updated!")
            return redirect('/user/account')
    else:
        return redirect('/user/account')
    
def delete_title(request, _id):
        print("estTesttesttest")

        magazine = Magazine.objects.get(id=_id)
        user_id = request.session.get('user_id')

        # Check if the current user is the one who uploaded the magazine
        # print("estTesttesttest"+magazine.uploaded_py)

        if user_id == magazine.uploaded_py.id: 
            magazine.delete()
            messages.success(request, "Magazine deleted successfully.")
        else:
            messages.error(request, "You are not authorized to delete this magazine.")

        return redirect('/user/account')


def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')
