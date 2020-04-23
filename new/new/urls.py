from django.contrib import admin
from django.urls import path
from account import views
from account.views import registration_view

from rest_framework.authtoken.views import obtain_auth_token

from django.contrib.auth import views as auth_views

app_name = "account"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
