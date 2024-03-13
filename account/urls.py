# urls.py

from django.urls import path
from .views import custom_login, custom_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
     # Password Change view
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    
    # Password Change Done view
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    # Other URLs for your project...
]

