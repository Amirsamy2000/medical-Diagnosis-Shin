from django import forms

class profileForm(forms.Form):
    photo=forms.ImageField(label='Upload your Photo')

