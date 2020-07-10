from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#
# def index(request):
#     return HttpResponse("Hello, world. You're at the Shop index.")
from django.urls import reverse_lazy

from django.views.generic import ListView, UpdateView, CreateView

from .models import Customer, Product, supplier, Countrie
from django.contrib.auth.mixins import LoginRequiredMixin


def login(request):
    return render(request, "registration/login.html")

def homepage(request):
    print('yessss')
    # return HttpResponse("test common")
    return render(request, "assign3static/landing_page.html", {})


class CustomerListView(ListView):
    model = Customer
    template_name = 'assign3static/Customer_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'assign3static/product_list.html'


class SupplierListView(ListView):
    model = supplier
    template_name = 'assign3static/supplier_list.html'


class CountryListView(ListView):
    model = Countrie
    template_name = 'assign3static/country_list.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('first_name', 'last_name', 'city', 'state', 'zip', 'notes')
    template_name = 'assign3static/edit_customer.html'
    success_url = reverse_lazy('customer_list')
    login_url = ''

class productUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_manufacturer', 'product_price', 'product_available_status')
    template_name = 'assign3static/edit_product.html'
    success_url = reverse_lazy('product_list')
    login_url = 'login'





class SupplierUpdateView(UpdateView):
    model = supplier
    fields = ('supplier_name', 'supplier_created')
    template_name = 'assign3static/edit_supplier.html'
    success_url = reverse_lazy('supplier_list')
    # login_url = 'login'



class CountryUpdateView(UpdateView):
    model = Countrie
    fields = ('country_code', 'country_name')
    template_name = 'assign3static/edit_country.html'
    login_url = 'login'
    success_url = reverse_lazy('country_list')


class CustomerCreateView(CreateView):
    model = Customer
    fields = ('first_name', 'last_name', 'city', 'state', 'zip', 'notes')
    template_name = 'assign3static/add_country.html'
    success_url = reverse_lazy('customer_list')
    login_url = 'login'


class ProductCreateView( CreateView):
    model = Product
    fields = ('product_name', 'product_manufacturer', 'product_price', 'product_available_status')
    template_name = 'assign3static/add_product.html'
    success_url = reverse_lazy('product_list')
    login_url = 'login'



class SupplierCreateView(CreateView):
    model = supplier
    fields = ('supplier_name', 'supplier_created')
    template_name = 'assign3static/add_supplier.html'
    success_url = reverse_lazy('common:supplier_list')
    login_url = 'login'




class CountryCreateView(CreateView):
    model = Countrie
    fields = ('country_code', 'country_name')
    template_name = 'assign3static/add_country.html'
    success_url = reverse_lazy('country_list')
    login_url = 'login'

