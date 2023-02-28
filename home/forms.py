from django import forms

class mainForm(forms.Form):
    description=forms.CharField(widget=forms.Textarea(
        { 'style': '   width: 80%;height: 200px;  border: 2px solid grey; font-size: 20px;border-radius: 10px; '}
    ),)
    link=forms.CharField(widget=forms.TextInput(
        {
            'style': '   width: 90%;height: 30px;  border: 2px solid grey; font-size: 20px;border-radius: 10px; '
        }
    ))