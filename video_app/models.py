from django.db import models
from django.db.models.deletion import SET_DEFAULT
from django.utils import timezone
import datetime
# Create your models here.
class EventManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            date__gte=timezone.now()-timezone.timedelta(minutes=5)
        )

class Expire(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    code=models.CharField(max_length=50)
    schedule=models.BooleanField(default=False)
    objects = EventManager()
    # def delete_after_five_minutes(self):
    #     time = self.date + datetime.timedelta(minutes=5)
    #     print('>>>>>>>time>',time)
    #     if time < datetime.datetime.now():
    #         e = Expire.objects.get(pk=self.pk)
    #         e.delete()
    #         return True
    #     else:
    #         return False
    def __str__(self) :
        return self.code


class  Data_entry_format(models.Model):
    data_receive= models.DateField()
    proposal_no=models.IntegerField()
    customer_name=models.CharField(max_length=50)
    DOB=models.DateField()
    phone_no=models.IntegerField()
    Mode_call=models.CharField(max_length=30)
    done_date=models.DateField()
    Status=models.CharField(max_length=30)
    remarks=models.CharField(max_length=100)
    recording=models.BooleanField(default=False)
    whatsapp_no=models.IntegerField()
    download_recording=models.CharField(default="Download", max_length=40)

    # class Feedback(models.Model):
    #     name=models.CharField(max_length=30)
    #     email=models.EmailField(max_length=256)
    #     is_the_app_is_user_friendly=models.CharField(max_length=20)
    #     What_was_the_quality_of_the_sound_during_the_video_conference_transmission=models.CharField(max_length=30)
