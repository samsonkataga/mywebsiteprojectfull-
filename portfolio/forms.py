from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name", widget=forms.TextInput(attrs={
        'placeholder': 'Your full name'
    }))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address'
    }))
    subject = forms.CharField(max_length=150, label="Subject", widget=forms.TextInput(attrs={
        'placeholder': 'Subject of your message'
    }))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={
        'placeholder': 'Type your message here...',
        'rows': 5
    }))
