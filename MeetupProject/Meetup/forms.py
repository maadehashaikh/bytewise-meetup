from django import forms



class Registrations(forms.Form):
    email=forms.EmailField(label='Your email')