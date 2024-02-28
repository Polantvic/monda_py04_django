from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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

def task_detail(request: HttpRequest, pk:int) -> HttpResponse:
    return render(request, 'pages/task_detail.html',
                  {'task': get_object_or_404(models.Task, pk=pk),})

def task_done(request: HttpRequest, pk:int) -> HttpResponse:
    task = get_object_or_404(models.Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    messages.success(request, f'Task "{task}" marked as '
                f"{'done' if task.is_done else 'undone'}.")
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))
    return redirect(task_list)
