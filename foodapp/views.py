from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'foodapp/index.html')

def login_view(request):
    return render(request, 'login.html')