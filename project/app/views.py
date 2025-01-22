from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import*

def home_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            form = TaskForm()
            return redirect('home')
    else:
        form = TaskForm()
    tasks=TaskManager.objects.all()
    
    context = {
        "form": form,
        "tasks":tasks
    }

    return render(request, 'app/home.html', context)

def update_task(request,pk):
    task = get_object_or_404(TaskManager, pk=pk)
    if request.method=="POST":
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = TaskForm()
    context = {
            'form': form,
             'task': task
        }
    return render(request,'app/update_task.html',context)


def delete_task(request,pk):
    task= get_object_or_404(TaskManager,id=pk)
    task.delete()
    return redirect('home')
    


    
