from django import forms 

from .models import Proveedor, Proveedor

class ProveedorForm(forms.ModelForm):
   # email=forms.EmailField(max_length=240)
    class Meta:
        model: Proveedor 
        fields=['estado','descripcion','direccion','contacto',\
                'telefono','email']
        exclude = ['um','fm','uc','fc']
        widget={'descripcion':forms.TextInput()}
    
    def _init_(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
