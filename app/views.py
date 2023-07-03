from django.shortcuts import render
from app.models import *

# Create your views here.

def view_table(request):
    if request.method=="GET":
        resp=render(request, 'app/table.html')
        return resp
    elif request.method=="POST":
        s=Customer.objects.all()
        d1={'cus':s}
        resp=render(request, 'app/table.html', context=d1)
        return resp