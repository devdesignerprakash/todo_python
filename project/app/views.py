from django.shortcuts import render

def home_view(request):
   return render(request,'app/home.html')

# Create your views here.
