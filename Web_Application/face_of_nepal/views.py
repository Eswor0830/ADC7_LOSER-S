from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FreelancerForm
from .models import Freelancer

# Create your views here.
def view_hello_world(request):
    return render(request,"index.html")



def freelancer_list(request):
    context = {'freelancer_list': Freelancer.objects.all()}
    return render(request, "freelancer_register/freelancer_list.html", context)


def freelancer_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FreelancerForm()
        else:
            freelancer = Freelancer.objects.get(pk=id)
            form = FreelancerForm(instance=freelancer)
        return render(request, "./freelancer_form.html", {'form': form})
    else:
        if id == 0:
            form = FreelancerForm(request.POST)
        else:
            freelancer = Freelancer.objects.get(pk=id)
            form = FreelancerForm(request.POST,instance= freelancer)
        if form.is_valid():
            form.save()
        return redirect('/freelancer/list')


def freelancer_delete(request,id):
    freelancer = Freelancer.objects.get(pk=id)
    freelancer.delete()
    return redirect('/freelancer/list')



