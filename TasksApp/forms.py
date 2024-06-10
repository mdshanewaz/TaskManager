from django.forms import ModelForm
from django import forms
from TasksApp.models import TaskModel


# Forms Stat here
class TasksForm(ModelForm):
    class Meta:
        model = TaskModel
        exclude = ('user', 'create_date', 'completed')
        
        widgets = {
            'due_date' : forms.DateInput(attrs={'type': 'date'}),
        }

class TaskfilterForm(forms.Form):
    # category = forms.ModelChoiceField(queryset=CategoryModel.objects.all(), empty_label="All Categories", required=False)
    # brand = forms.ModelChoiceField(queryset=BrandModel.objects.all(), empty_label="All Brands", required=False)
    # warranty = forms.ModelChoiceField(queryset=WarrantyModel.objects.all(), empty_label="All Warranties", required=False)
    # min_price = forms.IntegerField(label='Min Price', required=False)
    # max_price = forms.IntegerField(label='Max Price', required=False)

    # create_date = forms.ModelChoiceField()
    pass
