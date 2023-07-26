from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Food, Restaurant
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate, login

from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request,'foodapp/index.html')

def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('foodapp:home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'foodapp/login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('foodapp:home')
        else:
            messages.error(request, 'There was an error in the form submission. Please correct the errors and try again.')
    else:
        form = RegistrationForm()

    return render(request, 'foodapp/signup.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logout successful.')
        return reverse_lazy('foodapp:home')
    
class AddRestaurant(CreateView):
    model = Restaurant
    fields = '__all__'
    success_url = reverse_lazy("foodapp:restaurant_list")

class RestaurantList(ListView):
    model = Restaurant
    context_object_name = 'restaurant_list'

class AddFood(CreateView):
    model = Food
    fields = '__all__'
    success_url = reverse_lazy("foodapp:restaurant_list")

class FoodList(ListView):
    model = Food
    context_object_name = 'food_list'

