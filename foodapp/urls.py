from django.urls import path
from . import views

app_name = "foodapp"
urlpatterns = [
    path('',views.index,name="home"),
    path('login/', views.login_view),
]
