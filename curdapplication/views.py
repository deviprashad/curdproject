from django.shortcuts import render
from .forms import ProductInsertForm,ProductDeleteForm,ProductUpdateForm
from .models import ProductData
from django.http import HttpResponse
def insert(request):
    if request.method=="POST":
        iform=ProductInsertForm(request.POST)
        if iform.is_valid():
            pid1=request.POST.get('pid','')
            pname1=request.POST.get('pname','')
            pcost1=request.POST.get('pcost','')
            pcolor1=request.POST.get('pcolor','')
            pclass1=request.POST.get('pclass','')
            cname1=request.POST.get('canme','')
            cmobile1=request.POST.get('cmobile','')
            cemail1=request.POST.get('email','')
            data=ProductData(
                pid=pid1,
                pname=pname1,
                pcost=pcost1,
                pcolor=pcolor1,
                pclass=pclass1,
                cname=cname1,
                cmobile=cmobile1,
                cemail=cemail1
            )
            data.save()
            iform=ProductInsertForm()
            return render(request,'insert.html',{'insert':iform})
        else:
            return HttpResponse('Plz fill all the fields before submitting')
    else:
        iform = ProductInsertForm()
        return render(request, 'insert.html', {'insert': iform})
def retrive(request):
    data=ProductData.objects.all()
    return render(request,'retrive.html',{'retrive':data})
def update(request):
    if request.method=="POST":
        uform=ProductUpdateForm(request.POST)
        if uform.is_valid():
            pid1=request.POST.get('pid','')
            pcost1=request.POST.get('pcost','')
            data=ProductData.objects.filter(pid=pid1)
            if not data:
                return HttpResponse("Id not found")
            else:
                data.update(pcost=pcost1)
                uform=ProductUpdateForm()
                return render(request,'uform.html',{'update':uform})
        else:
            return HttpResponse('Invalid Form Details')
    else:
        uform = ProductUpdateForm()
        return render(request, 'uform.html', {'update': uform})
def delete(request):
    if request.method=="POST":
        dform=ProductDeleteForm(request.POST)
        if dform.is_valid():
            pid1=request.POST.get('pid','')
            data=ProductData.objects.filter(pid=pid1)
            if not data:
                return HttpResponse("id not found")
            else:
                data.delete()
                dform=ProductDeleteForm()
                return render(request,'delete.html',{'delete':dform})
        else:
            return HttpResponse('Plz fill before submit')
    else:
        dform = ProductDeleteForm()
        return render(request, 'delete.html', {'delete': dform})





# Create your views here.
