from django.urls import path
from . import views
from .views import sendMail


app_name = 'employee'

urlpatterns = [
    path('email/', views.sendMail),
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('<slug>/', views.SingleView.as_view(), name='single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),

]