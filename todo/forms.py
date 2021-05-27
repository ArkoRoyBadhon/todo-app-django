from django.forms import ModelForm
from todo.models import TODO
from django import forms

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','about','course','start_date','start_time','end_date','end_time','url1','url2','w1','w2']
        

