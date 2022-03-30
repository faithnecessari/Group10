from django.http import Http404
from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from django.contrib import messages
from .forms import *
from .models import *
from JulaneHotel.models import Rooms
from operator import itemgetter

# Create your views here.
class MyIndexView(View):
    def get(self, request):
        return render(request,'index.html', {})

class MyReservationView(View):
    def get(self, request):
        return render(request,'reservation.html', {})

class MyGalleryView(View):
    def get(self, request):
        return render(request,'gallery.html', {})

class MyContactView(View):
    def get(self, request):
        return render(request,'contact.html', {})

class MyAboutView(View):
    def get(self, request):
        return render(request,'about.html', {})

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', context={'form': form})
 
def login(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="julanehotel")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="julanehotel")
    cursor2=con2.cursor()
    sqlcommand="SELECT username from julanehotel_customer"
    sqlcommand2="SELECT password from julanehotel_customer"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        i=0
        k=len(res2)
        while i<k:
            if res[i]==username and res2[i]==password:
                return render(request,'indexCustomer.html',{'username':username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'LogIn.html')

class MyadminLogInView(View):
    def get(self, request):
        return render(request,'adminLogIn.html', {})

def MyCustomerRegistration(request):
    if request.method=="POST":
        customer=Customer()

        firstname = request.POST.get("firstname")         
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        contactnum = request.POST.get("contactnum")

        customer.firstname = firstname
        customer.lastname = lastname        
        customer.username = username
        customer.password = password
        customer.address = address
        customer.contactnum = contactnum
        

     

        if customer.firstname=="" or customer.lastname=="" or customer.username=="" or customer.password=="" or customer.address=="" or customer.contactnum=="":
            messages.info(request,'Some Fields are Empty')
            # return redirect("register")

        else:
            customer.save()
            messages.info(request, 'Successfully Registered!')
            # return render(request,'login.html')
       
    return render(request,'customerRegistration.html')

def MyadminLogInView(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="julanehotel")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="julanehotel")
    cursor2=con2.cursor()
    sqlcommand="SELECT username from julanehotel_admin"
    sqlcommand2="SELECT password from julanehotel_admin"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        i=0
        k=len(res2)
        while i<k:
            if res[i]==username and res2[i]==password:
                return render(request,'adminDashboard.html',{'username':username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'adminLogIn.html')


def MyCustomerRegistration(request):
    if request.method=="POST":
        customer=Customer()

        firstname = request.POST.get("firstname")         
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        contactnum = request.POST.get("contactnum")

        customer.firstname = firstname
        customer.lastname = lastname        
        customer.username = username
        customer.password = password
        customer.address = address
        customer.contactnum = contactnum
        

     

        if customer.firstname=="" or customer.lastname=="" or customer.username=="" or customer.password=="" or customer.address=="" or customer.contactnum=="":
            messages.info(request,'Some Fields are Empty')
            # return redirect("register")

        else:
            customer.save()
            messages.info(request, 'Successfully Registered!')
            # return render(request,'login.html')
       
    return render(request,'customerRegistration.html')

class MyaddRoomView(View):
    def get(self, request):

        return render(request,'addRoom.html') 

    def post(self, request):
        form = RoomsForm(request.POST)

        if form.is_valid():
            roomtype = request.POST.get("roomtype")  
            dateofuse = request.POST.get("dateofuse")       
            timeslot = request.POST.get("timeslot")
            price = request.POST.get("price")
            
            form = Rooms( roomtype=roomtype, dateofuse = dateofuse, timeslot = timeslot, price =price)
            form.save()

            return redirect('my_adminDashboard_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')



class MydashboardCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customers': customers
        }

        return render(request,'dashboardCustomer.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                firstname = request.POST.get("firstname")
                lastname = request.POST.get("lastname")
                username = request.POST.get("username")
                password = request.POST.get("password")
                address = request.POST.get("address")
                contactnum = request.POST.get("contactnum")
             
                
                update_customer = Customer.objects.filter(id = id).update(id = id, firstname = firstname, lastname = lastname, username = username, password = password, address = address, contactnum = contactnum)
                print(update_customer)
                print('profile updated')
                return redirect('my_dashboardCustomer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                customerdel = Customer.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_dashboardCustomer_view')

class MydashboardReservationView(View):
    def get(self, request):
        reservation = Reservation.objects.all()

        context = {
            'reservation': reservation
        }

        return render(request,'dashboardReservation.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                custID = request.POST.get("custID")
                roomID = request.POST.get("roomID")
                #dateofuse = request.POST.get("dateofuse")
             
                
                update_reservation = Reservation.objects.filter(id = id).update(id = id, custID_id = custID, roomID_id = roomID)
                print(update_reservation)
                print('profile updated')
                return redirect('my_dashboardReservation_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Reservation.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_dashboardReservation_view')

class MyCustomerReservationView(View):
    def get(self, request):
        rooms =Rooms.objects.all()
        context = {
           'rooms': rooms
        }

        return render(request,'customerReservation.html') 

    def post(self, request):
        form = ReservationForm(request.POST)

        if form.is_valid():
            custID = request.POST.get("custID")
            roomID = request.POST.get("roomID")
            #roomtype = request.POST.get("roomtype")         
            #timeslot = request.POST.get("timeslot")
            #dateofuse = request.POST.get("dateofuse")
            
            #form = Reservation(roomtype=roomtype, timeslot = timeslot, dateofuse =dateofuse, custID_id= custID)
            form = Reservation(custID_id= custID, roomID_id = roomID)
            form.save()

            return redirect('my_customerReservation_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')


class MyadminDashboardView(View):
    def get(self, request):
        roomsc = Rooms.objects.all()
        rooms = Rooms.objects.all().count()
        reservation = Reservation.objects.all().count()
        customer = Customer.objects.all().count()
        context = {
           'rooms': rooms, 'reservation' : reservation, 'customer': customer, 'roomsc': roomsc
        }

        return render(request,'adminDashboard.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                roomtype = request.POST.get("roomtype")
                timeslot = request.POST.get("timeslot")
                price = request.POST.get("price")
                status = request.POST.get("status")
             
                
                update_room = Rooms.objects.filter(id = id).update(id = id, roomtype = roomtype, timeslot = timeslot, price = price, status = status)
                print(update_room)
                print('profile updated')
                return redirect('my_adminDashboard_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Rooms.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_adminDashboard_view')

class MyCustomerDashboardView(View):
    def get(self, request):
        reservation = Reservation.objects.all()

        context = {
            'reservation': reservation
        }

        return render(request,'customerDashboard.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                custID = request.POST.get("custID")
                roomID = request.POST.get("roomID")
               
             
                
                update_reservation = Reservation.objects.filter(id = id).update(id = id, custID_id = custID, roomID_id = roomID)
                print(update_reservation)
                print('profile updated')
                return redirect('my_customerDashboard_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                resdel = Reservation.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                #return HttpResponse ('post')
                return redirect('my_customerDashboard_view')
            
class MyCustomerProfileView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customers': customers
        }

        return render(request,'customerProfile.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST: 
                print('update profile button clicked')
                id = request.POST.get("id")
                firstname = request.POST.get("firstname")
                lastname = request.POST.get("lastname")
                username = request.POST.get("username")
                password = request.POST.get("password")
                address = request.POST.get("address")
                contactnum = request.POST.get("contactnum")
             
                
                update_customer = Customer.objects.filter(id = id).update(id = id, firstname = firstname, lastname = lastname, username = username, password = password, address = address, contactnum = contactnum)
                print(update_customer)
                print('profile updated')
                messages.info(request,"Successfully Updated!")
                return redirect('my_customerProfile_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                customerdel = Customer.objects.filter(id=id).delete()
                # pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
                messages.info(request,"Successfully Deleted!")
                #return HttpResponse ('post')
                return redirect('my_customerProfile_view')


def searchRoom(request):
    if request.method == "POST":
        searched = request.POST['searched']
        rooms = Rooms.objects.filter(dateofuse__contains=searched)
        return render(request, 'searchRoom.html',{'searched': searched, 'rooms':rooms})

    else:
        return render(request, 'searchRoom.html',{})