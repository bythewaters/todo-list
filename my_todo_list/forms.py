from django import forms
from django.forms import SelectDateWidget

from my_todo_list.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=SelectDateWidget(
            attrs=(
                {"class": "deadline"}
            )
        ),
        required=False,
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def clean(self) -> dict:
        cleaned_data = super().clean()
        tags = cleaned_data.get("tags")
        if not tags:
            cleaned_data["tags"] = None
        return cleaned_data

    class Meta:
        model = Task
        fields = ("content", "deadline")


class UpdateTaskTagForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ("tags",)


class TaskUpdateForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=SelectDateWidget(
            attrs=(
                {"class": "deadline"}
            )
        ),
        required=False,
    )

    class Meta:
        model = Task
        fields = ("content", "deadline")
