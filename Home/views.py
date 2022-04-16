from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from Home.models import cruddata

# Create your views here.
def home(request):
    return render(request, "home.html")

def show(request):
    data = cruddata.objects.all()
    return render(request, "show.html", {'data': data})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        cruddata(ID = ID, name = name, address = address, phone = phone).save()
        msg = "Data Stored Successfully"
        return render(request, "home.html", {'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not found</h1>")

def delete(request):
    ID = request.GET['id']
    cruddata.objects.filter(ID = ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']
    name = address = phone = "Not_Available"
    for data in cruddata.objects.filter(ID = ID):
        name = data.name
        address = data.address
        phone = data.phone

    return render(request, "edit.html", {'ID':ID, 'name':name, 'address':address, 'phone':phone})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        cruddata.objects.filter(ID = ID).update(name= name, address=address, phone=phone)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

