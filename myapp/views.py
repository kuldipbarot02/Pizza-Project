from django.shortcuts import render,redirect
from . models import User,Pizza
    
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Alredy Registerd"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    usertype=request.POST['usertype'],

                )
                msg="User Sign Up Successfully"
                return render(request,'signup.html',{'msg':msg})
            else:
                msg="Password & Confirm Password Does Not Matched"
                return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                if user.usertype=='buyer':
                    return render (request,'index.html')
                else:
                    return render (request,'seller-index.html')

            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Email Not Registerd"
            return render(request,'login.html',{'msg':msg})        
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')
    
def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user. password=request.POST['new_password']
                user.save()
                return redirect ('logout')
            else:
                msg="New password & Confirm New Password Does Not Matched"
                if user.usertype=="buyer":
                    return render(request,'change-password.html',{'msg',msg})
                else:
                    return render(request,'seller-change-password.html',{'msg',msg})
                    
        else:
            msg="Old Password Does Not Matched"
            if user.usertype=="buyer":
                return render(request,'change-password.html',{'msg',msg})
            else:
                return render(request,'change-password.html',{'msg',msg})

    else:
        if user.usertype=="buyer":
            return render(request,'change-password.html')    
        else:
            return render(request,'change-password.html')    
    


def menu(request):
    return render(request,'menu.html')

def services(request):
    return render(request,'services.html')

def seller_add_pizza(request):
    if request.method=="POST":
        seller=User.objects.get(email=request.session['email'])
        Pizza.objects.create(
            seller=seller,
            pizza_category=request.POST['pizza_category'],
            pizza_types=request.POST['pizza_types'],
            pizza_size=request.POST['pizza_size'],
            pizza_price=request.POST['pizza_price'],
            pizza_pic=request.FILES['pizza_pic'],
        )
        msg="Pizza Added Successfully"
        return render(request,'seller-add-pizza.html',{'msg':msg})
    else:
        return render(request,'seller-add-pizza.html')
    
def seller_view_pizza_order(request):
    seller=User.objects.get(email=request.session['email'])
    pizzas=Pizza.objects.filter(seller=seller)
    return render(request,'seller-view-pizza-order.html',{'pizzas':pizzas})

    
