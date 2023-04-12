from django.shortcuts import render

# Create your views here.
def botany(request):
    d={'name':'TEJA'}
    return render(request,'botany.html',context=d)
