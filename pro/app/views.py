from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# This function is for Add  &  Create your views here.
def add(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
         nm = fm.cleaned_data['name']
         em = fm.cleaned_data['email']
         pw = fm.cleaned_data['password']
         reg = User(name=nm, email=em, password=pw,)
         reg.save()
    else:
        fm =StudentRegistration()
    stud = User.objects.all()
    return render (request, 'add.html', {'form': fm, 'stu':stud})

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'update.html', {'form':fm})


# This function for delete

def delete_obj(request, id):
    pi =User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')