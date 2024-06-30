from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('registration_success')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

""" 
def index(reuest):
    user = models.User.username
    password = models.User.password
    high_score = models.User.high_score
    
    context = {
        'password':password,
        'user':user,
        'high_score':high_score
    }
    
    return render(request, 'index.html', context)
    
"""
