from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


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



class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products_detail.html'
