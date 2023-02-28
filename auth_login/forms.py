
from django import forms
class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
      'placeholder': 'Enter Your Email',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
    password=forms.ChoiceField(widget=forms.PasswordInput(attrs={
'placeholder': 'Enter Your Password',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242;border-radius: 10px; '
    }))


class patientForm(forms.Form):
      levels=(
        (1,'Male'),
        (2,'Female')
      )
      username=forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Enter Your Name',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 5px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: -7px;'
    }))
      Email=forms.EmailField(widget=forms.EmailInput(attrs={
      'placeholder': 'Enter Your Email',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 5px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      Password=forms.ChoiceField(widget=forms.PasswordInput(attrs={
'placeholder': 'Enter Your Password',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242;border-radius: 10px; '
    }))
      Confirm=forms.ChoiceField(widget=forms.PasswordInput(attrs={
'placeholder': 'Confirm Your Password',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242;border-radius: 10px; '
    }))
      phone=forms.IntegerField(widget=forms.NumberInput(attrs={
      'placeholder': 'Enter Your Phone',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))

      Brith=forms.DateField(widget=forms.DateInput(attrs={
      'placeholder': 'Enter Your Birthdate',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      # Gender=forms.ChoiceField(choices=levels, )
    
class doctorForm(forms.Form):
      levels=(
        (1,'Male'),
        (2,'Female')
      )
      username=forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Enter Your Name',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 5px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: -7px;'
    }))
      Email=forms.EmailField(widget=forms.EmailInput(attrs={
      'placeholder': 'Enter Your Email',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 5px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      Password=forms.ChoiceField(widget=forms.PasswordInput(attrs={
'placeholder': 'Enter Your Password',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242;border-radius: 10px; '
    }))
      Confirm=forms.ChoiceField(widget=forms.PasswordInput(attrs={
'placeholder': 'Confirm Your Password',
        'style': '  color: white; height: 25px; width: 68%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242;border-radius: 10px; '
    }))
      phone=forms.IntegerField(widget=forms.NumberInput(attrs={
      'placeholder': 'Enter Your Phone',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))

      Brith=forms.DateField(widget=forms.DateInput(attrs={
      'placeholder': 'Enter Your Birthdate',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      Brith=forms.DateField(widget=forms.DateInput(attrs={
      'placeholder': 'Enter Your Birthdate',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      Special=forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Enter Your Specialization',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      address=forms.CharField(widget=forms.TextInput(attrs={
      'placeholder': 'Enter Your clinic address',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
      appoint=forms.MultipleChoiceField(
        choices=levels,
        widget=forms.MultipleHiddenInput(attrs={
      'placeholder': 'Enter Your clinic address',
        'style': '  color: white; height: 25px; width: 69%; border: 2px solid grey; padding: 7px; margin-top: 10px; margin-bottom: 10px; font-size: 20px; background-color: #424242; border-radius: 10px;margin-left: 15px;'
    }))
    




