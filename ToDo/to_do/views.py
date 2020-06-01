from django.shortcuts import render
from to_do.models import Agenda
from django.http import HttpResponse
from django.core import serializers


def list_tasks(request):
    my_tasks = Agenda.objects.filter(done=False)
    context = {
        'tasks': my_tasks,
    }
    return render(request, "todo_list.html", context)


def save_task(request):
    print(request.POST.get('content'))
    if request.POST.get('content') != "":
        new_task = Agenda.objects.create(content=request.POST.get('content'))
        task = Agenda.objects.filter(id=new_task.id)
        task_json = serializers.serialize('json', task)
        return HttpResponse(task_json, content_type='application/json')


def delete_task(request):
    checked_task = Agenda.objects.filter(id=request.POST.get('task_id'))
    field = 'done'
    checked = Agenda.objects.values_list(field, flat=True).get(id=request.POST.get('task_id'))
    print(checked)
    if checked is True:
        print("if")
        Agenda.objects.filter(id=request.POST.get('task_id')).update(done=False)
    else:
        print("else")
        Agenda.objects.filter(id=request.POST.get('task_id')).update(done=True)
    task_json = serializers.serialize('json', checked_task)
    return HttpResponse(task_json, content_type='application/json')



