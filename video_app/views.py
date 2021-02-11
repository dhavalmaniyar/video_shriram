from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Expire

# Create your views here.
def index(request):
    data=Expire.objects.all()
    return render(request,'index.html',{'data':data})

def call(request):
    # return HttpResponseRedirect("https://www.facebook.com/")
    print(">>>>>>>>>>")
    return render(request,'call.html')

@csrf_exempt 
def expirelink(request):
    print("asdf >>>>>")
    link= request.POST['counter']
    data=Expire(code=link)
    data.save()
    return render(request,'index.html')


def check(request):
    chk=request.POST['in']
    chkdata=Expire.objects.filter(code=chk)
    print("JJJJJJJJJJJJ"+chk)
    if chkdata:

    # for c in chkdata:         
    #     print(c.code)
    #     print(chk)
        # print("sfdsdfasdf<<<<<<<<<<"+type(chk)+">>>>>>>>>>>>>"+type(c.code))
        # if chk == c.code:
        return HttpResponseRedirect("http://127.0.0.1:8000/call#"+chk)
    return render(request,'index.html',{'message':"Link is Expired"})
