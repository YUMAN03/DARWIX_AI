from django import forms
from .models import TitleRequest

class ContentForm(forms.ModelForm):
    class Meta:
        model = TitleRequest
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your blog post content here...',
                'rows': 10,
            }),
        }