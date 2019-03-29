from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import CartInfo
from df_user import user_decorator

# Create your views here.
@user_decorator.login
def cart(request):      #cart
    uid =request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'page_name':1,
        'carts':carts,
    }
    return render(request, 'df_cart/cart.html', context)

@user_decorator.login
def add(request, gid, count):       #item id and QTY
    if int(gid)==0 and request.is_ajax() and int(count)==0:
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()     # get user ingo 
        return JsonResponse({'count':count})
    uid = request.session['user_id']        #get user id
    gid = int(gid)  #to int
    count = int(count)
    #check if exists in cart already, if not, add 
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()
    #ajax 
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()    
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')   

def edit(request,gid,count):
    try:
        if request.is_ajax():
            goods = CartInfo.objects.get(id=int(gid))
            goods.count=int(count)
            goods.save()
            data={'ok':1}
    except Exception as e:
        data={'ok':int(count)}
    return JsonResponse(data)

def delete(request,gid):
    try:
        if request.is_ajax():
            goods=CartInfo.objects.get(id=int(gid))
            goods.delete()
            data={'ok':1}
            print(1111)
    except Exception as e:
        data={'ok':0,'e':e}
    return JsonResponse(data)

def place_order(request):
    uid =request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'cart',
        'page_name':1,
        'carts':carts,
    }
    return render(request,'df_cart/place_order.html',context)


