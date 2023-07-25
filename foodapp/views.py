from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request,'foodapp/index.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, 'Login successful.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('foodapp:home')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'foodapp/signup.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logout successful.')
        return reverse_lazy('foodapp:home')
