from django import forms
from reminderlist import models

class TodolistForms(forms.ModelForm):
    class Meta:
        model = models.Todolist
        fields = '__all__'