from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'projects_count': models.Project.objects.count(),
        'tasks_count': models.Task.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'pages/index.html', context)

def task_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/task_list.html',
                  {'task_list': models.Task.objects.all(),})
