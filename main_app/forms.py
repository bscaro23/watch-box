# forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'style': 'width: 300px; max-width: 100%;',
            }),
        }
