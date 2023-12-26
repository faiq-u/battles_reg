from django.shortcuts import render, redirect
from .forms import AppplicantForm, accrej
from django.http import HttpResponse
from .models import applicant
# Create your views here.

applicants1 = applicant.objects.filter(accepted=False)
applicants2 = applicant.objects.filter(accepted=True)

def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method == 'POST':
        form = AppplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AppplicantForm()

    return render(request, 'reg.html', {'form': form})

def view(request):
    if request.method == 'POST':
        spec = applicant.objects.get(id=request.POST['id'])
        form1 = accrej(request.POST,instance=spec)
        form1.save()
        applicants1 = applicant.objects.filter(accepted=False)
        applicants2 = applicant.objects.filter(accepted=True)
        return render(request,'view.html',{'applicants':applicants1,'accrej':accrej()})
    y = accrej()
    applicants1 = applicant.objects.filter(accepted=False)
    applicants2 = applicant.objects.filter(accepted=True)
    return render(request,'view.html',{'applicants':applicants1,'accrej':y})

def own(request):
    if request.method == 'POST':
        applicants2 = applicant.objects.filter(accepted=True,name=request.POST['search'])
        return render(request,'own.html',{'applicants':applicants2})
    applicants1 = applicant.objects.filter(accepted=False)
    applicants2 = applicant.objects.filter(accepted=True)
    print(applicants2[0].photo.url)
    return render(request,'own.html',{'applicants':applicants2})