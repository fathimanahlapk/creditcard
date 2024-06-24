from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class branch(models.Model):
    branch_name=models.CharField(max_length=200)
    ifsc=models.CharField(max_length=200)
    pincode=models.IntegerField()
    email=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class customer(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.BigIntegerField()
    image=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    account_no=models.CharField(max_length=200)
    amount=models.CharField(max_length=200, default=0)
    BRANCH=models.ForeignKey(branch,default=1,on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)


class atm_card(models.Model):
    request_date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    card_no=models.CharField(max_length=200)
    cvv=models.CharField(max_length=200)
    exp_date=models.CharField(max_length=200)
    USER=models.ForeignKey(customer,default=1,on_delete=models.CASCADE)


class complaints(models.Model):
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(customer,default=1,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    reply_date=models.CharField(max_length=200)

class feedbacks(models.Model):
    date=models.CharField(max_length=200)
    USER=models.ForeignKey(customer,default=1,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)

class transactions(models.Model):
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    USER=models.ForeignKey(customer,default=1,on_delete=models.CASCADE)
    amount=models.CharField(max_length=200)
    type=models.CharField(max_length=200)


class block_details(models.Model):
    ATM_CARD=models.ForeignKey(atm_card,default=1,on_delete=models.CASCADE)
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200, default="")
    status=models.CharField(max_length=200)
    image=models.CharField(max_length=200, default="")

class authorized_person(models.Model):
    name=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    USER=models.ForeignKey(customer,default=1,on_delete=models.CASCADE)




























