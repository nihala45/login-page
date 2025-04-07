from django.shortcuts import render,redirect,HttpResponse
from .models import CustomUser
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth import logout as auth_logout


def login_page(request):
    return render(request, 'Login.html')

def register_page(request):
    return render(request, 'Register.html')

def home(request):
    return render(request, 'home.html')


def Signup(request):
    if request.method == 'POST':
        username = request.POST['user_username']
        email = request.POST['user_email']
        phone = request.POST['user_phone']
        password = request.POST['user_password']
        confirm_password = request.POST['user_confirm']
        
        already = CustomUser.objects.filter(email = email)
        if already:
            return JsonResponse({'status':'already','message':'There is already a Account with this Email'}) 
        else:
            user2 = CustomUser(
                username=username,
                email=email,
                password=password,
                phone=phone,
            )
            user2.save()
            
        redirect_url = reverse('home')
        return JsonResponse({'status':'success','redirect_url': redirect_url})   
    
    
def login(request):
    print("reached")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(email=email, password=password)
            if user and not user.is_blocked:
                
                request.session['email']=email
                request.session['phone'] = user.phone 
                request.session['username'] = user.username
                return JsonResponse({'status':'success'})
                
               

                
            else:
                return JsonResponse({'status':'block','message':'Your account is blocked. Please contact support.'})
                
                
        except CustomUser.DoesNotExist:
            return JsonResponse({'status':'wrong','message':'Incorrect email address or password. Please try again.'})


    return redirect('home')


def logout(request):
    auth_logout(request)            
    request.session.flush()         
    return redirect('login_page') 