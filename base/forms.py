from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('subject', 'name', 'description')

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter Subject'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Name'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter Description'
