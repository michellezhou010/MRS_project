#encoding:utf8
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from df_goods.models import GoodsInfo
from .models import UserInfo
from hashlib import sha1    # set password
from . import user_decorator
import re                 # email 
import pdb

# Create your views here.

def register(request):
    return render(request, 'df_user/register.html',{'title':'Register for Customer'})

def register_handle(request):   
    #Input
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 =post.get('cpwd')
    uemail = post.get('email')

    

    # # if set password
    # if not (uname and upwd and upwd2 and uemail):
    #     return redirect('/user/register/')
    #
    # # check if the length of name is vaild
    # if len(uname)<5 or len(uname)>20:
    #     return redirect('/user/register/')
    #
    # #if name exists already in our database
    # if UserInfo.objects.filter(uname=uname).count() != 0:
    #     return redirect('/user/register/')
    #
    # #check the password twice
    # if upwd != upwd2 or len(upwd) < 8 or len(upwd) > 20 :
    #     return redirect('/user/register/')
    #
    # # check the email address
    # if re.match("^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", uemail) == None:  # re.match, if fail return None
    #     return redirect('/user/register/')

    
    s1 = sha1()
    s1.update(upwd.encode("utf-8"))     
    upwd3 = s1.hexdigest()      

    #create user 
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()

    #success for new user
    return redirect('/user/login/')

def register_exist(request):    #if exists 
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()    #count = 0? 1
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')     #get cookie
    context = {'title':'用户登录', 'error_name':0, 'error_pwd':0, 'uname': uname}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
   
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu=post.get('jizhu', 0)      

    users = UserInfo.objects.filter(uname=uname)  

    # check user name and password
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode("utf-8"))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url','/')    
            red = HttpResponseRedirect(url)   #Cookie
            #user name
            if jizhu != 0:
                red.set_cookie('uname',uname)       #set cookie and store user name
            else:
                red.set_cookie('uname','', max_age=-1)  #max_age
            request.session['user_id'] = users[0].id    #user_id and name into session
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'Login', 'error_name':0, 'error_pwd':1, 'uname':uname, 'upwd':upwd}
            return render(request, 'df_user/login.html', context)
    context = {'title': 'Login', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
    return render(request, 'df_user/login.html', context)

def logout(request):
    # request.session.flush()     # clear seesion
    del request.session['user_id']
    del request.session['user_name']
    return redirect('/')

@user_decorator.login
def info(request):      #personal info
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    user_address = UserInfo.objects.get(id=request.session['user_id']).uaddress
    # goods_ids = request.COOKIES.get('goods_ids', '')   
    # goods_ids1 = goods_ids.split(',')   
    goods_ids1=request.session.get(str(request.session['user_id']),'')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.filter(id=int(goods_id)).values())
        # goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    # pdb.set_trace() 
    context = {'title':'Account',
               'user_name':request.session['user_name'],
               'user_email': user_email,
               'goods_list':goods_list,
               'user_address':user_address,
            }
    #pdb.set_trace() 
    print(context)
    print("----------------")
    return render(request, 'df_user/user_center_info.html', context)

@user_decorator.login
def order(request):     # all orders
    context = {'title': 'Account'}
    return render(request, 'df_user/user_center_order.html', context)

@user_decorator.login
def site(request):      #address
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        if not(user.ushou and user.uaddress and user.uaddress and user.uphone):
            return redirect('/user/site/')
    context = {'title': 'Account', 'user': user}
    user.save()
    return render(request, 'df_user/user_center_site.html', context)
