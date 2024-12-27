from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from drophutApp.models import Product
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView

# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')  # Redirect to login after successful registration
#          else:
#             print(form.errors)  # Print form errors
#     else:
#         form = RegistrationForm()
#     return render(request, 'user/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                print(user.username)
                print(user.email)
                user.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
            except Exception as e:
                print(f"Error saving user: {e}")
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    form_class = PasswordResetForm
    success_url = '/login/'

