import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Secure_ATM_app.models import *
import random
# Create your views here.

static_path=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"

def add_branch(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")

    return render(request,'admin/add_branch.html')

def add_branch_post(request):
    branch_name=request.POST['textfield']
    ifsc=request.POST['textfield2']
    pincode=request.POST['textfield3']
    phone= request.POST['textfield4']
    email = request.POST['textfield5']
    password=random.randint(1000,9999)
    obj1=login()
    obj1.username=email
    obj1.password=password
    obj1.usertype="branch"
    obj1.save()
    obj=branch()
    obj.branch_name=branch_name
    obj.ifsc=ifsc
    obj.pincode=pincode
    obj.email=email
    obj.phone=phone
    obj.LOGIN=obj1
    obj.save()
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("fathimazakki456@gmail.com", "pqhl syxk oddi nrmk")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "fathimazakki456@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your Password"
    body = "Your Password is:- - " + str(password)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Successfully added');window.location='/adminhome'</script>")


def delete_branch(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    login.objects.filter(id=id).delete()
    return redirect('/view_branch#products')


def edit_branch(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=branch.objects.get(id=id)
    return render(request,'admin/edit_branch.html',{"data":qry,"id":id})

def edit_branch_post(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    branch_name = request.POST['textfield']
    ifsc = request.POST['textfield2']
    pincode = request.POST['textfield3']
    phone = request.POST['textfield5']
    email = request.POST['textfield4']
    branch.objects.filter(id=id).update(branch_name=branch_name,ifsc=ifsc,pincode=pincode,phone=phone,email=email)
    return HttpResponse("<script>alert('Successfully updated');window.location='/view_branch#products'</script>")


def loginn(request):
    return render(request,'loginindex.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    qry=login.objects.filter(username=username,password=password)
    if qry.exists():
        request.session['lid']=qry[0].id
        request.session['log']="lo"
        if qry[0].usertype=="admin":
            return HttpResponse("<script>alert('Login success');window.location='/adminhome'</script>")
        elif qry[0].usertype=="branch":
            return HttpResponse("<script>alert('Login Success');window.location='/branch_home'</script>")
        elif qry[0].usertype == "user":
            return HttpResponse("<script>alert('Login Success');window.location='/user_home'</script>")
        else:
            return HttpResponse("<script>alert('user not found');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('user not found');window.location='/'</script>")




def send_reply(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'admin/send_reply.html',{"id":id})

def send_reply_post(request,id):
    reply=request.POST['textarea']
    complaints.objects.filter(id=id).update(reply=reply,reply_date=datetime.datetime.now().strftime("%Y-%m-%d"))
    return HttpResponse("<script>alert('Reply send');window.location='/view_complaints#products'</script>")


def view_branch(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=branch.objects.all()
    return render(request,'admin/view_branch.html',{"data":qry})

def view_complaints(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=complaints.objects.all()
    return render(request,'admin/view_complaints.html',{"data":qry})

def view_customers(request, id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=customer.objects.filter(BRANCH_id=id)
    return render(request,'admin/view_customers.html',{"data":qry})

def view_feedback(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=feedbacks.objects.all()
    return render(request,'admin/view_feedback.html',{"data":qry})

def adminhome(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'admin/admin_index.html')

def approve_atm_request(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    request.session['rid']=id
    return render(request,'admin/approve_atm_request.html',{"id":id})

def approve_atm_request_post(request,id):
    card_no=request.POST['textfield']
    cvv=request.POST['textfield2']
    exp_date=request.POST['textfield3']
    atm_card.objects.filter(id=id).update(status="approved",card_no=card_no,cvv=cvv,exp_date=exp_date)
    return redirect('/view_forwarded_atm_request#products')



def view_forwarded_atm_request(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=atm_card.objects.filter(status="Forwarded_to_admin")
    return render(request,'admin/view_forwarded_atm_request.html',{"data":qry})


def reject_request(request,id):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    atm_card.objects.filter(id=id).update(status="rejected")
    return redirect('/view_forwarded_atm_request#products')


def add_customer(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'branch/add_customer.html')

def add_customer_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    image=request.FILES['fileField']
    phone=request.POST['textfield4']
    gender=request.POST['radio']
    account_no=request.POST['textfield5']
    d=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs=FileSystemStorage()
    fs.save(static_path + "images\\" + d +".jpg", image)
    path="/static/images/"+ d +".jpg"
    password=random.randint(0000,9999)
    obj1=login()
    obj1.username=email
    obj1.password=password
    obj1.usertype="user"
    obj1.save()

    obj=customer()
    obj.name=name
    obj.email=email
    obj.phone=phone
    obj.image=path
    obj.gender=gender
    obj.account_no=account_no
    obj.LOGIN=obj1
    obj.BRANCH=branch.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("fathimazakki456@gmail.com", "pqhl syxk oddi nrmk")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] ="fathimazakki456@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Your Password"
    body = "Your Password is:- - " + str(password)
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script> alert('Successfully added');window.location='/branch_home'</script>")







def edit_customer(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=customer.objects.get(id=id)
    return render(request,'branch/edit_customer.html',{"data":qry,"id":id})

def edit_customer_post(request,id):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    account_no=request.POST['textfield4']
    if "fileField" in request.FILES:
        image = request.FILES['fileField']
        d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fs = FileSystemStorage()
        fs.save(static_path + "images\\" + d + ".jpg", image)
        path = "/static/images/" + d + ".jpg"
        customer.objects.filter(id=id).update(image=path)
    customer.objects.filter(id=id).update(name=name, email=email, phone=phone, account_no=account_no)
    return HttpResponse("<script>alert('Successfully updated');window.location='/view_customer#products'</script>")

def delete_customer(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    login.objects.filter(id=id).delete()
    return redirect('/view_customer#products')


def view_atm_card_request(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=atm_card.objects.filter(USER__BRANCH__LOGIN_id=request.session['lid'], status='pending')
    return render(request,'branch/view_atm_card_request.html',{'data':qry})

def forward_req(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    atm_card.objects.filter(id=id).update(status="Forwarded_to_admin")
    return redirect('/view_atm_card_request#products')

def view_customer(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=customer.objects.filter(BRANCH__LOGIN_id=request.session['lid'])
    return render(request,'branch/view_customer.html', {'data':qry})

def branch_add_deposit(request, id):
    return render(request, "branch/add_deposit.html", {'id':id})


def branch_add_deposit_post(request, id):
    amt=request.POST['textfield']
    obj=transactions()
    obj.date=datetime.datetime.now().strftime("%Y-%m-%d")
    obj.time=datetime.datetime.now().strftime("%H:%M")
    obj.amount=amt
    obj.type="Deposit"
    obj.USER_id=id
    obj.save()
    res=customer.objects.get(id=id)
    old_amt=res.amount
    res.amount=int(old_amt)+int(amt)
    res.save()
    return HttpResponse("<script>alert('Transaction added');window.location='/view_customer#products'</script>")

def branch_view_transactions(request, id):
    res=transactions.objects.filter(USER_id=id).order_by("-id")
    return render(request, "branch/view_transactions.html", {'data':res})


def view_profile(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry = branch.objects.get(LOGIN=request.session['lid'])
    return render(request,'branch/view_profile.html',{"data":qry})

def branch_home(request):
    return render(request,'branch/branch_index.html')

def approved_req(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=atm_card.objects.filter(USER__BRANCH__LOGIN_id=request.session['lid'], status='Approved')
    return render(request,'branch/approved_req.html',{'data':qry})

def view_block_details(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=block_details.objects.filter(ATM_CARD__USER__BRANCH__LOGIN_id=request.session['lid'],status="pending")
    print(qry)
    return render(request,'branch/view_block_details.html',{'data':qry})

def unblock(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    res=block_details.objects.get(id=id)
    cid=res.ATM_CARD_id
    res.status="Unblocked"
    res.save()
    atm_card.objects.filter(id=cid).update(status="approved")
    return redirect('/view_block_details#products')


def send_complaint(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/view_reply'</script>")
    return render(request,'user/send_complaint.html')

def send_complaint_post(request):
    complaint=request.POST['textarea']
    obj=complaints()
    obj.date= datetime.datetime.now().strftime("%Y-%m-%d")
    obj.complaint=complaint
    obj.reply="pending"
    obj.reply_date="pending"
    obj.USER=customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Successfully sent');window.location='/send_complaint#products'</script>")

def send_feedback(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'user/send_feedback.html')

def send_feedback_post(request):
    feedback = request.POST['textarea']
    r = request.POST['r']
    obj=feedbacks()
    obj.date= datetime.datetime.now().strftime("%Y-%m-%d")
    obj.feedback=feedback
    obj.rating=r
    obj.USER=customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Successfully sent');window.location='/send_feedback#products'</script>")

def view_card_details(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=atm_card.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/view_card_details.html',{"data":qry})

def view_profile_user(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=customer.objects.get(LOGIN=request.session['lid'])
    return render(request,'user/view_profile_user.html',{"data":qry})

def view_reply(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=complaints.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/view_reply.html',{"data":qry})

def user_home(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'user/user_index.html')

def user_block_details(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry=block_details.objects.filter(ATM_CARD__USER__LOGIN=request.session['lid'], status="blocked").order_by("-id")
    return render(request,'user/user_block_details.html',{"data":qry})


def send_request(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    block_details.objects.filter(id=id).update(status="pending")
    return HttpResponse("<script>alert('Successfully sent');window.location='/user_block_details#products'</script>")

def add_authorized_person(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    return render(request,'user/add_authorized_person.html')


def add_authorized_person_post(request):
    name=request.POST['textfield']
    image=request.FILES['textfield2']
    d = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs = FileSystemStorage()
    fs.save(static_path + "images\\" + d + ".jpg", image)
    path = "/static/images/" + d + ".jpg"
    obj=authorized_person()
    obj.name=name
    obj.image=path
    obj.USER=customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Authorized person added.');window.location='/add_authorized_person#products'</script>")

def view_authorised_person(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    qry = authorized_person.objects.filter(USER__LOGIN=request.session['lid'])
    return render(request,'user/view_authorised_person.html', {"data": qry})

def delete_authorized_person(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    authorized_person.objects.filter(id=id).delete()
    return redirect('/view_authorised_person#products')

def view_transactions(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('You are logged out');window.location='/'</script>")
    res = transactions.objects.filter(USER__LOGIN_id=request.session['lid']).order_by("-id")
    return render(request,'user/view_transactions.html',{"data":res})

def user_send_request(request):
    obj = atm_card()
    obj.request_date = datetime.datetime.now().strftime("%Y-%m-%d")
    obj.status = "pending"
    obj.card_no = "pending"
    obj.cvv = "pending"
    obj.exp_date = "pending"
    obj.USER = customer.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Successfully sent');window.location='/user_home#products'</script>")



def logout(request):
    request.session['log']=""
    return redirect('/')

