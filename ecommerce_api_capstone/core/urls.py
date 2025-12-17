from django.urls import path
from .views import UserListCreateView
from .views import LoginView
from .views import ProductListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListCreateView.as_view(), name = 'product-list-create')
]