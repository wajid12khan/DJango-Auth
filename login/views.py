from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
   if request.method == 'POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(request,username=username,password=password)
      if user is not  None:
         auth_login(request,user)
         return redirect('home')
      else:
         return HttpResponse('Username and password are incorrect')

       # user(username=username,password=password)
      

   return render(request, 'login.html')
 
def registration(request):
   if request.method == 'POST':
       username=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       cpassword=request.POST.get('cpassword')
       user=User.objects.create_user(username,email,password)
       user.save()
       return redirect('login')
      #  user.save()/
      #  return redirect('login')
   return render(request, 'registration.html') 

def pagelogout(request):
   logout(request)
   return redirect('login')