from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage
from django.utils import timezone


def home(request):
    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            submitted = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'portfolio/home.html', {
        'form': form,
        'submitted': submitted
    })
