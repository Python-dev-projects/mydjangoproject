from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "desc"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            })
        }
