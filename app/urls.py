
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('form/', views.fill_form, name='form'),
    path('logout/', views.logout_view, name='logout'),
]
