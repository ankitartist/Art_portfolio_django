from django.shortcuts import render
from . import forms
from . import models
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from artapp.models import artwork1,more,more2,details
from artapp.forms import UserForm,artworkform1,moreform,moreform2,detailsform,useredit
from django.contrib.auth.models import User
from django.views.generic import UpdateView



def index(request):
    return render(request,'artapp/index.html')
    
     
def home1(request):
    return render(request,'artapp/home1.html')
    
    
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            
            registered=True
            return HttpResponse("<h1>you have been successfully registered</h1>")
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request,'artapp/registration.html',{'user_form':user_form, 'register':register})
    
    
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                
                return HttpResponseRedirect(reverse('home1'))
            else:
                return HttpResponse("Sorry! Account is not active")
        else:
            return HttpResponse("someone tried to login and failed!")
            
    else:
        return render(request,'artapp/login.html',{})
        
        
def profile(request):
    temp=details.objects.filter(user1=request.user)
    pic2=more2.objects.filter(user1=request.user)
    pic=more.objects.filter(user1=request.user)
    context={'user':request.user,'pic':pic,'pic2':pic2,'temp':temp}
    return render(request,'artapp/profile.html',context)
    
    
@login_required    
def portfolio(request):
    temp=details.objects.filter(user1=request.user)
    pic2=more2.objects.filter(user1=request.user)
    pic=more.objects.filter(user1=request.user)
    artwork=artwork1.objects.filter(user1=request.user)[:5]
    context={'user':request.user,'pic':pic,'pic2':pic2,'temp':temp,'artwork':artwork}
    
    return render(request,'artapp/portfolio.html',context)
    
    
@login_required   
def viewart(request):
    artwork=artwork1.objects.filter(user1=request.user)
    return render(request,'artapp/viewart.html',{'artwork':artwork})  
       

# Create your views here.
      
def artworks1(request,pk):
    if request.method=='POST':
        form=artworkform1(request.POST)
        if form.is_valid():
            us=User.objects.filter(is_superuser=False)
            form.instance.user1 = us.get(pk=pk)     
            artwork=form.save(commit=False)
                    
            if 'art' in request.FILES:
                artwork.art=request.FILES['art']
                artwork.save()
                return HttpResponseRedirect(reverse("home1"))
        else:
            return HttpResponse("<h2>Shit</h2>")
                
    else:
        form = artworkform1(pk)
                
    return render(request,'artapp/artworks1.html',{'user':request.user,'artwork_form':form})
    
    
    
    
@login_required 
def more1(request,pk):
        pic=more.objects.filter(user1=request.user)
        if request.user.id == int(pk):
        
            if request.method=='POST':
                
                form=moreform(request.POST)
                if form.is_valid():
                    
                    us=User.objects.filter(is_superuser=False)
                    form.instance.user1=us.get(pk=pk)
                    
                    profile=form.save(commit=False)
                    if 'ppic' in request.FILES:
                        more.objects.filter(user1=request.user).delete()
                        profile.ppic=request.FILES['ppic']
                        profile.save()
                        return HttpResponseRedirect(reverse('home1'))
                        
                else:
                    return HttpResponse("<h1>Shit</h1>")
            else:
                form=moreform(pk)
            return render(request,'artapp/more.html',{'user':request.user,'profile_form':form,'pic':pic})
            
           
@login_required 
def details1(request,pk):
    if request.user.id == int(pk):
        wf=forms.detailsform()
    
        if request.method=='POST':
            wf=detailsform(request.POST)
            if wf.is_valid():
                us=User.objects.filter(is_superuser=False)
                wf.instance.user1=us.get(pk=pk)
                details.objects.filter(user1=request.user).delete()
                wf.save()
            else:
                print("invalid data entered")
        else:
            wf=detailsform()
        return render(request,'artapp/details.html',{'wf':wf})
        
            
            
            
@login_required 
def more22(request,pk):
        pic2=more2.objects.filter(user1=request.user)
        if request.user.id == int(pk):
        
            if request.method=='POST':
                
                form2=moreform2(request.POST)
                if form2.is_valid():
                    
                    us=User.objects.filter(is_superuser=False)
                    form2.instance.user1=us.get(pk=pk)
                    
                    profile2=form2.save(commit=False)
                    if 'coverphoto' in request.FILES:
                        more2.objects.filter(user1=request.user).delete()
                        profile2.coverphoto=request.FILES['coverphoto']
                        profile2.save()
                        return HttpResponseRedirect(reverse('home1'))
                        
                else:
                    return HttpResponse("<h1>Shit</h1>")
            else:
                form2=moreform2(pk)
            return render(request,'artapp/more11.html',{'user':request.user,'cover_form':form2,'pic2':pic2})
 
def navbar(request,pk):
    pic=more.objects.filter(user1=request.user)
    return render(request,'artapp/base.html',{'pic':pic})
    

def viewall(request):
    artwork=artwork1.objects.all()
    return render(request,'artapp/viewall.html',{'artwork':artwork})
    
    
   