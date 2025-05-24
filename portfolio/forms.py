from django import forms
import re

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Full Name",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your full name',
            'required': 'required'
        })
    )

    email = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'e.g. example@gmail.com',
            'pattern': r"[^@ \t\r\n]+@[^@ \t\r\n]+\.(com|co\.tz|org|net)",
            'title': 'Please enter a valid email (e.g. example@gmail.com, .co.tz, .org)',
            'required': 'required'
        })
    )

    subject = forms.CharField(
        label="Subject",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'required': 'required'
        })
    )

    message = forms.CharField(
        label="Message",
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Your message here...',
            'rows': 5,
            'required': 'required'
        })
    )
