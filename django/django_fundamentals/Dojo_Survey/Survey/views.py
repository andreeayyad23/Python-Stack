from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def result(request):
    if request.method == 'POST':
        context = {
            'name': request.POST['name'],
            'location': request.POST['location'],
            'language': request.POST['language'],
            'comment': request.POST['comment'],
        }
    return render (request, 'result.html', context)