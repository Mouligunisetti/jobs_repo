from django.shortcuts import render
from testapp.models import HydJobs, puneJobs, bangloreJobs
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/index.html')

def hyd_job_view(request):
    jobs_list=HydJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def pune_jobs_view(request):
    jobs_list=puneJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)

def banglore_jobs_view(request):
    jobs_list=bangloreJobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/banglorejobs.html',my_dict)
