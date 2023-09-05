from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from.models import hexa,pay,userlog,contact,subscribe
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.
def readdata(request):
    data=hexa.objects.all()
    return render(request,'readdata.html',{'data':data})

def usersignup(request):
    if request.method=="POST":
     name=request.POST['name']
     email=request.POST['mail']
     password=request.POST['pass']
     repeatpassword=request.POST['rpass']
     print(name,email,password,repeatpassword)
     obj=User.objects.create_user(username=name,email=email,password=password)
     obj.save()
    return render(request,'signup.html')
def userlogin(request):
    if request.method=="POST":
        Username=request.POST['name']
        password=request.POST['pass']    
        print(Username, password)
        obj=authenticate(request,username=Username,password=password)
        if obj:
            login(request,obj)
            # return HttpResponse('user login')
            return redirect(userindex)
           
        else:
            return HttpResponse('invalid user')
    return render(request,'login.html')
def userlogout(request):
    logout(request)

    return render(request,'login.html')
def userproduct(request):
    data=hexa.objects.all
    return render(request,'products.html',{'data':data})
def usersingleproduct(request,id):
    userdata=hexa.objects.get(id=id)
    print(userdata.image,userdata.name,userdata.price,userdata.discription)
    
    return render(request,'single-product.html',{'userdata':userdata,'id':id})
def userindex(request):
    accessories=hexa.objects.filter(categories='Accessories')
    mens=hexa.objects.filter(categories="Mens")
    womens=hexa.objects.filter(categories="Womens")
    kids=hexa.objects.filter(categories="Kids")
    print(accessories,mens,womens,kids,'=============================')
    for i in accessories:
        print(i,'------')                        
    data={'accessories':accessories,'mens':mens,'womens':womens,'kids':kids}
    return render(request,'index.html',{'accessories':accessories,'mens':mens,'womens':womens,'kids':kids})

def usercontact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email'] 
        message=request.POST['message']
        print(name,email,message)
        usercontact=contact(name=name,email=email,message=message)
        usercontact.save()
        return HttpResponse('message saved')
    return render(request,'contact.html')
def userabout(request):
    return render(request,'about.html')
def usercart(request):
    if request.method=="POST":
         image=request.FILES['img']
         name=request.POST['name']
         price=request.POST['price']
         discription=request.POST['disp']
         categories=request.POST['cat']
         print(image,name,price,discription,categories)
         userdata=hexa(image=image,name=name,price=price,discription=discription,categories=categories)
         userdata.save()
          
         return HttpResponse('data succesfully entered')

    return render(request,'cart.html')
def deletedata(request,id):
    userdata=hexa.objects.get(id=id)
    userdata.delete()
    return redirect(readdata)
def updatedata(request,id):
    userdata=hexa.objects.get(id=id)
    if request.method=="POST":
        image=request.FILES['img']
        name=request.POST['name']
        price=request.POST['price']
        discription=request.POST['disp']
        userdata.image=image
        userdata.name=name
        userdata.price=price
        userdata.discription=discription
        userdata.save()
        return redirect(readdata)
    
    return render(request,'cart.html',{'userdata':userdata})
def userpayment(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['mail']
        streetaddress=request.POST['address']
        streetaddressline2=request.POST['saddress']
        city=request.POST['city']
        state=request.POST['state']
        zipcode=request.POST['code']
        print(firstname,lastname,email,streetaddress,streetaddressline2,city,state,zipcode)
        paydata=pay(firstname=firstname,lastname=lastname,email=email,streetaddress=streetaddress,streetaddressline2=streetaddressline2,city=city,state=state,zipcode=zipcode)
        paydata.save()
        return HttpResponse('payment done')
    return render(request,'payment.html')
def userdetails(request,id):
    print(id,'----000000------')
    logd = userlog.objects.filter(userdata=request.user)
    user_pay_instance = hexa.objects.get(id = id)  # Retrieve the hexa instance
    userobj = userlog(userdata=request.user,user_pay = user_pay_instance)
    userobj.save()
    print(logd)
    total_price = 0
    totalitem =0
    # Iterate through the logs and sum up the prices
    for log in logd:
        vv = int(log.user_pay.price)
        total_price += vv
        totalitem = totalitem+1
    return render(request,'details.html',{'logd':logd,'totalitem':totalitem,'total_price':total_price})

    # return HttpResponse("after delete data")

def hexadelete(request,id):
    print(id,'----==0=-=-=-=-=-=-')
    userdata=userlog.objects.get(id=id)
    userdata.delete()
    idd = request.user.id
    print(idd,'-------')
    logd = userlog.objects.filter(userdata=request.user)
    print(logd)
    total_price = 0
    totalitem =0
    # Iterate through the logs and sum up the prices
    for log in logd:
        vv = int(log.user_pay.price)
        total_price += vv
        totalitem = totalitem+1
    return render(request,'details.html',{'logd':logd,'totalitem':totalitem,'total_price':total_price})
    # return redirect('newdetails',idd)

def usersubscribe(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        print(name,email)
        subscriber= subscribe(name=name,email=email)
        subscriber.save()
        subject ="Your Account Needs To Be verified"
        message =f"hi paste the link to verify your account "
        email_from = settings.EMAIL_HOST_USER
        receipt_list = [email]
        send_mail(subject,message,email_from,receipt_list)
        return HttpResponse('mail sent successfully')
    return render(request,'contact.html')
def userfilter(request):
    if request.method=="POST":
        
        cat = request.POST['categories']
        print(cat,'---------')
        bb = hexa.objects.filter(categories=cat)

        return render(request,'filter.html',{'bb':bb})
    # return render(request,'filter.html')

def send_mails(request):
    email = 'sk3354580@gmail.com'
    subject ="Your Account Needs To Be verified"
    message =f"hi paste the link to verify your account "
    email_from = settings.EMAIL_HOST_USER
    receipt_list = [email]
    send_mail(subject,message,email_from,receipt_list)
    return HttpResponse('mail sent')