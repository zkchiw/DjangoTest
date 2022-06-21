from django.shortcuts import render

# Create your views here.
def join(request):
    return render(request, 'members/join.html')

def login(request):
    return render(request, 'members/login.html')

def myinfo(request):
    return render(request, 'members/myinfo.html')