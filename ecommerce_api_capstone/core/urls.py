from django.urls import path

from core.admin import AdminOrderListView
from .views import UserListCreateView
from .views import LoginView
from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListCreateView.as_view(), name= 'product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name= 'product-detail'),
]

# category urls
from .views import CategoryListCreateView, CategoryDetailView

urlpatterns += [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]

from .views import OrderListCreateView

urlpatterns += [
    path("orders/", OrderListCreateView.as_view(), name="order-list-create"),
    path("admin/orders/",AdminOrderListView.as_view(), name="admin-order-list"),
]