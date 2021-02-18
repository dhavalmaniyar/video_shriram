from django.contrib import admin
from django.db import models
from . models import Expire,Data_entry_format
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('code','date')
class BookData(admin.ModelAdmin):
    list_display=('data_receive','proposal_no','customer_name','DOB','phone_no','Mode_call','done_date','Status','remarks','recording','whatsapp_no','download_recording')
admin.site.register(Expire,BookAdmin)
admin.site.register(Data_entry_format,BookData)
