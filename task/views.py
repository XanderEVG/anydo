from django.shortcuts import render
from django.http import HttpResponse

def tasks_list(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'task/tasks_list.html', {})