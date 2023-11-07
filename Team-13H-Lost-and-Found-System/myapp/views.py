from django.shortcuts import render
from myapp.models import users
from django.contrib.auth import authenticate, login
from django.shortcuts import render,HttpResponse,redirect
from accounts.forms import SignUpForm

    
# Create your views here.

em=""
pwd=""


def login_page(request):
    global em,pwd
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value

        if(request.POST("email") and request.POST("password")):
            cred = users()
            cred.email = request.POST['email']
            cred.password = request.POST['password']
            return render(request,"home.html")
        else:
            return render(request,"error.html")
            
    return render(request,"login_page.html")


def signup_page(request):
    print('Hello')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print('Hello')

        if form.is_valid():
            objuser = form.save()

            print(objuser.id)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            print(request.user.id)

            objt = users(user=objuser,
                        first_name=request.POST.get('first_name'), 
                        last_name=request.POST.get('last_name'),
                        sex=request.POST.get('sex'),
                        email=request.POST.get('email'),
                        password=request.POST.get('password'),)

            print(objt)

            objt.save()

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/accounts')

    else:
        form = SignUpForm()

    print('Hello')
    return render(request, 'templates/signup_page.html', {'form': form})














