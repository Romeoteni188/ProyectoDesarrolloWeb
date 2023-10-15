from django import forms

from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion',"estado"]
        labels = {'descripcion':"Descripcion de la categoria",
                "estado":"Estado"}
        widgets={'descripcion':forms.TextInput}

    def _init_(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True)
        .order_by('descripcion')

    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion',"estado"]
        labels = {'descripcion':"Sub Categoria",
                "estado":"Estado"}
        widgets={'descripcion':forms.TextInput}

    def _init_(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"

#marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion',"estado"]
        labels = {'descripcion':"Descripcion de la marca",
                "estado":"Estado"}
        widgets={'descripcion':forms.TextInput}

    def _init_(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

#unidad
class UMForm(forms.ModelForm):
    class Meta:
        model=UnidadMedida
        fields = ['descripcion',"estado"]
        labels = {'descripcion':"Descripcion de la marca",
                "estado":"Estado"}
        widgets={'descripcion':forms.TextInput}

    def _init_(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

#producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','codigo_barra',
                'descripcion' ,'estado',\
                'precio' ,'existencia','ultima_compra',\
                'marca','subcategoria' ,'unidad_medida']
        exclude=['um','fm','uc','fc']
        widget={'descripcion':forms.TextInput()}

    def _init_(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrsx.update({
                'class':'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly']=True
        self.fields['existencia'].widget.attrs['readonly']=True
        