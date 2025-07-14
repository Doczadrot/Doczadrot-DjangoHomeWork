from django.shortcuts import render

from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormView
from .forms import ProductForm
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products_list'




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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')
    template_name = 'catalog/product_confirm_delete.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:products_list')


