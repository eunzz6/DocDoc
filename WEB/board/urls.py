from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    path('<int:pk>',views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/',views.create, name="create"),
    path('<int:pk>/remove/', views.remove, name='remove'),
    path('<int:pk>/update/', views.update, name='update'),
    path('download/<int:pk>/', views.download_file, name='download'),

]
