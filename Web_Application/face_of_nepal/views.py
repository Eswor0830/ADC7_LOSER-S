from django.shortcuts import render,redirect
#from django.http import HttpResponse
from .models import Freelancer
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse, Http404
import os

def freelancer_form(request):
    return render(request,'Freelancerform.html')



def freelancer_save(request):
    if request.method== 'POST': 
        get_Name =request.POST['Name']
        get_Address= request.POST['Address']
        get_Phone =request.POST['Phone']
        get_Description= request.POST['Description']
        Freelancer_obj = Freelancer(Name=get_Name,Address=get_Address,Phone=get_Phone,Description=get_Description)
        Freelancer_obj.save()
        return HttpResponse("Record saved")
    else:
        return HttpResponse("Error record saving")


def Freelancer_list(request):
    list_of_Freelancers= Freelancer.objects.all()
    context_variable = {
        'Freelancer':list_of_Freelancers
    }
    return render(request,'Freelancer.html',context_variable)

def freelancer_edit(request, ID):
    freelancer_obj = Freelancer.objects.get(id=ID)
    context_varible = {
        'Freelancer':freelancer_obj
    }
    return render(request,'Freelancerupdateform.html',context_varible)

def freelancer_update_save(request,ID):
    freelancer_obj = Freelancer.objects.get(id=ID)
    freelancer_form_data = request.POST
    print(freelancer_form_data) 
    freelancer_obj.Name = request.POST['Name']
    freelancer_obj.Address =request.POST['Address']
    freelancer_obj. phone = request.POST['Phone']
    freelancer_obj. Description = request.POST['Description']
    freelancer_obj.save()
    return HttpResponse("Record Updated!!!!")

def freelancer_delete(request,ID):
        freelancer_obj= Freelancer.objects.get(id=ID)
        freelancer_obj.delete()
        return HttpResponse("Record Delete!!")

def search(request):
        freelancer_id = request.GET['Address']
        print(freelancer_id)
        freelancer = freelancer_id.objects.filter(Address__contains=freelancer_id)
        return HttpResponse("Test")
        #return render(request, 'hostel.html', {'hostel': hostel, 'Location': hostel_id})

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        file_object = FileSystemStorage()
        file_object.save(uploaded_file.name, uploaded_file)
        return render(request, 'upload.html')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

