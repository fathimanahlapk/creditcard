
from django.contrib import admin
from django.urls import path

from Secure_ATM_app import views

urlpatterns = [

    path('logout',views.logout),
    path('add_branch',views.add_branch),
    path('add_branch_post',views.add_branch_post),
    path('edit_branch/<id>',views.edit_branch),
    path('edit_branch_post/<id>',views.edit_branch_post),
    path('delete_branch/<id>',views.delete_branch),
    path('',views.loginn),
    path('login_post',views.login_post),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_branch',views.view_branch),
    path('view_complaints',views.view_complaints),
    path('view_customers/<id>',views. view_customers),
    path('view_feedback',views.view_feedback),
    path('adminhome',views.adminhome),
    path('view_forwarded_atm_request',views.view_forwarded_atm_request),
    path('approve_atm_request/<id>',views.approve_atm_request),
    path('approve_atm_request_post/<id>',views.approve_atm_request_post),
    path('reject_request/<id>',views.reject_request),
    path('approve_atm_request_post',views.approve_atm_request_post),
    path('add_customer',views.add_customer),
    path('add_customer_post',views.add_customer_post),
    path('edit_customer/<id>',views.edit_customer),
    path('edit_customer_post/<id>',views.edit_customer_post),
    path('delete_customer/<id>',views.delete_customer),
    path('view_atm_card_request',views.view_atm_card_request),
    path('forward_req/<id>',views.forward_req),
    path('view_customer',views.view_customer),
    path('branch_add_deposit/<id>',views.branch_add_deposit),
    path('branch_add_deposit_post/<id>',views.branch_add_deposit_post),
    path('branch_view_transactions/<id>',views.branch_view_transactions),
    path('view_profile',views.view_profile),
    path('view_block_details',views.view_block_details),
    path('unblock/<id>',views.unblock),
    path('approved_req',views.approved_req),
    path('branch_home',views.branch_home),
    # =================================================
    path('send_complaint',views.send_complaint),
    path('send_complaint_post',views.send_complaint_post),
    path('send_feedback',views.send_feedback),
    path('send_feedback_post',views.send_feedback_post),
    path('view_card_details',views.view_card_details),
    path('view_profile_user',views.view_profile_user),
    path('view_reply',views.view_reply),
    path('user_home',views.user_home),
    path('user_block_details',views.user_block_details),
    path('send_request/<id>',views.send_request),
    path('add_authorized_person',views.add_authorized_person),
    path('add_authorized_person_post',views.add_authorized_person_post),
    path('view_authorised_person',views.view_authorised_person),
    path('delete_authorized_person/<id>',views.delete_authorized_person),
    path('view_transactions',views.view_transactions),
    path('user_send_request',views.user_send_request),










]