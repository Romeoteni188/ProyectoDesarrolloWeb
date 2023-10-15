from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json

from .models import Proveedor
from .forms import ProveedorForm


class ProveedorView(LoginRequiredMixin,generic.ListView):
    model=Proveedor
    template_name ="cmp/proveedor_list.html"
    content_object_name="obj"
    login_url="bases:login"

class ProveedorNew(LoginRequiredMixin,generic.ListView):
    model=Proveedor
    template_name ="cmp/proveedor_form.html"
    content_object_name='obj'
    form_class=ProveedorForm
    suscces_url=reverse_lazy("cmp:proveedor_list")
    login_url='bases:login'

    def form_valid(self,form):
        form.instance.uc=self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin,generic.ListView):
     model=Proveedor
     template_name ="cmp/proveedor_form.html"
     content_object_name='obj'
     form_class=ProveedorForm
     suscces_url=reverse_lazy("cmp:proveedor_list")
     login_url='bases:login'

     def form_valid(self,form):
         form.instance.um=self.request.user.id
         print(self.request.user.id)
         return super().form_valid(form)
     
def proveedorInactivar(request,id):
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv=Proveedor.objects.filter(pk=id).first()

    if not prv:
     return HttpResponse('Proveedor no existe'+ str(id))

    if request.method =='GET':
     contexto={'obj':prv}
    
    if request.method =='POST':
     prv.estado=False
     prv.save()
     contexto={'obj':'ok'}
     return HttpResponse('Proveedor Inactivo')

    return render(request,template_name,contexto)
