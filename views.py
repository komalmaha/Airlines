from django.http import HttpResponseRedirect
from django.shortcuts import render
from service.models import Signup,Flight

def MyHome(request):
    return render(request,'index.html')

def MyLogin(request):
    if(request.method=='POST'):
        em=request.POST['em']
        ps=request.POST['ps']

        if(em=='admin@gmail.com' and ps=='admin'):
            return HttpResponseRedirect('/adash')
        else:
            return HttpResponseRedirect('/udash')
    return render(request,'login.html')

def MySignup(request):
    if(request.method=='POST'):
        fn=request.POST['fname']
        add=request.POST['add']
        em=request.POST['em']
        mob=request.POST['mob']
        pass1=request.POST['pass']
        cpass1=request.POST['cpass']
        gen=request.POST['gender']
        s1=Signup(fname=fn,address=add,email=em,mobile=mob,pass1=pass1,repass=cpass1,gen=gen)
        s1.save()
        return HttpResponseRedirect('/login')
    return render(request,'signup.html')

def UserDash(request):
    return render(request,'userdash.html')

def AdminDash(request):
    return render(request,'admindash.html')

def FlightAdd(request):
    if(request.method=='POST'):
        fid=request.POST['fid']
        dt1=request.POST['dt1']
        fname=request.POST['fname']
        seats=request.POST['seats']
        source=request.POST['source']
        dest=request.POST['det']
        prize=request.POST['prize']
        dt2=request.POST['dt2']
        f1=Flight(fid=fid,dt1=dt1,fname=fname,seats=seats,source=source,dest=dest,prize=prize,dt2=dt2)
        f1.save()
        return HttpResponseRedirect('/adash')
    return render(request,'flightadd.html')

def FlightPage(request):
    f1=Flight.objects.all()
    dict1={
        'data':f1
    }
    return render(request,'flight.html',dict1)

def CustView(request):
    s1=Signup.objects.all()
    dict1={
        's1':s1
    }
    return render(request,'custviews.html',dict1)
def Reservation(request):
    if(request.method=='GET'):
        em=request.session['em']
        s1=Signup.objects.get(email=em)
        print(s1)
        dict1={
            's1':s1
        }
        return render(request,'reservation.html',dict1)
    if(request.method=='POST'):
        bid=request.POST['bid']
        dt=request.POST['dt']
        name=request.POST['name']
        em=request.POST['email']
        mob=request.POST['mob']
        fname=request.POST['fname']
        bdt=request.POST['bdt']
        source=request.POST['source']
        dest=request.POST['dest']
        seat=request.POST['seat']
        f1=Flight.objects.get(fname=fname,source=source,dest=dest)
        p=f1.prize
        tot=int(p)*int(seat)
        s1=Reservation(bid=bid,dt=dt,name=name,email=em,
                       mobile=mob,fname=fname,bookdt=bdt,source=source,
                       dest=dest,seat=seat,prize=tot)
        s1.save()
        return HttpResponseRedirect('/udash')     

def RevView(request):
    em=request.session['em']
    print(em)
    f1=Reservation.objects.get(email='komalmahajan292@gmail.com')
    dict1={
        'data':f1
    }
    return render(request,'resview.html',dict1)

def RevCancel(request):
    bid=request.GET['bid']
    r1=Reservation.objects.get(bid=bid)
    r1.status='cancel'
    r1.save()
    return HttpResponseRedirect('/resview')

def AdminRevView(request):
    try:
        f1=Reservation.objects.get(status='reserve')
        dict1={
            'data':f1
        }
    except:
        dict1={
            'data':'-'
        }
    return render(request,'adminrevview.html',dict1)

def AdminRevcancel(request):
    try:
        f1=Reservation.objects.get(status='cancel')
        dict1={
            'data':f1
        }
    except:
        dict1={
            'data':'-'
        }
    return render(request,'adminrevcancel.html',dict1)

def AdminRevDel(request):
    id=request.GET['bid']
    r1=Reservation.objects.get(bid=id)
    r1.delete()
    return HttpResponseRedirect('/adminresview')