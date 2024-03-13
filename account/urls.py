# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Login view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Logout view
    path('logout/', views.logout_view, name='logout'),

    #logged out
    path('logged_out/', views.logged_out_view, name='logged_out'),
    
    # Password Change view
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    
    # Password Change Done view
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
]
