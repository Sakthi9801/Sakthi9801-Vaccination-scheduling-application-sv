from django.shortcuts import render
from center.models import Center
from center.forms import CenterForm
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

def center_list(request):
    objects=Center.objects.all()
    context={"center":objects,}
    return render(request,"center/center-list.html",context)

def center_detail(request,id):
    object=Center.objects.get(id=id)
    context={"center":object,}
    return render(request,"center/center-detail.html",context) 

def create_center(request):
    if request.method == "POST":
        form=CenterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("center:list"))
        else:
            return render(request,"center/create-center.html",{"form":form})

    #get
    context={"form" : CenterForm() }
    return render(request,"center/create-center.html",context)

def update_center(request,id):
    try:
        center =Center.objects.get(id=id)
    except Center.DoesNotExist:
        raise Http404("center instance is not found")

    if request.method=="POST":
        context={
            "form":CenterForm(instance=center)
        }
        return render(request,"update-center.html",context)
