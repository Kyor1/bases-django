from django.urls import path, include
from django.contrib.auth import views as auth_views
from bases.views import HomeSinPrivilegios,SinPrivilegios,avisos_list, Transferir




urlpatterns = [
    
    

    path('sin_privilegios/',HomeSinPrivilegios.as_view(), name='sin_privilegios'),
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),name='login'),
    path('',avisos_list, name='avisos_list'),
    path('transferir/',Transferir.as_view(), name='transferir'),
    
]