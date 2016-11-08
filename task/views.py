from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    #return HttpResponse("Hello, You're at the tasks index.")
    return render(request, 'task/tasks_list.html', {})
    
def new(request):
    return render(request, 'task/new.html', {})
    
def detail(request, task_id):
    return render(request, 'task/detail.html', {})
    
def edit(request, task_id):
    return render(request, 'task/edit.html', {})