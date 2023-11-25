from django.shortcuts import render

# Create your views here.
def mycard(request):
    return render(request,'mycard.html')

def pavi(request):
    return render(request,'pavi.html')