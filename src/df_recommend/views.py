from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import TypeInfo, GoodsInfo
import ast
import pdb

# Create your views here.
def index(request):            
   
    typelist = TypeInfo.objects.all()        
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]         
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context = {
        'title':'Home',
        'type0':type0, 'type01':type01,
        'type1':type1, 'type11':type11,
        'type2':type2, 'type21':type21,
        'type3':type3, 'type31':type31,
        'type4':type4, 'type41':type41,
        'type5':type5, 'type51':type51,
    }
    return render(request, 'df_recommend/index.html', context)

def list(request, tid, pindex, sort):  
    typeinfo = TypeInfo.objects.get(id=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]  
    if sort == '1':   
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
        # print(22233)
    elif sort == '2':     
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    elif sort == '3':
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list,100)        
    page = paginator.page(int(pindex))         
    context = {
        'title':typeinfo.ttitle,    
        'page':page,        
        'typeinfo':typeinfo,    
        'news':news,    
        'sort':sort,    
        'paginator':paginator,  
    }
    return render(request, 'df_recommend/all.html', context)

def detail(request, id):        
    goods = GoodsInfo.objects.get(id=int(id))
    goods.gclick = goods.gclick + 1     
    goods.save()
    bought = []
    al_buy = []
    view = []
    item_buy = []
    list_b = []
    if goods.galso_buy is not None:
        
        list_b = goods.galso_buy.split(',')
        
        for b in list_b: 
            if GoodsInfo.objects.filter(gasin=str(b)).exists():
                b_info = GoodsInfo.objects.filter(gasin=str(b)).values('gtitle','gpic','gprice','gunit')
                item_buy.append(b_info[0])
                
        # item_buy.append(GoodsInfo.objects.get(gasin=b)) 
   
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title': goods.gtype.ttitle,
        'goods':goods,
        'news':news,
        'id': id,
        'bought':bought,
        'al_buy':al_buy,
        'view':view,
        'buy_list': item_buy,
    }
    response = render(request, 'df_recommend/detail_r.html', context)


    # #recently viewed
    if request.session.has_key('user_id'):   #check if logged in
        goods_ids = request.COOKIES.get('goods_ids','')     #browsing history
        # print(type(goods_ids))
        # print(goods_ids)
        goods_id = str(goods.id)        #convert int to string
        if goods_ids != '':     #if viewed
            goods_ids1 = goods_ids.split(',')   
            if goods_ids1.count(goods_id) >= 1:     #if exist deleted
                goods_ids1.remove(goods_id)
            goods_ids1.insert(0, goods_id)  #add to the first item
            if len(goods_ids1) >= 6:        #delete if greater than 6
                del goods_ids1[5]
            goods_ids=','.join(goods_ids1)     #  's'.join(seq)  
        else:
            goods_ids=goods_id      # add records
        # print(type(goods_ids))
        # print(goods_ids)
        response.set_cookie('goods_ids',goods_ids)  # insert into cookie

    
    if request.session.has_key('user_id'):   #
        key=str(request.session.get('user_id'))
        goods_ids=request.session.get(key,'')
        # print(type(goods_ids))
        # print(goods_ids)
        goods_id = str(goods.id)  # 
        if goods_ids != '':  
            # goods_ids = goods_ids.split(',')  
            if goods_ids.count(goods_id) >= 1:  
                goods_ids.remove(goods_id)
            goods_ids.insert(0, goods_id)  
            if len(goods_ids) >= 6:  
                del goods_ids[5]
        else:
            goods_ids = []
            goods_ids.append(goods_id)
        # print(type(goods_ids))
        # print(goods_ids)
        request.session[key]=goods_ids
    return response

# from haystack.views import SearchView
# class MySearchView(SearchView):
#     def extra_context(self):
#         context=super(MySearchView,self).extra_context()
#         context['title']='搜索'
#         context['guest_cart']=1
#         return context

from haystack.views import SearchView
from mrs.settings import HAYSTACK_SEARCH_RESULTS_PER_PAGE

class MySearchView(SearchView):
    def build_page(self):
        #page rewriting
        context=super(MySearchView, self).extra_context()   # context
        try:
            page_no = int(self.request.GET.get('page', 1))
        except Exception:
            return HttpResponse("Not a valid number for page.")

        if page_no < 1:
            return HttpResponse("Pages should be 1 or greater.")
        a =[]
        for i in self.results:
            a.append(i.object)
        paginator = Paginator(a, HAYSTACK_SEARCH_RESULTS_PER_PAGE)
        # print("--------")
        # print(page_no)
        page = paginator.page(page_no)
        return (paginator,page)

    def extra_context(self):
        context = super(MySearchView, self).extra_context()  # context
        context['title']='Search'
        return context