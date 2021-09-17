from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmployerForm
from .models import Employer

# Create your views here.
def add(request):
    form = EmployerForm(request.POST or None)
    #employer = Employer.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def details(request):
    employer = Employer.objects.all()
    return render(request, 'details.html', {'employer': employer})

def update(request, id):
    employer = Employer.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employer)
    if form.is_valid():
       form.save()
       return HttpResponseRedirect('/details')
    return render(request, 'update.html', {'employer': employer})

def delete(request, id):
    form = Employer.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')
