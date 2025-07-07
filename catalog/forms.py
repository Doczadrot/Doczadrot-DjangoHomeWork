from django import forms
from .models import Product
from django.core.exceptions import ValidationError

# Константа запрещенных слов
FORBIDDEN_WORDS = ["казино", "криптовалюта", "крипта", "биржа",
                   "дешево", "бесплатно", "обман", "полиция", "радар"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'name':
                field.widget.attrs['placeholder'] = 'Введите название:'
            elif field_name == 'description':
                field.widget.attrs['placeholder'] = 'Заполните описание:'
            elif field_name == 'price':
                field.widget.attrs['placeholder'] = 'Введите цену:'

            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        # Валидация на запрещенные слова для имени
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word in name.lower():  # Проверяем без учета регистра
                raise ValidationError(f"Слово '{word}' не разрешено в названии продукта.")
        return name

    def clean_description(self):
        # Валидация на запрещенные слова для описания
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word in description.lower():  # Проверяем без учета регистра
                raise ValidationError(f"Слово '{word}' не разрешено в описании продукта.")
        return description

    def clean_price(self):
        # Кастомная валидация для поля price
        price = self.cleaned_data['price']
        if price is not None and price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price



