from django import forms
from django.forms import ModelForm
from models import Shop, User, Fronut

# class RegisterFronutForm(forms.Form):
#     user_name = forms.ModelChoiceField(label='Who are you?', choices=User.objects.all())
#     shop_name = forms.ChoiceField(label='Who is your fronut supplier?', choices=Shop.objects.all())
#     initial_amount = forms.IntegerField(label="How many did you bring?", initial=12)
#     notes = forms.TextField(label="Notes", initial="Mmmmmmmmmm Donuts")

class RegisterFronutForm(ModelForm):
    class Meta:
        model = Fronut
        fields = ['user', 'shop', 'initial_amount', 'notes']