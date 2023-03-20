from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import mysql.connector

# Create your views here.

document_no = 210045678

def home(request):
    try:
        loggedin = request.session['loggedin_admin']
    except:
        loggedin = False
    if loggedin:
        return render(request, 'admin_home.html')
    return redirect('a_login')

def login(request):
    try:
        loggedin = request.session['loggedin_admin']
    except:
        loggedin = False
    if loggedin:
        return redirect('a_home')
    else:
        msg=''
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        if(id != '' and password != ''):
            if(id == "admin" and password == "admin@123"):
                request.session['loggedin_admin'] = True
                return redirect('a_home')
            else:
                msg = "Invalid User ID or Password"
        param = {'msg':msg}
        return render(request, 'admin_login.html', param)

def logout(request):
    print("jerry")
    try:
        loggedin = request.session['loggedin_admin']
    except:
        loggedin = False
    if loggedin:
        request.session['loggedin_admin'] = False
    return redirect('home')



    
