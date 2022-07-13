from django import forms
from django.forms import ModelForm
from django.db.models import Q
from .models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class QueryForm(forms.Form):
    query = forms.CharField(label='Student Name or Id', max_length="150")

    def search(self):
        q = self.cleaned_data['query']
        # To account for Elon Musk's son's name which has a digit in the name
        condition = Q(first_name__contains=q) | Q(last_name__contains=q)
        if q.isdigit():
            condition = condition | Q(id=q)
        return Student.objects.filter(condition)
