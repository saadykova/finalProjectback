from django import forms
from .models import Employee


class PostForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


