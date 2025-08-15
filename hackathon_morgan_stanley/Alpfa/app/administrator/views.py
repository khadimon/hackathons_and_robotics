# administrator/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



def admin_home(request):
    return render(request, 'administrator/admin_home.html') 



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Method:", request.method)
        print("Username:", username)
        print("Password:", password)



        user = authenticate(request, username=username, password=password)
        print("Super user: ",user.is_superuser)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin-home')  # Redirect to admin home
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('admin-login')

    return render(request, 'administrator/admin_login.html')

