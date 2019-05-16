from django import forms
from .models import Article


from .widgets import BootstrapDateTimePickerInput


class ArticleCreateForm(forms.ModelForm):
    publish_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=BootstrapDateTimePickerInput()
    )
    
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'author',
            'publish_date'
        ]