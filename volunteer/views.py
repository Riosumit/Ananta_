from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import re
import mysql.connector

# Create your views here.

def personal(request):
    try:
        personal=request.session["personal"]
    except:
        personal=False
    if personal:
        return redirect('medical')
    msg=''
    aadhar=request.POST.get('aadhar','')
    name=request.POST.get('name','')
    dob=request.POST.get('dob','')
    gender=request.POST.get('gender','')
    email=request.POST.get('email','')
    phone_no=request.POST.get('phone_no','')
    address=request.POST.get('address','')
    password=request.POST.get('password','')
    c_password=request.POST.get('c_password','')
    if name != '' and dob != '' and gender != '' and email != '' and phone_no != '':
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif len(aadhar)!=12:
            msg = 'Aadhar Number must contain only 12 digits!'
        elif re.match(r'[0-9]+', name):
            msg = 'Name must contain only characters'
        elif re.match(r'[0-9]+', gender):
            msg = 'Gender must contain only characters'
        elif len(phone_no)!=10:
            msg = 'Phone Number must contain only 10 digits!'
        elif password != c_password:
            msg = 'Confirm password does not match'
        else:
            request.session["aadhar"]=aadhar
            request.session["user_name"]=name
            request.session["dob"]=dob
            request.session["gender"]=gender
            request.session["email"]=email
            request.session["phone_no"]=phone_no
            request.session["address"]=address
            request.session["password"]=password
            request.session["personal"]=True
            return redirect('medical')
    param={'msg':msg, 'name':name, 'dob':dob, 'gender':gender, 'email':email, 'phone_no':phone_no, 'address':address}
    return render(request, 'personal_details.html', param)

def medical(request):
    try:
        personal=request.session["personal"]
        try:
            medical=request.session["medical"]
        except:
            medical=False
    except:
        personal=False
    print(medical)
    if not personal:
        return redirect('personal')
    elif medical:
        return redirect('document')
    msg=''
    blood=request.POST.get('blood','')
    allergies=request.POST.get('allergies','')
    height=request.POST.get('height','')
    weight=request.POST.get('weight','')
    history=request.POST.get('history','')
    kin_name=request.POST.get('kin_name','')
    kin_contact=request.POST.get('kin_contact','')
    arr = ['heart','lungs','liver','kidneys','pancreas','intestines','corneas','skin','bone','valves','tissue']
    donation=''
    for i in arr:
        if request.POST.get(i,''):
            donation=donation+i.title()+', '
    if blood != '' and allergies != '' and height != '' and weight != '' and history != '' and kin_name != '' and kin_contact != '':
        if re.match(r'[0-9]+', kin_name):
            msg = 'Name must contain only characters'
        elif donation == '':
            msg = 'Must select any organ to donate'
        else:
            request.session["blood"]=blood
            request.session["allergies"]=allergies
            request.session["height"]=height
            request.session["weight"]=weight
            request.session["history"]=history
            request.session["kin_name"]=kin_name
            request.session["kin_contact"]=kin_contact
            request.session["donation"]=donation
            request.session["medical"]=True
            return redirect('document')
    param = {'blood':blood, 'allergies':allergies, 'height':height, 'weight':weight, 'history':history, 'kin_name':kin_name, 'kin_contact':kin_contact, 'msg':msg}
    return render(request, 'medical_details.html', param)

