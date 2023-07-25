from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'foodapp/index.html')

def login_view(request):
    return render(request, 'login.html')

class RegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')  # Redirect to the homepage after successful registration

    def form_valid(self, form):
        # Save the user upon successful form submission.
        form.save()
        return super().form_valid(form)