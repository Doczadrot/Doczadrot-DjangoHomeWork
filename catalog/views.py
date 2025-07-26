from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormView
from .forms import ProductForm
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.services import get_product_cache, get_products_category


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products_list'

    def get_queryset(self):
        return get_product_cache()

def category_products_view(request, category_id):
    """
    Отображает список продуктов для конкретной категории по её ID.
    """
    # Получаем объект категории. Если не найден, Django автоматически вернет 404.
    category = get_object_or_404(Category, pk=category_id)

    # Используем сервисную функцию для получения продуктов данной категории
    products = get_products_category(category_id)

    context = {
        'category': category,
        'products': products
    }
    return render(request, 'catalog/category_products.html', context)




class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100, label="Ваше имя")
    contact_phone = forms.CharField(max_length=20, label="Телефон для связи")
    contact_message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class ContactView(FormView):
    template_name = 'catalog/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['contact_name']
        phone = form.cleaned_data['contact_phone']
        message = form.cleaned_data['contact_message']
        return render(self.request, 'catalog/success.html', {
            'name': name,
            'message': 'Спасибо за ваше сообщение! Мы свяжемся с вами в ближайшее время.'
        })


class ProductListView(ListView):
    model =  Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products_detail.html'
    context_object_name = 'product'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")
        return product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
    template_name = 'catalog/product_confirm_delete.html'

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user and not self.request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")
        return product

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")
        return super().delete(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')
    # cоздаем функцию редактирования только своего продукта

    def form_valid(self, form): # функция из  CreateView
        form.instance.owner = self.request.user
        return super().form_valid(form)