def document(request):
    try:
        personal=request.session["personal"]
        try:
            medical=request.session["medical"]
        except:
            medical=False
    except:
        personal=False
    if not personal:
        return redirect('personal')
    elif not medical:
        return redirect('medical')
    if request.method == "POST":
        regi_no=request.session["aadhar"]
        photo=request.FILES['photo']
        photo_name=str(regi_no)+"_photo."+(photo.name).split('.')[-1]
        aadhar_card=request.FILES['aadhar_card']
        aadhar_name=str(regi_no)+"_aadhar."+(aadhar_card.name).split('.')[-1]
        addressf=request.FILES['address']
        address_name=str(regi_no)+"_address."+(addressf.name).split('.')[-1]
        report=request.FILES['report']
        report_name=str(regi_no)+"_report."+(report.name).split('.')[-1]
        score = 0
        print(photo_name,aadhar_name,address_name,report_name)
        fs = FileSystemStorage()
        fs.save(photo_name,photo)
        fs.save(aadhar_name,aadhar_card)
        fs.save(address_name,addressf)
        fs.save(report_name,report)
        mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
        cursor=mydb.cursor()
        cursor.execute('INSERT INTO volunteer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (request.session["aadhar"], request.session["user_name"], request.session["dob"], request.session["gender"], request.session["email"], request.session["phone_no"], request.session["address"], request.session["password"], request.session["blood"], request.session["allergies"], request.session["height"], request.session["weight"], request.session["history"], request.session["kin_name"], request.session["kin_contact"], request.session["donation"], photo_name, aadhar_name, address_name, report_name, score))
        del request.session["aadhar"]
        del request.session["user_name"]
        del request.session["dob"]
        del request.session["gender"]
        del request.session["email"]
        del request.session["phone_no"]
        del request.session["address"]
        del request.session["password"]
        del request.session["personal"]
        del request.session["blood"]
        del request.session["allergies"]
        del request.session["height"]
        del request.session["weight"]
        del request.session["history"]
        del request.session["kin_name"]
        del request.session["kin_contact"]
        del request.session["donation"]
        del request.session["medical"]
    return render(request,'document.html')

def login(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if loggedin:
        return redirect('v_home')
    else:
        msg=''
        id = request.POST.get('id','')
        password = request.POST.get('password','')
        if(id != '' and password != ''):
            mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
            cursor=mydb.cursor()
            cursor.execute('SELECT * FROM volunteer WHERE email = %s and password = %s', (id, password,))
            account = cursor.fetchone()
            if account:
                request.session['loggedin_volunteer'] = True
                request.session['loggedin_volunteer_email'] = account[4]
                request.session['loggedin_volunteer_aadhar'] = account[0]
                return redirect('v_home')
            else:
                msg = "Invalid Email ID or Password"
        param = {'msg':msg}
        return render(request, 'volunteer_login.html', param)

def logout(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if loggedin:
        request.session['loggedin_volunteer'] = False
    return redirect('home')

def dashboard(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if not loggedin:
        return redirect('login')
    mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
    cursor=mydb.cursor()
    cursor.execute('SELECT blood, height, weight, score FROM volunteer WHERE email = %s', (request.session['loggedin_volunteer_email'],))
    account = cursor.fetchone()
    cursor.execute('SELECT title FROM todo WHERE email = %s', (request.session['loggedin_volunteer_email'],))
    todo = cursor.fetchall()
    cursor.execute('SELECT title FROM todo WHERE email = %s', (request.session['loggedin_volunteer_email'],))
    todo = cursor.fetchall()
    cursor.execute('SELECT * FROM report WHERE aadhar = %s ORDER BY date DESC', (request.session['loggedin_volunteer_aadhar'],))
    report = cursor.fetchall()
    print(report, request.session['loggedin_volunteer_aadhar'])
    height = float(account[1])
    weight = float(account[2])
    bmi = round(weight/(height*height),2)
    underweight = False
    healthy = False
    overweight = False
    if(bmi<18):
        underweight = True
    elif(bmi<22):
        healthy = True
    else:
        overweight = True
    param = {'blood':account[0], 'height':int(height*100), 'weight':weight, 'bmi':bmi, 'underweight':underweight, 'healthy':healthy, 'overweight':overweight, 'todo':todo,'report':report, 'score':account[3]}
    return render(request, 'dashboard.html', param)

def add_todo(request):
    title = request.POST.get('title','')
    if(title != ''):
        mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
        cursor=mydb.cursor()
        cursor.execute('INSERT INTO todo VALUES (%s,%s)', (request.session['loggedin_volunteer_email'],title))
    return redirect('dashboard')

def home(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if not loggedin:
        return redirect('login')
    return render(request, 'hospitals.html')

def search(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if not loggedin:
        return redirect('login')
    pin = request.POST.get('pin','')
    if pin != '':
        mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
        cursor=mydb.cursor()
        cmd = "SELECT * FROM hospital WHERE pin like '"+pin[:4]+"%'"
        cursor.execute(cmd)
        hospital=cursor.fetchall()
        print(hospital)
        if hospital != []:
            found=True
        else:
            found=False
        hosp = []
        for i in hospital:
            hosp.append({'name':i[1], 'id':i[0]})
        param={'hospital':hosp, 'found':found, 'pin':pin}
        return render(request, 'filterHospital.html', param)
    return render(request, 'hospitals.html')

def get_hospital(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if not loggedin:
        return redirect('login')
    id = request.POST.get("id","")
    if id != "":
        request.session["id"]=id
        mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
        cursor=mydb.cursor()
        cursor.execute("SELECT * FROM hospital WHERE id=%s",(id,))
        hospital=cursor.fetchone()
        param = {"name":hospital[1], "about":hospital[2]}
        return render(request, 'parHospital.html', param)
    return redirect('search')

def book(request):
    try:
        loggedin = request.session['loggedin_volunteer']
    except:
        loggedin = False
    if not loggedin:
        return redirect('login')
    motive = request.POST.get("for","")
    date = request.POST.get("date","")
    if motive != "":
        mydb = mysql.connector.connect(host="sql12.freesqldatabase.com",user="sql12607289",password="5FTzUZ9R2q",charset='utf8',database="sql12607289")
        cursor=mydb.cursor()
        cursor.execute('INSERT INTO appointment VALUES (%s,%s,%s,%s)', (request.session['loggedin_volunteer_aadhar'],request.session["id"],motive,date))
    return redirect(search)
    