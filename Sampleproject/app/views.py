from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse("Welcome")

def fun2(request):
    return HttpResponse("Ok Bye")

l=[]
def fun3(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun3)
    else:
        return render(request,'demo.html')

def fun4(request):
    return render(request,'home.html')

def fun5(request):
    return render(request,'about.html')

def fun6(request):
    return render(request,'contact.html')



l=[{'name': 'aa', 'age':'22'},{'name': 'bb', 'age':'21'}]

def display(req):
    a="Not Welcome"
    return render(req,'display.html',{'data':l,'data1':a})

def add_dtls(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(display)
    else:
        return render(request,'add_dtls.html')