from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    a = Info.objects.all()
    
    #a=Info.objects.order_by('-first_name')
    #print Info.objects.values_list('first_name',flat=True)
    #p=Info.objects.extra(where=["salary>6000"])
    #print p.values_list('id','salary')
    return render(request,'home.html',{'record':a,})


    
def contact(request):
    
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            
            #print form.cleaned_data['first_name']
            
            form.save()
            #con_obj.save()
            
            return HttpResponseRedirect('/')
            
    else:
        form=contactform()
    return render(request,'contact.html',{'form':form})

def success(request):
    return render(request,'success.html')

def detail(request,d):
    n=Info.objects.get(id=d)
    return render(request,'detail.html',{'t':n})


def del_record(request,d):
    n=Info.objects.get(id=d)
    n.delete()
    #return HttpResponse('deleted')
    return HttpResponseRedirect('/')


def search(request):
    if request.method =='POST':

        squery = request.POST['search_box1']
        if squery:
            s = Info.objects.filter(first_name__icontains=squery)
            if s:
                return render(request,'search.html',{'q':s})
            else:
                return render(request,'notfound.html')
            
        else:    

            return HttpResponseRedirect('/')


        
def edit_record(request,d):
    n=Info.objects.get(id=d)
    
    if request.method == "POST":
        form = contactform(request.POST,instance=n)
        if form.is_valid():
            

            form.save()
            
            return HttpResponseRedirect('/')
            
    else:
        form=contactform(instance=n)
    return render(request,'edit_form.html',{'form':form})
