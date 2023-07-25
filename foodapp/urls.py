from django.urls import path
from . import views

app_name = "foodapp"
urlpatterns = [
    path('',views.index,name="home"),
    path('login/', views.CustomLoginView.as_view(),name='login'),
    path('signup/', views.registration_view, name="signup"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
]
