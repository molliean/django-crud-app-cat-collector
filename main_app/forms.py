from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
    # this is like configuration options for the class
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
        # widgets property allows you to customize the inputs
        # add new attributes, etc.
        #customize the 'date' input
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
