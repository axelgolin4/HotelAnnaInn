from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.LoginFormView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name = 'logout'),
]