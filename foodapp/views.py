from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Food, Restaurant
from django.views.generic import CreateView, ListView

from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request,'foodapp/index.html')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    success_url = reverse_lazy('foodapp:home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)

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

