from django.contrib.admin.widgets import AutocompleteSelect
from django import forms
from .models import Raza, Producto, Marca
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RazaForm(forms.ModelForm):
    #validadores en los formularios
    nombre = forms.CharField(min_length=3)
    precio = forms.IntegerField()
     
    class Meta:
        model = Raza
        fields = '__all__'
        
class MarcaForm(forms.ModelForm):
       nombre = forms.CharField(min_length=3)     
       class Meta:
        model = Marca
        fields = '__all__'
        
class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3)
    precio = forms.IntegerField()
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        
#de esta forma transformo los campos en ingles del user default de django a español        
class CustomerUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomerUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"
        
        
        
        
           