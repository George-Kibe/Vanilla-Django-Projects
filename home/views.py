from django.shortcuts import render, redirect
from home.models import Task
from .forms import *

# Create your views here.
def home(request):
    context = {'success': False}#by default
    if request.method == "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        randomno=request.POST.get('randomno')
        #randomno=request.data.get('randomno')
        print(request.POST)
        #date_time=request.POST['']
        #print(title, desc)
        ins = Task(taskTitle=title, taskdesc=desc, randomno=randomno)
        #first name is one in model second is one in this function
        ins.save()
        context = {'success': True}
    return render(request, 'home/index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'home/tasks.html', context)

def test(request):   
    return render(request, 'home/test.html')

def updateTask(request, pk):
    task=Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method=='POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}

    return render(request, 'home/updatetask.html', context)

def deleteTask(request, pk):    
    context = {'success': False}#by default
    item=Task.objects.get(id=pk)
    if request.method=='POST':        
        item.delete()
        return redirect('/')
    context[0]= {'success': True} 
    context[1]= {'item': item}   
    return render(request, 'home/deletetask.html', context)