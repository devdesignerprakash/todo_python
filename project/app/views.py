from django.shortcuts import render
from .forms import TaskForm

def home_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            form = TaskForm()
    else:
        form = TaskForm()

    context = {
        "form": form 
    }

    return render(request, 'app/home.html', context)