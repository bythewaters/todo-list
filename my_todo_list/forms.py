from django import forms
from django.forms import SelectDateWidget

from my_todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=SelectDateWidget(),
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")


class UpdateTaskTagForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ("tags",)
