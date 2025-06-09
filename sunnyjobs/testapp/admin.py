from django.contrib import admin
from testapp.models import HydJobs,puneJobs,bangloreJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class puneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(puneJobs,puneJobsAdmin)

class bangloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(bangloreJobs,bangloreJobsAdmin)
