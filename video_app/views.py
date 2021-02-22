from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Expire
from django.core.mail import send_mail
from . import forms
import datetime
# Create your views here.
def index(request):
    data=Expire.objects.all()
    return render(request,'index.html',{'data':data})

def call(request):
    return render(request,'call.html')

def feedback(request):
    # name=request.POST.get('name')
    # email=request.POST.get('email')
    # user_friendly=request.POST.get('user_friendly')
    # audio=request.POST.get('qty')
    # data=Feedback(name=name,email=email,is_the_app_is_user_friendly=user_friendly,What_was_the_quality_of_the_sound_during_the_video_conference_transmission=audio)
    # data.save()
    return render(request,'feedback.html')
@csrf_exempt 
def expirelink(request):
    link= request.POST['counter']
    time=datetime.datetime.now()
    data=Expire(date=time,code=link)
    print("asdf >>>>>",time)
    data.save()
    return render(request,'index.html')


def check(request):
    chk=request.POST['in']
    chkdata=Expire.objects.filter(code=chk)
    if chkdata:
      
    # for c in chkdata:         
    #     print(c.code)
    #     print(chk)
        # print("sfdsdfasdf<<<<<<<<<<"+type(chk)+">>>>>>>>>>>>>"+type(c.code))
        # if chk == c.code:
        return HttpResponseRedirect("http://127.0.0.1:8000/call#"+chk)
    return render(request,'index.html',{'message':"Link is Expired"})

@csrf_exempt
def subscribe(request):
    client= request.POST.get('mail')
    
    # sub = forms.Subscribe()
    codes=123
    
    # codesTwo=request.POST.data['code']
    
    link=request.POST.get('shurl')
    time=request.POST.get('shtime')
    dataschedule=Expire(date=time, code=codes)
    dataschedule.save()
    # print("CCCCCCCCCCCCCCC",codes)
    print("!!!!!!!backend",datetime.datetime.now())
    print("!!!!!!!!!!!!time",time)
    if client:
        # sub = forms.Subscribe(request.POST)
        subject = 'Shreeram Videocall Link'
        message = 'Meeting is scheduled on '+time+'\n link: '+link
        # recepient = str(sub['Email'].value())
        recepient=str(client)
        send_mail(subject, 
            message, "dhavalmaniyar100@gmail.com", [recepient], fail_silently = False)
        send_mail(subject,message,'dhavalmaniyar100@gmail.com',['dhavalmaniyar100@gmail.com'],fail_silently=False)
        return render(request,'index.html',{'message':"meeting is scheduled"})

