from django.shortcuts import render, HttpResponse, redirect
prices= {
    '1001':50.00,
    '1002':20.00,
    '1003':10.00,
    '1004':30.00}
def index(request):
    return render(request, 'store/index.html', {'prices':prices})

def process(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count']=0
        request.session['total']=0

    request.session['count']+=int(request.POST['quantity'])
    quantity=int(request.POST['quantity'])
    product_id=request.POST['product_id']
    request.session['order']=quantity*int(prices[product_id])
    request.session['total']=request.session['total']+request.session['order']

    return redirect('/amadon/checkout')

def cart(request):
    return render(request, 'store/checkout.html')

def secretclear(request):
    del request.session['count']
    del request.session['order']
    del request.session['total']
    return redirect('/')
