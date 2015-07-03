# Create your views here.
from django.shortcuts import render
from .froms import SampleSearchForm

def index(request):
    form = SampleSearchForm(request.GET)
    results = form.search()
    return render(request,'index.html', {'samples':results})


