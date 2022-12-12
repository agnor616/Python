from django.shortcuts import render, redirect
from app.forms import carroForm, motoristaForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data ={}
    data['form'] = carroForm()
    return render(request, 'form.html', data)

def forme(request):
    data ={}
    data['form'] = motoristaForm()
    return render(request, 'forme.html', data)

def create(request):
    form = carroForm(request.POST or None)
    if form.is_valid():
        form.save
        return redirect('home')

def create(request):
    form = motoristaForm(request.POST or None)
    if form.is_valid():
        form.save
        return redirect('home')