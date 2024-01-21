from django import forms
from .models import Travel, Promotion, Category

class BaseForm(forms.ModelForm):
    def save(self, commit=True, **kwargs):
        instance = super().save(commit=False)
        if 'request' in kwargs:
            instance.created_by = kwargs['request'].user
        if commit:
            instance.save()
        return instance

class TravelForm(BaseForm):
    class Meta:
        model = Travel
        fields = ['title', 'description', 'category', 'starting_point', 'ending_point', 'price', 'image', 'trip_type', 'departure_date', 'return_date']
        exclude = ['created_by']

        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'return_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

class PromotionForm(BaseForm):
    class Meta:
        model = Promotion
        exclude = ['created_by']

class CategoryForm(BaseForm):
    class Meta:
        model = Category
        exclude = ['created_by']
