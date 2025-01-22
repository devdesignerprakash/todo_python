from django.shortcuts import render
from .forms import TaskForm
from .models import*

def home_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            form = TaskForm()
    else:
        form = TaskForm()
    tasks=TaskManager.objects.all()

    context = {
        "form": form,
        "tasks":tasks
    }

    return render(request, 'app/home.html', context)
