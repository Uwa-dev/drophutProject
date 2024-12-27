from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html', authentication_form=LoginForm), name='login'),

    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),

    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('profile/', views.profile, name='profile'),
    # path('edit_profile/', views.edit_profile, name='edit_profile'),
    # path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),  # URL for seller dashboard
    # path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
]