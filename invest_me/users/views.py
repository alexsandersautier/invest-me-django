from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def new_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'The user {user} has been successfully registered')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})