from django.shortcuts import render, redirect
from .models import Record
from .forms import RecordForm


def index(request):
    records = Record.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'records': records})


def create_record(request):
    error = ''
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = RecordForm()
    context = {
        'form': form,
        'error': error
        }
    return render(request, 'main/create_record.html', context)


def about(request):
    return render(request, 'main/about.html')
