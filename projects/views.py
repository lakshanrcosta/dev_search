from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    msg = 'This this the project page'
    return render(request, 'projects/projects.html', {'message': msg})


def project(request, id):
    return render(request, 'projects/single-project.html')
