from django import forms
from .models import Article




class ArticleCreateForm(forms.ModelForm):
    publish_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'author',
            'publish_date'
        ]