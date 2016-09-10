from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person
# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the myapp page</h1>")
def formsubmission(request):
    NUM=Person.objects.filter(cpi=7).values('first_name')

    dic={"user":"this is dynamic data 67","cpi9":NUM}
    return render(request,'formsubmission.html',context=dic)
