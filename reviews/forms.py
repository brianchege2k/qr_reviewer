from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=10)
    class Meta:
        model = Review
        fields = ('name', 'email','review_text','rating')
