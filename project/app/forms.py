from django import forms
from .models import TaskManager

class TaskForm(forms.ModelForm):
 class Meta:
    model=TaskManager
    fields=['name','desc','deadline']
    labels = {
            'desc': 'Description',
        }
    widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }
