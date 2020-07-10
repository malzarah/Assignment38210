from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='customerList'),
    path('customersList', views.CustomerListView.as_view(), name='customer_list'),
    path('productsList', views.ProductListView.as_view(), name='product_list'),
    path('supplierList', views.SupplierListView.as_view(), name='supplier_list'),
    path('countryList', views.CountryListView.as_view(), name='country_list'),
    path('customer/edit/<int:pk>/',views.CustomerUpdateView.as_view(), name='customer_edit'),
path('product/edit/<int:pk>/',views.productUpdateView.as_view(), name='product_edit'),
path('supplier/edit/<int:pk>/',views.SupplierUpdateView.as_view(), name='supplier_edit'),
path('country/edit/<int:pk>/',views.CountryUpdateView.as_view(), name='country_edit'),
    path("customers/new/", views.CustomerCreateView.as_view(), name='customer_create'),
    path("products/new/", views.ProductCreateView.as_view(), name='products_create'),
    path("suppliers/new/", views.SupplierCreateView.as_view(), name='suppliers_create'),
    path("country/new/", views.CountryCreateView.as_view(), name='country_create'),
    path('login', views.login,name='login')

]