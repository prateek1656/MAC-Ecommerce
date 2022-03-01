from django.db.models import query
from django.shortcuts import render
from .models import Orders, Product , OrderUpdates
from math import ceil
from datetime import timedelta
import json

# Create your views here.
from django.http import HttpResponse, response

def index(request):
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        Prod = Product.objects.filter(category = cat)
        n = len(Prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([Prod, range(1,nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query,item):
    '''return true only if the item matches the search'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        RawProd = Product.objects.filter(category = cat)
        Prod = [item for item in RawProd if searchMatch(query,item)]

        n = len(Prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        if len(Prod)!=0:
            allProds.append([Prod, range(1,nSlides), nSlides])
    params = {'allProds': allProds,'msg':''}
    if len(allProds) == 0 or len(query)<2:
        params = {'msg':"No items found related to your query, Please chech again the serch item, query must be longer than 2 chars to be noted"}
    return render(request, 'shop/search.html',params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return render(request, 'shop/contact.html')
def tracker(request):
    if request.method == "POST":
        order_id=request.POST.get('orderID','')
        email = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=order_id,email = email)
            if len(order) > 0:
                update = OrderUpdates.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc,'time':item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')
def productview(request,myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/productView.html', {'product':product[0]})
def checkout(request):
    if request.method == "POST":
        items_json=request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2'+'')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        order = Orders(items_json = items_json ,name = name,email = email,address = address,city=city,state=state,zip_code = zip_code,phone =phone)
        order.save() 
        thank = True
        id = order.order_id
        update = OrderUpdates(order_id = id , update_desc = "Order has been placed successfully")
        update.save()
        deliveryDate = order.order_date.date() + timedelta(days=10)
        return render(request, 'shop/checkout.html',{'thank':thank,'id':id,'deliveryDate':deliveryDate})
    return render(request, 'shop/checkout.html')