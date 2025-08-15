from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    return render(request, 'register.html')

def user_view(request):
    return render(request, 'user.html')

def admin_view(request):
    return render(request, 'admin.html')
