from django import forms
from .models import Module, ModuleRegistration


# class ModuleRegForm(forms.ModelForm):
#     class Meta:
#         model = ModuleRegistration
#         fields = ['student', 'module']

class ModuleRegForm(forms.Form):
    modules = forms.ModelMultipleChoiceField(
        queryset= Module.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )