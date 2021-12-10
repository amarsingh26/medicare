from django.shortcuts import render, HttpResponse
from home.models import Signup
# Create your views here.
def home(request):
    return render(request,'home.html')
    
def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')
        signup= Signup(firstname=firstname,lastname=lastname,username=username,email=email,password=password,confirmpass=confirmpass)
        signup.save()
    return render(request,'register.html')
    
def login(request):
    return render(request,'index.html')
