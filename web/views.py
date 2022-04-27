from django.shortcuts import render
from .models import Flan, ContactForm, Local
from .forms import ContactFormModelForm, ContactFormForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def indice (request):
    public_flans = Flan.objects.filter(is_private = False)

    return render (request, 'index.html', {
        'public_flans': public_flans
    })

def acerca (request):
    return render (request, 'about.html', {})

@login_required
def bienvenido (request):
    private_flans = Flan.objects.filter(is_private = True)
    return render (request, 'welcome.html', {
        'private_flans': private_flans
    })

def contacto (request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormModelForm()
    return render (request, 'contactus.html', {'form': form,})


def local(request):
    locales = Local.objects.all()
    return render(request, 'local.html', {
        'locales': locales,
    })

def exito (request):
    return render (request, 'success.html', {})