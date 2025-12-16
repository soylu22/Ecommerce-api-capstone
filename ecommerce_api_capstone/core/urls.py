from django.urls import path
from .views import UserListCreateView
from .views import LoginView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('login/', LoginView.as_view(), name='login'),
]