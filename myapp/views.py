from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import Person
from myapp.forms import NameForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is the myapp page</h1>")
def formsubmission(request):
    NUM=Person.objects.filter(cpi=7)

    dic={"user":"this is dynamic data 67","cpi9":NUM}
    return render(request,'formsubmission.html',context=dic)
def studlogin(request):
    return render(request,'login.html',{})
def details(request,pk):
    p=Person.objects.get(pk=pk)
    return HttpResponse(p)
    #return render(request,'dummy.html',context=dic)
def dummy(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect('../dummy/')
    else:
        form=NameForm()
    return render(request,'formsubmission.html',{'form':form})
