from django.shortcuts import render
from django.contrib.auth.models import  auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm
# Create your views here.



def home(request):

    
    return render(request, 'home.html')

def about_us(request):

    
    return render(request, 'about-us.html')

def contact_us(request):

    
    return render(request, 'contact-us.html')



def signin(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username = username, password= password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Enter a valid User ID')
                return redirect('signin')
        return render(request, 'login.html')

def register(request):
    form = UserForm()
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully")
            return redirect('signin')
        else:
            messages.error(request, 'Password not secure') 
            return redirect('register')
    else:
        context = {'form':form}
        
    return render(request, 'register.html', context )

@login_required(login_url='signin')
def dashboard(request):

    
    return render(request, 'dashboard.html')
        

def logout(request):
    auth.logout(request)
    return redirect('signin')