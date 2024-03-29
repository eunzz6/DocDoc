from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('/', views.logout, name='logout'),
    path('agree/', views.agree, name='agree'),
    path('signup/', views.signup, name='signup'),
    path('use_acc/',views.use_acc, name='use_acc'),
]