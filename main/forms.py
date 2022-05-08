from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'tesk']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'tesk': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input description'
            })            
        }