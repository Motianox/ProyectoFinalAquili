from django.urls import path

from cuentas.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup', register, name='Register'),
    path('login', login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('update', update_acc, name='UpdateAcc'),
    path('avatar', add_avatar, name='AddAvatar'),
    path('profile', profile, name='Profile'),
    path('addinfo', add_info, name='AddInfo'),
]