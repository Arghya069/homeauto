from django.http import JsonResponse
from django.shortcuts import render,redirect,HttpResponse
from .models import GetLED
# Create your views here.
def home(request):
    return HttpResponse('Welcome')

def getLight1(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_1==0:
        return HttpResponse("Light is off")
    else:
        return HttpResponse("Light is on")
    
def getLight2(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_2==0:
        return HttpResponse("Light is off")
    else:
        return HttpResponse("Light is on")
    
def getLight3(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_3==0:
        return HttpResponse("Light is off")
    else:
        return HttpResponse("Light is on")
    
def getLight4(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_4==0:
        return HttpResponse("Light is off")
    else:
        return HttpResponse("Light is on")
    
def ToggleLight1(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_1==0:
        gled.light_1=1
        gled.save()
        return redirect('getstat1',pk)
    else:
        gled.light_1=0
        gled.save()
        return redirect('getstat1',pk)
    
def ToggleLight2(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_2==0:
        gled.light_2=1
        gled.save()
        return redirect('getstat2',pk)
    else:
        gled.light_2=0
        gled.save()
        return redirect('getstat2',pk)
    
def ToggleLight3(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_3==0:
        gled.light_3=1
        gled.save()
        return redirect('getstat3',pk)
    else:
        gled.light_3=0
        gled.save()
        return redirect('getstat3',pk)
    
def ToggleLight4(request,pk):
    gled = GetLED.objects.get(device_id=pk)
    if gled.light_4==0:
        gled.light_4=1
        gled.save()
        return redirect('getstat4',pk)
    else:
        gled.light_4=0
        gled.save()
        return redirect('getstat4',pk)
    
def sendControl(request,pk):
    gled=GetLED.objects.get(device_id=pk)
    return JsonResponse({'Light1':str(gled.light_1),'Light2':str(gled.light_2),'Light3':str(gled.light_3),'Light4':str(gled.light_4)})



def profile(request):
    return HttpResponse('Behold_my_greatness')