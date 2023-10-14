from django.shortcuts import render
from datetime import date

def hello(request):
    return render(request, 'index.html', {
        'current_date': date.today()
    })



# Create your views here.
